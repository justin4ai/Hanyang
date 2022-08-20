from xgboost import XGBRegressor, plot_importance 
import pandas as pd
import numpy as np
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt                              data = pd.read_csv('features.csv')
data = data.drop(data.columns[3], axis=1)
data = data.drop(data.columns[3], axis=1)
data = data.drop(data.columns[7], axis=1)
data = data.fillna(data.mean())
display(data.head())

x = data[['sim_user2','sim_user3','sim_user4','sim_user5', 'sim_movie2','sim_movie3','sim_movie4','sim_movie5']]
col_names = ['sim_user2','sim_user3','sim_user4','sim_user5', 'sim_movie2','sim_movie3','sim_movie4','sim_movie5']
y = data['rating']

rgr = XGBRegressor()
rgr.fit(x, y)
#importance = rgr.feature_importances_
#print(importance)

ax = plot_importance(rgr,color=['#8fd9a6', '#8fd9b8', '#8fd9c4', '#8fd9cf', '#b895d3', '#c195d3', '#d295d3', '#d395bd'])
ax.figure.set_size_inches(12,6)

#plot_importance(rgr,color=['#a5d98f', '#8fd9b6', '#8fd9cf', '#8fc7d9', '#8fa0d9', '#a28fd9', '#b98fd9', '#c78fd9'])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Feature importance',fontsize=15)
plt.xlabel('F score', fontsize=15)
plt.ylabel('Features', fontsize=15)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

rgr = XGBRegressor()
rgr_train = rgr.fit(x_train, y_train)

pred_train = rgr_train.predict(x_train)
pred_test = rgr_train.predict(x_test)

train_rmse = math.sqrt(metrics.mean_squared_error(y_train, pred_train))
train_mae = mean_absolute_error(y_train, pred_train)
test_rmse = math.sqrt(metrics.mean_squared_error(y_test, pred_test))
test_mae = mean_absolute_error(y_test, pred_test)

print("\n")
print("="*50, "\n")
print("train RMSE :", train_rmse, "\n")
print("train MAE :", train_mae)
print("-"*50)
print("test RMSE :", test_rmse, "\n")
print("test MAE :", test_mae, "\n")
print("="*50, "\n")
