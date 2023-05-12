import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

font1 = {'family': 'serif',
         'color': 'blue',
         'size': 10
         }
font2 = {'family': 'serif',
         'color': 'darkred',
         'size': 12
         }

df = pd.read_csv("dhaka homeprices.csv")
# print(df["price"])

x = pd.DataFrame(df, columns=["area"])
y = pd.DataFrame(df, columns=["price"])
plt.figure(figsize=(10, 5))

plt.xlabel('Area in square ft', fontdict=font1)
plt.ylabel("Price in tk", fontdict=font2)
plt.title("Home price in Dhaka", fontdict=font1, pad=20)

regression = LinearRegression()
regression.fit(x, y)
print(regression.coef_)
print(regression.intercept_)
predicted_y_value = regression.predict(x)
plt.plot(x, predicted_y_value, linewidth=5)
plt.scatter(x, y)

plt.show()
