import pandas as pd
# Read in the csv file
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
votes = pd.read_csv("114_congress.csv")


kmeans_model = KMeans(n_clusters=2, random_state=1).fit(votes.iloc[:, 3:])

votes["labels"] = kmeans_model.labels_
democratic_oddballs = votes[(votes["labels"] == 1) & (votes["party"] == "D")]

pca_2 = PCA(2)

# Turn the vote data into two columns with PCA
plot_columns = pca_2.fit_transform(votes.iloc[:,3:18])

# Plot senators based on the two dimensions, and shade by cluster label
# You can see the plot by clicking "plots" to the bottom right
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=votes["labels"])
plt.show()