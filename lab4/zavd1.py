import numpy as np
import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
import seaborn as sns
# ігноруємо warnings
import warnings
warnings.filterwarnings("ignore")
sns.set_context("notebook", font_scale = 1.5, rc = {"figure.figsize" : (12, 9), "axes.titlesize" : 18})
df=pd.read_csv('http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/data/mlbootcamp5_train.csv', sep=';', index_col='id')

df_uniques = pd.melt(frame=df, value_vars=['gender','cholesterol','gluc', 'smoke', 'alco','active', 'cardio'])
df_uniques = pd.DataFrame(df_uniques.groupby(['variable','value'])['value'].count()).sort_index(level=[0, 1]).rename(columns={'value': 'count'}).reset_index()
sns.factorplot(x='variable', y='count', hue='value', data=df_uniques, kind='bar', size=12)

df_uniques = pd.melt(frame=df, value_vars=['gender','cholesterol','gluc','smoke', 'alco','active'],id_vars=['cardio'])
df_uniques = pd.DataFrame(df_uniques.groupby(['variable', 'value','cardio'])['value'].count()).sort_index(level=[0, 1]).rename(columns={'value': 'count'}).reset_index()
sns.factorplot(x='variable', y='count', hue='value', col='cardio', data=df_uniques, kind='bar', size=9)

for c in df.columns:
	n = df[c].nunique()
	print(c)
	if n <= 3:
		print(n, sorted(df[c].value_counts().to_dict().items()))
	else:
		print(n)
print(10 * '-')

plt.show()