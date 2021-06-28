# Cafe Sales Analysis & Forecast Prediction

# --------------------------------------------------------------------------------------------------------------------------
# Import necessary packages

import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

from warnings import filterwarnings
filterwarnings('ignore')



# --------------------------------------------------------------------------------------------------------------------------
# Step 1: Import & EDA
sales = pd.read_csv('sales_weather_joined.csv')
# print(sales.head(5))
#
# sns.lmplot(x='avg_temp', y='sales_count', data=sales)
# plt.title('Average Temp vs Sales Count')
# plt.xlabel('Average Temp (degC)')
# plt.ylabel('Daily Sales Count ')
#
# plt.show()




# --------------------------------------------------------------------------------------------------------------------------
# Subplots

# # Correlation Co-efficients
# r_avg, p_avg = stats.pearsonr(sales.avg_temp, sales.sales_count)
# r_range, p_range = stats.pearsonr(sales.range_temp, sales.sales_count)
# r_hum, p_hum = stats.pearsonr(sales.rel_humidity, sales.sales_count)
# r_prec, p_prec = stats.pearsonr(sales.precipitation, sales.sales_count)
#
# # Figure & Graph setup
# fig, axes = plt.subplots(
#                      ncols=2,
#                      nrows=2, figsize=(10, 7))
#
# ax1, ax2, ax3, ax4 = axes.flatten()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
#
# fig.suptitle('Linear Regression Analysis of Weather variables vs Daily Sales Count')
#
# # Annotation formatting
# bbox_args = dict(boxstyle="round", fc="none", ec="gray", alpha=0.8)
#
# # Avg_temp
# avg = sns.regplot(x='avg_temp', y='sales_count', data=sales, ax=ax1)
# avg.set_xlabel('Average Temp (degC)')
# avg.set_ylabel('Daily Sales Count')
#
# ax1.annotate('r = {:.2f} '.format(r_avg), xy=(0.94, 1), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
# ax1.annotate('p = {:.2e}'.format(p_avg), xy=(1, 0.87), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
#
# # Range_temp
# range = sns.regplot(x='range_temp', y='sales_count', data=sales, ax=ax2)
# range.set_xlabel('Daily Temp Range (degC)')
# range.set_ylabel('Daily Sales Count')
#
# ax2.annotate('r = {:.2f} '.format(r_range), xy=(0.94, 1), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
# ax2.annotate('p = {:.2e}'.format(p_range), xy=(1, 0.87), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
#
#
#
# # Rel_humidity
# hum = sns.regplot(x='rel_humidity', y='sales_count', data=sales, ax=ax3)
# hum.set_xlabel('Relative Humidity (%)')
# hum.set_ylabel('Daily Sales Count')
#
# ax3.annotate('r = {:.2f} '.format(r_hum), xy=(0.94, 1), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
# ax3.annotate('p = {:.2e}'.format(p_hum), xy=(1, 0.87), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
#
#
#
# # Precipitation
# prec = sns.regplot(x='precipitation', y='sales_count', data=sales, ax=ax4)
# prec.set_xlabel('Daily Precipitation (mm)')
# prec.set_ylabel('Daily Sales Count')
#
# ax4.annotate('r = {:.2f} '.format(r_prec), xy=(0.94, 1), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
# ax4.annotate('p = {:.2e}'.format(p_prec), xy=(1, 0.87), xycoords='axes fraction',
#              xytext=(-20, -20), textcoords='offset points',
#              ha="right", va="top",
#              bbox=bbox_args)
#
#
# plt.show()





# --------------------------------------------------------------------------------------------------------------------------
# Joint Plots for Correlated Variables

# Avg_temp
# joint = sns.jointplot(x='avg_temp', y='sales_count', data=sales, kind='reg')
#
# plt.xlabel('Average Temp (degC)')
# plt.ylabel('Daily Sales Count ')
# plt.ylim(2000, 3000)
# joint.fig.suptitle('Daily Sales Count vs Average Temperature')
# joint.ax_joint.set_xlabel('Average Temp (degC)')
# joint.ax_joint.set_ylabel('Daily Sales Count')
# joint.ax_joint.plot([], [], linestyle="", alpha=0)
#
# r, p = stats.pearsonr(sales.avg_temp, sales.sales_count)
#
# joint.ax_joint.annotate('r = {:.2f} '.format(r), xy=(.8, .9), xycoords=joint.ax_joint.transAxes,
#   bbox=dict(boxstyle="round", fc="none", ec="gray", alpha=0.8))
# joint.ax_joint.annotate('p = {:.2e}'.format(p), xy=(.8, .85), xycoords=joint.ax_joint.transAxes,
#   bbox=dict(boxstyle="round", fc="none", ec="gray", alpha=0.8))
#
# plt.tight_layout()
# plt.show()


