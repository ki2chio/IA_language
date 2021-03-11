import numpy as np
import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
import seaborn as sns
# ігноруємо warnings
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')

sns.jointplot(df['ap_hi'], df['ap_lo'], size=10, marker='.', marginal_kws=dict(bins=100, rug=False, hist_kws={'log': True}))
data_filtered = df[(df['ap_hi'] > 0) & (df['ap_lo'] > 0)][['ap_lo', 'ap_hi']].apply(np.log1p)
data_filtered.describe()

g = sns.jointplot(data_filtered['ap_hi'], data_filtered['ap_lo'], size=10,  marginal_kws=dict(bins=100, rug=False,hist_kws={'log': True}),marker='.')
g.ax_joint.grid(True)
g.ax_joint.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(round(int(np.exp(x))))))
g.ax_joint.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(round(int(np.exp(x))))))

plt.show()

#Скільки чітко виражених кластерів вийшло на спільному
#графіку обраних ознак, за логарифмічною шкалою? Під кластером іноді
#розуміють щільне скупчення точок, в околиці яких досить мало
#одиночних і які візуально відділені від інших кластерів
#7