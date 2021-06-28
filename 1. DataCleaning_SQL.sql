
/* NYC Cafe Data cleaning

*/

SELECT TOP 10 *
from dbo.sales_reciepts;


--------------------------------------------------------------------------------------------------------------------------
-- Ivestigate NULL's
-- Null per column count

SELECT *
FROM dbo.sales_reciepts;

SELECT 
    COUNT(*)-COUNT(transaction_id) as transaction_id, 
    COUNT(*)-COUNT(transaction_date) as transaction_date, 
    COUNT(*)-COUNT(transaction_time) As transaction_time, 
    COUNT(*)-COUNT(sales_outlet_id) As sales_outlet_id,
    COUNT(*)-COUNT(staff_id) As staff_id,
    COUNT(*)-COUNT(customer_id) As scustomer_id,
    COUNT(*)-COUNT(line_item_id) As line_item_id,
    COUNT(*)-COUNT(product_id) As product_id,
    COUNT(*)-COUNT(quantity) As quantity,
    COUNT(*)-COUNT(unit_price) As unit_price,
    COUNT(*)-COUNT(line_item_amount) As line_item_amount,
    COUNT(*)-COUNT(promo_item_YesNo) As promo_item_YesNo
FROM dbo.sales_reciepts;


--------------------------------------------------------------------------------------------------------------------------
-- Investigate Zero's
-- Replace Customer_ID of 0 with NULL

UPDATE dbo.sales_reciepts
SET customer_id = CASE WHEN customer_id = 0 THEN NULL else customer_id END
WHERE customer_id = 0;



-- Assume if the line_item_amout is zero and there is not a promotion (ie. promo_item_YesNo is 'NO'), the entry has an error

SELECT 
    SUM(CASE WHEN line_item_amount = 0 THEN 1 else 0 END) as line_item_amount 
FROM dbo.sales_reciepts
WHERE promo_item_YesNo = 'No';


--------------------------------------------------------------------------------------------------------------------------
-- Invstigate Promo Sales
SELECT transaction_date, product_id
from dbo.sales_reciepts
WHERE promo_item_YesNo = 'Yes'
GROUP BY product_id, transaction_date
ORDER BY transaction_date;




--------------------------------------------------------------------------------------------------------------------------
-- Identify Duplicates using CTE (Going to assume that rows with identical transaction_id, transaction_date, transaction_time, sales_outlet_id, staff_id, line_item_id, product_id and quantity values, are duplicate entries)

WITH RowNumCTE AS (

SELECT *,
    ROW_NUMBER() OVER (
        PARTITION BY transaction_id, transaction_date, transaction_time, sales_outlet_id, staff_id, line_item_id, product_id, quantity
        ORDER BY transaction_id
    ) AS row_num

FROM dbo.sales_reciepts

)

/* Select duplicates only (104 duplicates found)

SELECT *
FROM RowNumCTE
WHERE row_num > 1;

*/

-- Delete Duplicates
DELETE 
FROM RowNumCTE
WHERE row_num > 1;




--------------------------------------------------------------------------------------------------------------------------
-- Create new Transaction tables
    -- Create new transactions table using subset of columns, spitting quantity entries and performing joins

SELECT transaction_id, transaction_date, transaction_time, sales_outlet_id, customer_id, product_id, quantity, unit_price, promo_item_YesNo
INTO dbo.transactions
FROM dbo.sales_reciepts;

SELECT TOP 10 *
FROM dbo.transactions
ORDER BY transaction_date;


-- Spitting quantity entries using CTE (replicate entries for quantity > 1)

WITH ReplicateTable(transaction_id, transaction_date, transaction_time, sales_outlet_id, customer_id, product_id, quantity, unit_price, promo_item_YesNo
, repeat) as
   (
      SELECT
        transaction_id, transaction_date, transaction_time, sales_outlet_id, customer_id, product_id, quantity, unit_price, promo_item_YesNo
        , 1
      FROM
        dbo.transactions
      UNION ALL
      SELECT
        transaction_id, transaction_date, transaction_time, sales_outlet_id, customer_id, product_id, quantity, unit_price, promo_item_YesNo
        , repeat + 1
      FROM
        ReplicateTable R
      WHERE
        R.repeat < R.quantity
   )
