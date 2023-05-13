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

# This is the code for the first graph.

plt.subplot(1, 2, 1)
plt.title("The Cost Function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("g(x)", fontdict=dict)
plt.xlim((-2, 2))
plt.ylim((0.5, 5.5))

plt.plot(x, g(x), linewidth=5)

# This is the code for the second graph.

plt.subplot(1, 2, 2)
plt.grid()
plt.title("Slope of the cost function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("d'(x)", fontdict=dict)
plt.xlim((-2, 2))
plt.ylim((-6, 8))
plt.plot(x, dg(x), linewidth=5)
plt.show()
