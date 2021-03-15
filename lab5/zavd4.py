import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv('Advertising.txt', sep=",",index_col=' ')
#Побудуйте лінію регресії для продажів в залежності від реклами на
#TV, Radio і Newspaper за допомогою функції (sns.pairplot()), і 95%
#довірчий інтервал для цієї регресії: y ~ x
sns.lmplot('TV', 'Sales', data=df,line_kws={'lw': 2, 'color': 'red'})
sns.lmplot('Radio', 'Sales', data=df,line_kws={'lw': 2, 'color': 'red'})
sns.lmplot('Newspaper', 'Sales', data=df,line_kws={'lw': 2, 'color': 'red'})

#Побудувати коробчасті діаграми для даних TV, Radio і Newspaper
fig, axs = plt.subplots(1, 3, sharey=True)
sns.boxplot(y="TV",data=df,ax=axs[0])
sns.boxplot(y="Radio",data=df,ax=axs[1])
sns.boxplot(y="Newspaper",data=df,ax=axs[2])
plt.show()

#Розрахувати оцінки модельних коефіцієнтів для рекламних в газетах і на радіо.
lm_radio = smf.ols(formula='Sales~Radio', data=df).fit()
print(lm_radio.params)

lm_newspaper = smf.ols(formula='Sales~Newspaper', data=df).fit()
print(lm_newspaper.params)

# Зробити прогноз:
# o Якщо на рекламу на радіо буде потрачено $ 50,000
# o Якщо на рекламу в газеті буде потрачено $ 50,000
X_new_radio = pd.DataFrame({'Radio': [50]})
print(X_new_radio.head())
print(lm_radio.predict(X_new_radio))

X_new_newspaper = pd.DataFrame({'Newspaper': [50]})
print(X_new_newspaper.head())
print(lm_newspaper.predict(X_new_newspaper))

# З графіків, що були побудовані, вже можна зробити декілька цікавих
# висновків за даними, щодо того, як впливає реклама в газетах, на радіо і ТV
# на продажи: найменше на продажі впливає реклама в газетах, потім реклама
# на радіо і найбільше - реклама на ТV