SELECT
    *
INTO dbo.transaction_reps
FROM
    ReplicateTable
ORDER BY
   transaction_id
    , customer_id;
GO

SELECT COUNT(*)
FROM dbo.transactions;

SELECT COUNT(*)
FROM dbo.transaction_reps;

ALTER TABLE dbo.transaction_reps
DROP COLUMN quantity

SELECT TOP 10 *
FROM dbo.transaction_reps;



-- ADD DateTime Column
ALTER TABLE dbo.transaction_reps
ADD [transaction_datetime] [datetime] NULL;

ALTER TABLE dbo.transaction_reps
ALTER COLUMN transaction_date datetime;

ALTER TABLE dbo.transaction_reps
ALTER COLUMN transaction_time datetime;

UPDATE dbo.transaction_reps
SET transaction_datetime = transaction_date + transaction_time;

ALTER TABLE dbo.transaction_reps
ALTER COLUMN transaction_date date;

ALTER TABLE dbo.transaction_reps
ALTER COLUMN transaction_time TIME;


-- Add and calculate Profit column

ALTER TABLE dbo.transaction_reps
ADD [transaction_profit] [float] NULL;

ALTER TABLE dbo.transaction_reps
ADD [wholesale_price] [float] NULL;

UPDATE dbo.transaction_reps
SET wholesale_price = (SELECT current_wholesale_price
                        FROM dbo.product
                        WHERE dbo.transaction_reps.product_id = dbo.product.product_id);

UPDATE dbo.transaction_reps
SET transaction_profit = unit_price - wholesale_price;


SELECT *
FROM dbo.transaction_reps
ORDER BY transaction_id, transaction_date, transaction_time


--------------------------------------------------------------------------------------------------------------------------
-- Generating Unique Transaction ID's based on transaction id, date, time, and store_id

-- This output shows that there are many transactions share the same transaction_id, I assume this must be due to the POS system used
SELECT *
FROM dbo.transaction_reps
ORDER BY transaction_id, transaction_date, transaction_time

-- Generate Unique ID & export output
SELECT DENSE_RANK() OVER(ORDER BY transaction_date, transaction_time, sales_outlet_id, transaction_id) AS unique_ID,
       transaction_id,
       transaction_date,
       transaction_time,
       transaction_datetime,
       product_id,
       sales_outlet_id,
       customer_id,
       unit_price,
       transaction_profit
FROM dbo.transaction_reps;

--------------------------------------------------------------------------------------------------------------------------
SELECT *
FROM dbo.transaction_reps;







-- NYC Weather data analysis
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------


-- Generate new daily sales summary table ('daily_sales'), which will be used for sales forcasting using python

SELECT transaction_date, COUNT(transaction_id) as sales_count, SUM(unit_price) as revenue, SUM(transaction_profit) as profit
INTO dbo.daily_sales
FROM dbo.transaction_reps
GROUP BY transaction_date;


SELECT *
FROM dbo.daily_sales
ORDER BY transaction_date


-- Generate date column for weather datasets
--2019
ALTER TABLE dbo.NYC_weather19
ADD [date] date;

UPDATE dbo.NYC_weather19
SET date = CONVERT(DATE,CAST([year] AS VARCHAR(4))+'-'+
                    CAST([month] AS VARCHAR(2))+'-'+
                    CAST([day] AS VARCHAR(2)));

SELECT *
FROM dbo.NYC_weather19


-- JOIN daily_sales with weather data
SELECT w.city, w.date, w.precipitation, w.rel_humidity, w.avg_temp, w.max_temp, w.min_temp, w.range_temp, d.sales_count, d.revenue, d.profit
FROM NYC_weather.dbo.NYC_weather19 w
JOIN NYC_Cafes.dbo.daily_sales d ON w.date = d.transaction_date


--------------------------------------------------------------------------------------------------------------------------
