import numpy as np
from matplotlib import cm  # color map
import matplotlib.pyplot as plt
from sympy import symbols, diff
from mpl_toolkits.mplot3d.axes3d import Axes3D


def f(x, y):
    r = 3 ** (-x ** 2 - y ** 2)
    return 1 / (r + 1)


x = np.linspace(start=-2, stop=2, num=200)
y = np.linspace(start=-2, stop=2, num=200)
# We need meshgrid because we needed to create 2D arrays.
x, y = np.meshgrid(x, y)
Z = f(x, y)

# Partial derivatives and symbolic computation
a, b = symbols('x, y')
print("Our cost function f(x, y) is: ", f(a, b))
print("Partial derivatives with respect to x :", diff(f(a, b), a))
print("Cost at this point is ,", f(a, b).evalf(subs={a: 1.8, b: 1.0}))
print("The slope with respect to x is :", diff(f(a, b), a).evalf(subs={a: 1.8, b: 1.0}))

# Doing the gradient descent work
learning_rate = .1
# params = np.array([1.8, 1.0])
initial_x = 1.8
initial_y = 1
values_list = []
# Note in order to boost our performance we should do the partial derivatives with hand and not wit help of sympy
# library. So, in order to optimize the code we should calculate it manually.

for i in range(200):
    gradient_x = diff(f(a, b), a).evalf(subs={a: initial_x, b: initial_y})
    gradient_y = diff(f(a, b), b).evalf(subs={a: initial_x, b: initial_y})
    gradients = np.array([gradient_x, gradient_y])
    initial_x = initial_x - learning_rate * gradient_x
    initial_y = initial_y - learning_rate * gradient_y
    # values_array = np.append(values_array, params.reshape(1, 2), axis=0)
    values_list.append([initial_x, initial_y])

x_val = []
y_val = []
length = len(values_list)
for i in range(length):
    x_val.append(values_list[i][0])

print(x_val)

for i in range(length):
    y_val.append(values_list[i][1])

print(y_val)

print("Values of gradients ", gradients)
print("Minimum occurs at x value of:", initial_x)
print("Minimum occurs at y value of:", initial_y)
print("The cost is :", f(initial_x, initial_y))

fig = plt.figure(figsize=[16, 12])
ax = fig.add_subplot(projection='3d')
ax.set_xlabel("X", fontsize=25, labelpad=20)
ax.set_ylabel("Y", fontsize=25, labelpad=20)
ax.set_zlabel("f(x, y) - Cost", fontsize=25, labelpad=20)
x_val = np.array(x_val)
y_val = np.array(y_val)

ax.plot_surface(x, y, Z, cmap=cm.viridis, alpha=.4)
ax.scatter(x_val, y_val,
           f(x_val, y_val), s=60, color="red")
plt.show()
