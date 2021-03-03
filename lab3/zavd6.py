import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('flats.csv', sep=',', decimal=',')
df["Загальна_площа"] = df.Загальна_площа.astype(float)

plot5 = sns.FacetGrid(df, col='Місто')
plot5 = plot5.map(sns.boxplot, 'Ціна')

plot6 = sns.FacetGrid(df, col='Кімнат')
plot6 = plot6.map(sns.boxplot, 'Ціна')


plt.show()