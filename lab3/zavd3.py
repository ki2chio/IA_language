import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('flats.csv', sep=',',index_col='Місто', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")
print(df.head())

fig, grph = plt.subplot()

grph.hist(df['Загальна_площа'])

grph.set_title('Загальна_площа')
grph.set_xlabel('Загальна_площа')
grph.set_ylabel('Частота')

plt.show()