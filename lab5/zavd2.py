import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([6.5, 4.4, 3.8, 3.5, 3.1, 3.0])
y = np.array([-5, -4, 0.7, 1.25, 3, 5])

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print(p)

xp = np.linspace(-1, 6, 100)
plt.plot(x, y, '.', xp, p(xp))
plt.show()