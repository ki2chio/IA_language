import numpy as np
import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
import seaborn as sns
# ігноруємо warnings
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')
#Побудуйте кореляційну матрицю, використовуючи коефіцієнт Спірмена
sns.heatmap(df.corr(method='spearman'))
plt.show()
#Які ознаки тепер найбільше корелюють одна з одною за Спірменом
#ap_lo ap_hi

#Чому значення рангової кореляції у цих ознаках таке велике
#Тому що це наближені величини які показують мінімальний та максимальний тиск

