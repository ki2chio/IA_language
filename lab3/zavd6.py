import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('flats.csv', sep=',', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")
df['Ціна'] = df['Ціна'].astype("int64")

fig, grph = plt.subplots() 
df_box = df[(df['Кімнат']) & (df['Ціна'])]
sns.boxplot('Кімнат', 'Ціна', data = df_box)

plt.show().barh()