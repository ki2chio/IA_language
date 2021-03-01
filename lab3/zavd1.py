import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)


df = pd.read_csv('flats.csv', sep=',',index_col='Місто', decimal=',')
df['Загальна_площа'] = df['Загальна_площа'].astype("float64")
city_groups = df.groupby("Місто")
print('-----------------------------------------------\nCкільки квартир продається у кожному місті\n')
print(city_groups.size().sort_values(ascending=False))

df_zavd2=df.drop(index='Києво-Святошинський')
df_3kimnat=df_zavd2[df_zavd2.Кімнат == 3].groupby("Місто")
print('-----------------------------------------------\n3 Кімнатні квартири\n')
print(df_3kimnat.size().sort_values(ascending=False))

print('-----------------------------------------------\nПлоща\n')
print(city_groups['Загальна_площа'].mean())

df_2kimnat=df[df.Кімнат == 2]
df_2kimnat=df_2kimnat[df_2kimnat.Загальна_площа > 60]
print('-----------------------------------------------\nКількість двокімнатних квартир загальною площею більше 60 м.кв\n')
print(df_2kimnat.count())

print('-----------------------------------------------\nсереднє значення площі\n')
print(df['Загальна_площа'].mean())
print('-----------------------------------------------\nсередньоквадратичне відхилення\n')
print(df['Загальна_площа'].std())
print('-----------------------------------------------')