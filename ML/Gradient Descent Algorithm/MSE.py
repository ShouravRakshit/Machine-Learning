import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def mse(y, y_hat):
    result = 0
    for i in range(len(y)):
        result = result + (y[i] - y_hat[i]) ** 2

    return result / len(y)


x = np.array([[.1, 1.2, 2.4, 3.2, 4.1, 5.7, 6.5]]).transpose()
y = np.array([[1.7, 2.4, 3.5, 3.0, 6.1, 9.4, 8.2]]).transpose()
print(x.shape)
print(y.shape)
regression = LinearRegression()
regression.fit(x, y)
predict_value_y = regression.predict(x)
print("The intercept of the line is :", regression.intercept_)
print("The slope of the line is :", regression.coef_)

plt.scatter(x, y, s=70)
plt.plot(x, predict_value_y, color="orange", linewidth=4)
plt.xlabel("x values")
plt.ylabel("y values")
y_predicted_vals = .84753515 + 1.22272646 * x

MSE = mse(y, y_predicted_vals)
print("The value of MSE is :", MSE)
plt.show()
