import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('flats.csv', sep=',',index_col='Місто', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")
print(df.head())

fig, grph = plt.subplot()

grph.hist(df['Кімнат'])

grph.set_title('Кімнат')
grph.set_xlabel('Кімнат')
grph.set_ylabel('Кількість')

plt.show()