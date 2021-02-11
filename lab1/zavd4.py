import numpy as np
import scipy.linalg

a = [
	[1., -3., 4.],
	[-2., -1., 2.], 
	[-6., 7., -2.]]
b = [9., 5., 1.]

print(scipy.linalg.inv(a).dot(b))
print(scipy.linalg.solve(a,b))