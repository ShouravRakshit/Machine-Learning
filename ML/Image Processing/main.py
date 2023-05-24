import numpy as np
import tensorflow as tf
from keras.utils import load_img, img_to_array
from keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input
from keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import preprocess_input as preprocess_input_vgg19
from keras.applications.vgg19 import decode_predictions as decode_vgg19
from keras.preprocessing import image
from keras.applications.nasnet import NASNetLarge, preprocess_input
from keras.models import Model

def format_img_inceptionresnet(file_name):
    pic = load_img(file_name, target_size=(299, 299))
    # (display(pic))
    pic_array = img_to_array(pic)
    # print(pic_array.shape)
    expanded = np.expand_dims(pic_array, axis=0)
    print(expanded.shape)
    preprocessed = preprocess_input(expanded)
    inception_model = InceptionResNetV2(weights='imagenet')
    inception_model.graph = tf.compat.v1.get_default_graph()

    prediction = inception_model.predict(preprocessed)
    print(decode_predictions(prediction))


def format_vgg19_model(file_name):
    pic = load_img(file_name, target_size=(224, 224))
    # (display(pic))
    pic_array = img_to_array(pic)
    # print(pic_array.shape)
    expanded = np.expand_dims(pic_array, axis=0)
    print(expanded.shape)
    preprocessed = preprocess_input_vgg19(expanded)
    vgg19_model = VGG19()
    prediction = vgg19_model.predict(preprocessed)
    print(decode_vgg19(prediction))


def nasnet_large_model(file_name):
    # Load NasNetLarge model

    base_model = NASNetLarge(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('global_average_pooling2d_1').output)

    # Load and preprocess the image
    img_path = file_name
    img = image.load_img(img_path, target_size=(331, 331))  # NasNetLarge input size is (331, 331)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Extract features using the NasNetLarge model
    features = model.predict(x)

    return features


file_1 = 'C:/Work/Machine-Learning/ML/Image Processing/TF_Keras_Classification_Images/01 Umbrella.jpg'
file_2 = 'C:/Work/Machine-Learning/ML/Image Processing/TF_Keras_Classification_Images/02 Couple.jpg'
file_3 = 'C:/Work/Machine-Learning/ML/Image Processing/TF_Keras_Classification_Images/03 Ocean.jpg'

format_img_inceptionresnet(file_1)
format_vgg19_model(file_1)
features = nasnet_large_model(file_1)
print(features)
