import numpy as np
import matplotlib.pyplot as plt

dict = {'family': 'serif',
        'color': 'darkred',
        'fontweight': 20,
        'size': 15}


# This is the function for the cost function.
def f(a):
    return a ** 2 + a + 1


# This is the function for the derivative.
def df(a):
    return 2 * a + 1


x = np.linspace(start=-3.0, stop=3.0, num=500)

plt.figure(figsize=(15, 5))
# This is the code for the first graph.
plt.subplot(1, 2, 1)
plt.title("The Cost Function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("F(x)", fontdict=dict)
plt.xlim((-3, 3))
plt.ylim((0, 10))
plt.plot(x, f(x), linewidth=5)
# plt.show()


# This is the code for the second graph.
plt.subplot(1, 2, 2)
plt.grid()
plt.title("Slope of the cost function", fontdict=dict, pad=20.5)
plt.xlabel("X", fontdict=dict)
plt.ylabel("F'(x)", fontdict=dict)
plt.xlim((-2, 3))
plt.ylim((-3, 6))
plt.plot(x, df(x), linewidth=5)
plt.show()


new_x = 3
previous_x = 0
step_multiplier = .1

for n in range(500):
    previous_x = new_x
    gradient = df(previous_x)
    new_x = previous_x - step_multiplier * gradient
    print("This is the value of new X ", new_x)

