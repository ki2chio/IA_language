import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB

df = pd.read_csv('zavd2.csv', sep=',',index_col='day')
print (df['outlook'].value_counts())
print (df['humidity'].value_counts())
print (df['wind'].value_counts())

le = preprocessing.LabelEncoder()
outlook_encoded = le.fit_transform(df['outlook'])
humidity_encoded = le.fit_transform(df['humidity'])
wind_encoded = le.fit_transform(df['wind'])
label=le.fit_transform(df['play'])
print ("outlook",outlook_encoded)
print ("humidity:",humidity_encoded)
print ("wind:",wind_encoded)
print ("play:",label)

features = list(zip(outlook_encoded,humidity_encoded,wind_encoded))
print (features)

model = BernoulliNB()
model.fit(features,label)
predicted = model.predict([[2,1,0]]) #Outlook = Sunny 2, Humidity = Normal 1, Wind = Strong 0
print ("Predicted Value:","yes" if predicted else "no" )