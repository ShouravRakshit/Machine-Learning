from numpy.random import seed
from tensorflow import random
import keras
import os
import tensorflow as tf
import numpy as np
from IPython.display import display
from tensorflow.keras.preprocessing.image import array_to_img
import matplotlib.pyplot as plt

# We can get the data from a website called cs.toronto.edu
# However, we can get this dataset just by importing it from keras which is lot simpler.
from keras.datasets import cifar10
seed(887)
random.set_seed(404)

# print(type(cifar10.load_data()))
# Separating the train data from the test data.
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# pic = array_to_img(x_train[0])
# (display(pic))
# print((x_train, y_train))
plt.imshow(x_train[7])
plt.show()

