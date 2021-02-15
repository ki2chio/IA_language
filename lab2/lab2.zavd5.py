import numpy as np
import pandas as pd

df = pd.read_csv('mlbootcamp5_train.csv', sep=';',index_col='id')
df['age_years'] = ((df[['age']] / 365).round()).astype("int64")
old_male = df[df.gender == 2][df.age_years >= 60][df.age_years <= 64]

old_smok_male = old_male [ old_male.smoke == 1 ]

old_smok_male_low_ap = old_smok_male [old_smok_male.ap_hi < 120 ] [ old_smok_male.cholesterol == 1 ]

old_smok_male_high_ap = old_smok_male [old_smok_male.ap_hi >= 160 ] [old_smok_male.ap_hi < 180 ] [ old_smok_male.cholesterol == 3 ]
print(((old_smok_male_high_ap[old_smok_male_high_ap.cardio == 1].count() / 
	old_smok_male_high_ap.count()) / (old_smok_male_low_ap[old_smok_male_low_ap.cardio == 1].count() / old_smok_male_low_ap.count())).round())

