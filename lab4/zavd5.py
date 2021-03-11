import numpy as np
import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
import seaborn as sns
# ігноруємо warnings
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')

df['age_years'] = (df['age'] // 365.25).astype(int)

ax = sns.countplot(x="age_years", hue="cardio", data=df)

plt.show()

#В якому віці кількість пацієнтів з ССЗ вперше стає більше,ніж здорових?
#В 53 роки 