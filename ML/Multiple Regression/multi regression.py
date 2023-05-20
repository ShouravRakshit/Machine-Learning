import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
boston_datasets = pd.DataFrame(data,
                               columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                                        'PTRATIO', 'B',
                                        'LSTAT'])
price_list = np.linspace(start=20, stop=60, num=len(boston_datasets))
# print(price_list)

boston_datasets["PRICE"] = price_list

prices = boston_datasets["PRICE"]
features = boston_datasets.drop('PRICE', axis=1)

x_train, x_test, y_train, y_test = train_test_split(features, prices, train_size=.8, random_state=10)
# print(len(x_train)/len(features))

regression = LinearRegression()
# These codes are for training dataset.
regression.fit(x_train, y_train)
intercept = regression.intercept_
coefficient = regression.coef_
print("This is the intercept for the training dataset", intercept)
print("This is the slope for the training dataset", coefficient)
print("R squared value for the training dataset", regression.score(x_train, y_train))

# These codes are for testing dataset.
regression.fit(x_test, y_test)
intercept = regression.intercept_
coefficient = regression.coef_
print("This is the intercept for the testing dataset", intercept)
print("This is the slope for the testing dataset", coefficient)
print("R squared value for the testing dataset", regression.score(x_test, y_test))

