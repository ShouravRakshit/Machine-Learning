import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("online.csv")
dummy = pd.get_dummies(data["Area"])
dummy_df = dummy.astype(int)

merged_data = pd.concat([data, dummy_df], axis=1)

x = merged_data.drop(['Area', 'Profit'], axis=1)
y = merged_data[["Profit"]]

regression = LinearRegression()
regression.fit(x, y)

print("This is the value of intercept:", regression.intercept_)
print("This is the value of slope:", regression.coef_)

# Select a specific column from x for the scatter plot
x_column = x.columns[0]
plt.figure(figsize=(10, 5))
plt.scatter(x[x_column], y)
plt.xlabel(x_column)
plt.ylabel("Profit")
plt.show()
