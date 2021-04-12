import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2
model = tf.keras.models.load_model("saved.model")

def img_load(img_path):
	img_temp = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
	plt.imshow(img_temp)
	plt.show()
	img_temp = img_temp.reshape(1, 784)
	img_temp = img_temp.astype('float32')
	img_temp = img_temp/255
	prediction=model.predict(img_temp)
	print(prediction)
	classes=['1','2','3','4','5','6','7','8','9','0']
	print(classes[np.argmax(prediction)])

image = ['4.jpg','5.jpg','7.jpg']

for img in image:
	img_load(img)