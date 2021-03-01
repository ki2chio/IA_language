import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('flats.csv', sep=',',index_col='Місто', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")

fig, ax = plt.subplot()

ax.hist(df['Ціна'])

ax.set_title('Ціна')
ax.set_xlabel('Ціна')
ax.set_ylabel('Кількість')

plt.show()