# Rel_humidity
# joint = sns.jointplot(x='rel_humidity', y='sales_count', data=sales, kind='reg')
#
# plt.xlabel('Relative Humidity (%)')
# plt.ylabel('Daily Sales Count ')
# plt.ylim(2000, 3000)
# joint.fig.suptitle('Daily Sales Count vs Relative Humidity')
# joint.ax_joint.set_xlabel('Relative Humidity (%)')
# joint.ax_joint.set_ylabel('Daily Sales Count')
# joint.ax_joint.plot([], [], linestyle="", alpha=0)
#
# r, p = stats.pearsonr(sales.rel_humidity, sales.sales_count)
#
# joint.ax_joint.annotate('r = {:.2f} '.format(r), xy=(.8, .9), xycoords=joint.ax_joint.transAxes,
#   bbox=dict(boxstyle="round", fc="none", ec="gray", alpha=0.8))
# joint.ax_joint.annotate('p = {:.2e}'.format(p), xy=(.8, .85), xycoords=joint.ax_joint.transAxes,
#   bbox=dict(boxstyle="round", fc="none", ec="gray", alpha=0.8))
#
# plt.tight_layout()
# plt.show()





# --------------------------------------------------------------------------------------------------------------------------
# Sales Prediction using a Multivarient Linear Regression Model

# # Assign Variables
# y = sales['sales_count']
# X = sales[['avg_temp', 'rel_humidity']]
# # print(X)
#
#
# # Split Train and Test sets
# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# # print(X_train.shape)
#
#
# # Fit & Train Model
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
#
# regr = LinearRegression(fit_intercept=True)
#
# regr.fit(X_train, y_train)
#
# print('Intercept: ', regr.intercept_)
# print('Coefficients: ', regr.coef_)
#
# # Evaluate Fitting
# print('R^2 train score: ', regr.score(X_train, y_train))
#
# # 5-fold Cross validation of R^2 scores
# from sklearn.model_selection import cross_val_score
# cv_scores = cross_val_score(regr, X, y, cv=5)
# print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))
#
#
# # Predict on test set
# y_predict = regr.predict(X_test)
#
#
# # Evaluate Model
# rmse = mean_squared_error(y_test, y_predict, squared=False)
# print("Root Mean Squared Error of Prediction: {}".format(rmse))
#
# from sklearn.metrics import mean_absolute_percentage_error
# mape = mean_absolute_percentage_error(y_test, y_predict)
# print("Mean Absolute Percentage Error of Prediction: {}".format(mape))



# # Creating GUI to predict sales
# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
#
# # tkinter GUI
# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=500, height=300)
# canvas1.pack()
#
# # with sklearn
# Intercept_result = ('Intercept: ', regr.intercept_)
# label_Intercept = tk.Label(root, text=Intercept_result, justify='center')
# canvas1.create_window(260, 220, window=label_Intercept)
#
# # with sklearn
# Coefficients_result = ('Coefficients: ', regr.coef_)
# label_Coefficients = tk.Label(root, text=Coefficients_result, justify='center')
# canvas1.create_window(260, 2400, window=label_Coefficients)
#
#
# # New_Avg_Temp label and input box
# label1 = tk.Label(root, text='Enter Average Temperature: ')
# canvas1.create_window(87, 100, window=label1)
#
# entry1 = tk.Entry(root)  # create 1st entry box
# canvas1.create_window(270, 100, window=entry1)
#
# # New_Rel_humidity label and input box
# label2 = tk.Label(root, text='Enter Relative Humidity: ')
# canvas1.create_window(100, 120, window=label2)
#
# entry2 = tk.Entry(root)  # create 2nd entry box
# canvas1.create_window(270, 120, window=entry2)
#
#
# def values():
#     global New_Avg_Temp  # our 1st input variable
#     New_Avg_Temp = float(entry1.get())
#
#     global New_Relative_Humidity  # our 2nd input variable
#     New_Relative_Humidity = float(entry2.get())
#
#     Prediction_result = ('Predicted Daily Sales Count: ', regr.predict([[New_Avg_Temp, New_Relative_Humidity]]))
#     label_Prediction = tk.Label(root, text=Prediction_result, bg='orange')
#     canvas1.create_window(260, 280, window=label_Prediction)
#
#
# button1 = tk.Button(root, text='Predict Daily Sales Count', command=values,
#                     bg='orange')  # button to call the 'values' command above
# canvas1.create_window(270, 150, window=button1)
#
# # plot 1st scatter
# figure3 = plt.Figure(figsize=(5, 4), dpi=100)
# ax3 = figure3.add_subplot(111)
# ax3.scatter(sales['avg_temp'].astype(float), sales['sales_count'].astype(float), color='r')
# scatter3 = FigureCanvasTkAgg(figure3, root)
# scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
# ax3.set_xlabel('Average Temp (degC)')
# ax3.set_ylabel('Daily Sales Count')
# ax3.set_title('Average Temperature vs Daily Sales Count')
#
# # plot 2nd scatter
# figure4 = plt.Figure(figsize=(5, 4), dpi=100)
# ax4 = figure4.add_subplot(111)
# ax4.scatter(sales['rel_humidity'].astype(float), sales['sales_count'].astype(float), color='g')
# scatter4 = FigureCanvasTkAgg(figure4, root)
# scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
# ax4.set_xlabel('Relative Humidity')
# ax4.set_ylabel('Daily Sales Count')
# ax4.set_title('Relative Humidity vs Daily Sales Count')
#
# root.mainloop()