import numpy as np
import pandas as pd

df = pd.read_csv('mlbootcamp5_train.csv', sep=';',index_col='id')
avg_height_gender_1=df[df.gender == 1][['height']].mean()
avg_height_gender_2=df[df.gender == 2][['height']].mean()

# print(avg_height_gender_1)
# print(avg_height_gender_2)
#Визначення статі гендера 1 та 2
if avg_height_gender_1.height>avg_height_gender_2.height:
	print('gender 1 its male, gender 2 its female')
else:
	print('gender 1 its female, gender 2 its male')
#Вживання алкоголю
avg_alcohol_gender_1 = df[df.gender == 1][['alco']].mean()
avg_alcohol_gender_2 = df[df.gender == 2][['alco']].mean()
if (avg_alcohol_gender_1.alco>avg_alcohol_gender_2.alco):
	print('female drink alcohol more often that male')
else:
	print('male drink alcohol more often that female')
#у скількі разів%курців більше серед чоловіків
avg_smoke_gender_1 = df[df.gender == 1][['smoke']].mean()
avg_smoke_gender_2 = df[df.gender == 2][['smoke']].mean()
print(str((avg_smoke_gender_2/avg_smoke_gender_1).smoke.round()) + ' times more')

#на скільки місяців (приблизно) відрізняються медіанне значення віку курців і тих хто не курить

avg_age_smoke_months = df[df.smoke == 1][['age']].mean() / 30
avg_age_no_smoke_months = df[df.smoke == 0][['age']].mean() / 30

print(str((avg_age_no_smoke_months - avg_age_smoke_months).age.round()) + ' months')

# female_smoke = df[df.gender==1][df.smoke==1].count()
# female_all = df[df.gender==1].count()
# print(female_smoke/female_all*100)

# male_smoke = df[df.gender==2][df.smoke==1].count()
# male_all = df[df.gender==2].count()
# print(male_smoke/male_all*100)

# print((male_smoke/male_all*100)/(female_smoke/female_all*100))



