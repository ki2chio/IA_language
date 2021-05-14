import cv2
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from matplotlib import pyplot as plt

cv2.__version__

pixels = cv2.imread('img/cars.jpg')

classifier = CascadeClassifier('haarcascade/haarcascade_plate_number.xml')
bboxes = classifier.detectMultiScale(pixels)
for box in bboxes:
	x, y, width, height = box
	x2, y2 = x + width, y + height
	# малюємо прямокутник
	cv2.rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
plt.imshow(pixels)
plt.show()