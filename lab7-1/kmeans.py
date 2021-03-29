import csv
import numpy as np
import pandas as pd


import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN, KMeans
import sklearn.utils




#df=pd.read_csv('http://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/data/mlbootcamp5_train.csv', sep=';', index_col='id')
df=pd.read_csv('Advertising.txt')
df.head()

# Create KMeans object
kmeans = KMeans(n_clusters=4)

# Train
kmeans.fit(df)

# Get output
labels = kmeans.labels_

# Add labels to dataframe
df['KMeans_LT_Clusters'] = labels

# View sample of clusters
#df[['height','weight','cholesterol',"KMeans_LT_Clusters"]].head()
df[["TV","Radio","Newspaper","KMeans_LT_Clusters"]].head(100)



kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(df)

plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c = labels, marker = '*', s=500)

plt.scatter( kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],c='r',s=900)
plt.show()