import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('flats.csv', sep=',',index_col='Місто', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")
print(df.head())

fig, grph = plt.subplots() 

grph.scatter(df['Загальна_площа'], df['Ціна'])

grph.set_title('Графік залежності ціни від загальної площі')
grph.set_xlabel('Загальна_площа')
grph.set_ylabel('Ціна')
plt.show()