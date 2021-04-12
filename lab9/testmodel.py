import numpy as np
from keras.datasets import cifar10
# %tensorflow_version 2.x
import tensorflow as tf
print(tf.__version__)

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Convolution2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.utils import np_utils
from tensorflow.keras.models import model_from_json
import os

batch_size = 32
num_epochs = 15
kernel_size = 3
pool_size = 2
conv_depth_1 = 32
conv_depth_2 = 64
drop_prob_1 = 0.25
drop_prob_2 = 0.5
hidden_size = 512


(X_train, y_train), (X_test, y_test) = cifar10.load_data()

num_train, depth, height, width = X_train.shape
num_test = X_test.shape[0]

num_classes = np.unique(y_train).shape[0]

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= np.max(X_train)
X_test /= np.max(X_train)

Y_train = np_utils.to_categorical(y_train, num_classes)
Y_test = np_utils.to_categorical(y_test, num_classes)

inp = tf.keras.Input(shape=(depth, height, width))
conv_1 = Convolution2D(conv_depth_1, kernel_size, kernel_size, padding='same', activation='relu')(inp)
conv_2 = Convolution2D(conv_depth_1, kernel_size, strides=kernel_size, padding='same', activation='relu')(conv_1)

pool_1 = MaxPooling2D((pool_size, pool_size), padding='same')(conv_2)
drop_1 = Dropout(drop_prob_1)(pool_1)

conv_3 = Convolution2D(conv_depth_2, kernel_size, strides=kernel_size, padding='same', activation='relu')(drop_1)
conv_4 = Convolution2D(conv_depth_2, kernel_size, strides=kernel_size, padding='same', activation='relu')(conv_3)

pool_2 = MaxPooling2D((pool_size, pool_size), padding='same')(conv_4)
drop_2 = Dropout(drop_prob_1)(pool_2)

flat = Flatten()(drop_2)
hidden = Dense(hidden_size, activation='relu')(flat)
drop_3 = Dropout(drop_prob_2)(hidden)
out = Dense(num_classes, activation='softmax')(drop_3)
model = Model(inp, out) 

model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy']) 
model.fit(X_train, Y_train, batch_size=batch_size, epochs=num_epochs,verbose=1, validation_split=0.1)

model.evaluate(X_test, Y_test, verbose=1)

print('model will be saved')
model.save('test_img_model')
print('~~model saved~~')