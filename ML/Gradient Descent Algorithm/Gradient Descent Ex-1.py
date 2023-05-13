import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# This is the function for the cost function.
def f(a):
    return a ** 2 + a + 1


# This is the function for the derivative.
def df(a):
    return 2 * a + 1


dict = {'family': 'serif',
        'color': 'darkred',
        'fontweight': 20,
        'size': 15}

x = np.linspace(start=-3.0, stop=3.0, num=500)
plt.figure(figsize=(18, 8))

new_x = 3
step_multiplier = .1
precision = .00001

x_list = []
slope_list = []

# This is the algorithm for the Gradient Descent.
for n in range(500):
    gradient = df(new_x)
    new_x = new_x - step_multiplier * gradient
    x_list.append(new_x)
    slope_list.append(gradient)
    if abs(gradient) < precision:
        print("This is the number of times the loop ran ", n)
        break

print("In this x point we find the lowest value ", new_x)
print("This is the value of my slope ", df(new_x))
print("This is the value of the cost function ", f(new_x))

# This is the code for the first graph.
plt.subplot(1, 3, 1)
plt.title("The Cost Function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("F(x)", fontdict=dict)
plt.xlim((-3, 3))
plt.ylim((0, 10))
values = np.array(x_list)
plt.scatter(x_list, f(values), color="red", s=80, alpha=.8)
plt.plot(x, f(x), linewidth=5)

# This is the code for the second graph.
plt.subplot(1, 3, 2)
plt.grid()
plt.title("Slope of the cost function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("F'(x)", fontdict=dict)
plt.xlim((-2, 3))
plt.ylim((-3, 6))
plt.plot(x, df(x), linewidth=5)
plt.scatter(x_list, slope_list, alpha=.8, color="orange", s=90)

# This is the Gradient Descent chart.
plt.subplot(1, 3, 3)
plt.grid()
plt.title("Gradient Descent (Close up)", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.xlim((-.60, -.2))
plt.ylim((-.3, .9))
plt.plot(x, df(x), linewidth=5)
plt.scatter(x_list, slope_list, alpha=.8, color="orange", s=90)

plt.show()
