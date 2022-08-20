from xgboost import XGBRegressor, plot_importance 
import pandas as pd
import numpy as np
import math
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

rating = pd.read_csv("./ratings.csv")
feature_movie = pd.read_csv("./feature_movie.csv")
feature_movie = feature_movie.drop(feature_movie.columns[5], axis=1)
feature_user = pd.read_csv("./feature_user.csv")
feature_user = feature_user.drop(feature_user.columns[5], axis=1)

rating = rating.drop(rating.columns[3], axis=1)

data = pd.concat([feature_movie, feature_user], axis=1)
data = pd.concat([rating, data], axis = 1)

data = data.fillna(data.mean())

x = data[['sim_movie2','sim_movie3','sim_movie4','sim_movie5',  'sim_user2','sim_user3','sim_user4','sim_user5']]
col_names = ['sim_movie2','sim_movie3','sim_movie4','sim_movie5','sim_user2','sim_user3','sim_user4','sim_user5']
y = data['rating']

rgr = XGBRegressor()
rgr.fit(x, y)
plot_importance(rgr, color=[ '#b895d3', '#c195d3', '#d295d3', '#d395bd','#8fd9a6', '#8fd9b8', '#8fd9c4', '#8fd9cf'])

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
print("train MAE :", train_mae, "\n")
print("test RMSE :", test_rmse, "\n")
print("test MAE :", test_mae, "\n")
print("="*50, "\n")

plt.show()
