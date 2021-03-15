import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('out.csv', sep=',', decimal='.')
df.plot('Дата', 'Курс')
plt.show()

