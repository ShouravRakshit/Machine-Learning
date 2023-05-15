import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def h(a):
    return a ** 5 - 2 * a ** 4 + 2


def dh(a):
    return 5 * a ** 4 - 8 * a ** 3


dict = {'family': 'serif',
        'color': 'darkred',
        'fontweight': 20,
        'size': 15}

plt.figure(figsize=(15, 8))
x = np.linspace(start=-2, stop=2, num=1000)


def gradient_descent(initial_guess, learning_rate, precision):
    new_x = initial_guess

    x_list = []
    slope_list = []

    # This is the algorithm for the Gradient Descent.
    for n in range(72):
        gradient = dh(new_x)
        new_x = new_x - learning_rate * gradient
        x_list.append(new_x)
        slope_list.append(gradient)
        if abs(gradient) < precision:
            print("This is the number of times the loop ran ", n)
            break

    # print("In this x point we find the lowest value ", new_x)
    # print("This is the value of my slope ", dg(new_x))
    # print("This is the value of the cost function ", g(new_x))
    return [new_x, x_list, slope_list]


low_x_value, x_coor, slope_list = (gradient_descent(initial_guess=-.2, learning_rate=-1, precision=.001))
print("In this x point we find the lowest value ", low_x_value)
print("This is the value of my slope ", dh(low_x_value))
print("This is the value of the cost function ", h(low_x_value))
# This is the code for the first graph.
x_values = np.array(x_coor)
plt.subplot(1, 2, 1)
plt.title("The Cost Function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("h(x)", fontdict=dict)
plt.xlim((-1.2, 2.5))
plt.ylim((-1, 4))
plt.scatter(x_coor, h(x_values), color="darkred", s=100, alpha=.7)
plt.plot(x, h(x), linewidth=5, alpha=.7)

# This is the code for the second graph.

plt.subplot(1, 2, 2)
plt.grid()
plt.title("Slope of the cost function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("h'(x)", fontdict=dict)
plt.xlim((-1, 2))
plt.ylim((-4, 5))
plt.scatter(x_coor, dh(x_values), color="yellow", s=100, alpha=.7)
plt.plot(x, dh(x), linewidth=5)
plt.show()
