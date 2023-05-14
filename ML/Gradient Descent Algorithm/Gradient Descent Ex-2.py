import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def g(a):
    return a ** 4 - 4 * a ** 2 + 5


def dg(a):
    return 4 * a ** 3 - 8 * a


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
    for n in range(500):
        gradient = dg(new_x)
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


low_x_value, x_coor, slope_list = (gradient_descent(initial_guess=.5, learning_rate=.02, precision=.001))
print("In this x point we find the lowest value ", low_x_value)
print("This is the value of my slope ", dg(low_x_value))
print("This is the value of the cost function ", g(low_x_value))
# This is the code for the first graph.
x_values = np.array(x_coor)
plt.subplot(1, 2, 1)
plt.title("The Cost Function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("g(x)", fontdict=dict)
plt.xlim((-2, 2))
plt.ylim((0.5, 5.5))
plt.scatter(x_coor, g(x_values), color="darkred", s=100, alpha=.7)
plt.plot(x, g(x), linewidth=5, alpha=.7)

# This is the code for the second graph.

plt.subplot(1, 2, 2)
plt.grid()
plt.title("Slope of the cost function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("d'(x)", fontdict=dict)
plt.xlim((-2, 2))
plt.ylim((-6, 8))
plt.scatter(x_coor, dg(x_values), color="yellow", s=100, alpha=.7)
plt.plot(x, dg(x), linewidth=5)
plt.show()
