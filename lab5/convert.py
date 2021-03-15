import numpy as np
import pandas as pd

df = pd.read_csv('UAG-USD.csv', sep=',',index_col='Дата', decimal='.')

df['Курс'] = df['Офіційний курс гривні, грн']/df['Кількість одиниць']
df = df.drop(['Офіційний курс гривні, грн'], axis=1)
df = df.drop(['Кількість одиниць'], axis=1)
df.to_csv('out.csv')