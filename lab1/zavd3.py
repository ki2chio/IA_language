# У двовимірному масиві зберігається інформація про заробітну плату 15
# осіб за кожен місяць року (першої особи у першому рядку, другої - у другому …).
# Написати програму, що обчислює сумарну зарплату, виплачену всім особам за
# заданий користувачем місяць.
import numpy as np 
nrows = 15
ncols = 12

arr = np.zeros(shape = (nrows, ncols))

for i in range(len(arr)):
	for j in range(len(arr[i])):
		arr[i][j] = np.random.randint(1,10)
		# print(arr[i][j])

print(arr)	
		
print('input month (1-12)')
input_ = int(input())-1

summ = 0

for k in range(nrows):
	summ+=arr[k][input_]
print("Summ",summ)