import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

import keras 
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

np.random.seed(42)
(х_train, y_train), (x_test, y_test) = mnist.load_data()
х_train = х_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
х_train = х_train.astype('float32')
x_test = x_test.astype('float32')
х_train /= 255
x_test /= 255
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
model = Sequential()

model.add(Dense(800, input_dim=784, activation="relu", kernel_initializer="normal"))


model.add(Flatten())

model.add(Dense(units = 120, activation = 'relu'))

model.add(Dense(units = 84, activation = 'relu'))

model.add(Dense(units = 10, activation="softmax", kernel_initializer="normal"))

model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

model.fit(х_train, y_train, batch_size=200, epochs=100, validation_split=0.2, verbose=2)

scores = model.evaluate(x_test, y_test, verbose=0)
print("Точність роботи на тестових даних: %.2f%%" % (scores[1]*100))