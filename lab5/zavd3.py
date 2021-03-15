import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
df = pd.read_csv('Advertising.txt', sep=",",index_col=' ')
print('*'*40)
print(df.head())
print('*'*40)
print(df.info())

lm = smf.ols(formula='Sales~TV', data=df).fit()
print('*'*40)
print(lm.params)

X_new = pd.DataFrame({'TV': [50]})
print('*'*40)
print(X_new.head())
print('*'*40)
print(lm.predict(X_new))



sns.pairplot(df, kind="kde")

fig, axs = plt.subplots(1, 3, sharey=True)
df.plot(kind='scatter', x='TV', y='Sales', ax=axs[0], figsize=(16, 8))
df.plot(kind='scatter', x='Radio', y='Sales', color='red', ax=axs[1])
df.plot(kind='scatter', x='Newspaper', y='Sales', color='green', ax=axs[2])

plt.show()