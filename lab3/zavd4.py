import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('flats.csv', sep=',',index_col='Місто', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")
print(df.head())

fig, grph = plt.subplots() 

data = df['Загальна_площа'].value_counts() 
points = data.index 
frequency = data.values 

grph.bar(points, frequency) 
grph.set_title('Загальна площа') 
grph.set_xlabel('Площа') 
grph.set_ylabel('Частота')

plt.show()