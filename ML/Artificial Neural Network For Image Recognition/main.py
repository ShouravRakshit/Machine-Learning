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
img_width = 32
img_height = 32
img_pixels = img_width * img_height
total_input = img_height * img_width * 3
validation = 10000

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
# plt.imshow(x_train[7])
# plt.xlabel(label_names[y_train[7][0]], fontsize=12)



fig, axes = plt.subplots(1, 10)
ax = plt.gca()



for i in range(len(label_names)):
    # Plot the first image in the left subplot

    axes[i].imshow(x_train[i])
    axes[i].set_title(label_names[y_train[i][0]])


plt.tight_layout()

x_train = x_train / 255.0
x_test = x_test / 255.0
# print(x_train[0][0][0][0])
# print(x_test.shape[0])
# print(x_train.shape)

x_train = x_train.reshape(x_train.shape[0], total_input)
# print(x_train.shape)
x_test = x_test.reshape(x_test.shape[0], total_input)
# print(x_test.shape)
# Now we are going to separate some data for validation purposes.
x_val = x_train[:10000]
y_val = y_train[:10000]
# print(x_val.shape)

x_train = x_train[10000:50000]
y_train = y_train[10000:50000]
print(x_train.shape)
# plt.show()
