import numpy as np
import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
import seaborn as sns
# ігноруємо warnings
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')
#Побудуйте кореляційну матрицю (heatmap). Матриця формуєтьсязасобами Pandas, зі стандартним значенням параметрів.
sns.heatmap(df.corr())
#Проведіть візуалізацію даних: зріст і стать (violinplot)
sns.violinplot(hue="gender",x='gender', y='height', data=df)
#Побудуйте на одному графіку два окремих kdeplot росту і вагі, окремо для чоловіків і жінок
sns.kdeplot(df[df.gender == 1]['height'],color = "blue", shade = True)
sns.kdeplot(df[df.gender == 1]['weight'],color = "blue")

sns.kdeplot(df[df.gender == 2]['height'],color = "orange", shade = True) 
sns.kdeplot(df[df.gender == 2]['weight'],color = "orange")
plt.show() 

