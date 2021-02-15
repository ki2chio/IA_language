import numpy as np
import pandas as pd

df = pd.read_csv('mlbootcamp5_train.csv', sep=';',index_col='id')
df['imb'] = df['weight'] / ((df['height']/100 * df['height']/100)) 
if df[df.cardio == 0]['imb'].mean() > df[df.cardio == 1]['imb'].mean() :
	print('true')
else:
	print('false')
print(df[df.cardio == 0]['imb'].mean())
print(df[df.cardio == 1]['imb'].mean())