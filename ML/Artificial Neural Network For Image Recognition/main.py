from numpy.random import seed
from tensorflow import random
import keras
import os
import tensorflow as tf
import numpy as np
from IPython.display import display
from tensorflow.keras.preprocessing.image import array_to_img
import matplotlib.pyplot as plt

# Constants
label_names = ["Plane", "Car", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]

# We can get the data from a website called cs.toronto.edu
# However, we can get this dataset just by importing it from keras which is lot simpler.
from keras.datasets import cifar10
seed(888)
random.set_seed(404)

# print(type(cifar10.load_data()))

# Separating the train data from the test data. Getting the value from cifar.
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# pic = array_to_img(x_train[0])
# (display(pic))
# print(x_train.shape)

# Showing the 7th pciture.
plt.imshow(x_train[7])
plt.xlabel(label_names[y_train[7][0]], fontsize=12)



fig, axes = plt.subplots(1, 10)
ax = plt.gca()



for i in range(len(label_names)):
    # Plot the first image in the left subplot

    axes[i].imshow(x_train[i])
    axes[i].set_title(label_names[y_train[i][0]])


plt.tight_layout()
plt.show()
