#Import Library of Gaussian Naive Bayes model
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

#assigning predictor and target variables
dataset = datasets.load_iris()

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets 
model.fit(dataset.data, dataset.target)

#Predict Output 
expected = dataset.target
predicted = model.predict(dataset.data)

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))