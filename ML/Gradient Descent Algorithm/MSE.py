import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import cm  # color map


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
# plt.plot(x, predict_value_y, color="orange", linewidth=4)
plt.xlabel("x values")
plt.ylabel("y values")
y_predicted_vals = .84753515 + 1.22272646 * x

MSE = mse(y, y_predicted_vals)
print("The value of MSE is :", MSE)

th_0 = np.linspace(start=-1, stop=3, num=500)
th_1 = np.linspace(start=-1, stop=3, num=500)

plot_t0, plot_t1 = np.meshgrid(th_0, th_1)

plot_cost = np.zeros((500, 500))  # It creates 2d array

for i in range(500):
    for j in range(5):
        y_hat = plot_t0[i][j] + plot_t1[i][j] * x
        plot_cost[i][j] = mse(y, y_hat)

print(plot_cost)

# Plotting MSE
fig = plt.figure(figsize=[16, 12])
ax = fig.add_subplot(projection='3d')
ax.set_xlabel("Theta 0", fontsize=20)
ax.set_ylabel("Theta 1", fontsize=20)
ax.set_zlabel("Cost - MSE", fontsize=20)

ax.plot_surface(plot_t0, plot_t1, plot_cost, cmap=cm.hot)

plt.show()
