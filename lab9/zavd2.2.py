from keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("test_img_model")

img_path='dog.jfif'
img = image.load_img(img_path, target_size=(32, 32))
plt.imshow(img)
plt.show()

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

prediction = model.predict(x)
classes=['літак', 'автомобіль', 'птах', 'кіт', 'олень', 'собака', 'жаба', 'кінь', 'корабель', 'вантажівка']
print(classes[np.argmax(prediction)])