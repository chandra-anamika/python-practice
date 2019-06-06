#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as plt2 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Social_Network_Ads.csv')

#Splitting into independent and dependent data
personal_details = dataset.iloc[:, [2,3]].values
purchase=dataset.iloc[:, 4].values

#Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
personal_details_train, personal_details_test, purchase_train, purchase_test = train_test_split(personal_details, purchase, test_size = 0.25, random_state = 0)

#Feature scaling
from sklearn.preprocessing import StandardScaler
personalDetails_scaled= StandardScaler()
personal_details_train = personalDetails_scaled.fit_transform(personal_details_train)
personal_details_test = personalDetails_scaled.transform(personal_details_test)

#Fitting classifier to the training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2,)
classifier.fit(personal_details_train,purchase_train)

#Predicting the test set results
purchase_pred = classifier.predict(personal_details_test)

#Making confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(purchase_test,purchase_pred)

#Visualising training set results
personal_details_set, purchase_set = personal_details_train, purchase_train
personal_details_plot, personal_details_plot2 = np.meshgrid(np.arange(start = personal_details_set[:,0].min()-1, stop = personal_details_set[:,0].max()+1, step = 0.01),
                                                            np.arange(start = personal_details_set[:,0].min()-1, stop = personal_details_set[:,0].max()+1, step = 0.01))
plt.contourf(personal_details_plot, personal_details_plot2, classifier.predict(np.array([personal_details_plot.ravel(),personal_details_plot2.ravel()]).T).reshape(personal_details_plot.shape), alpha = 0.75, cmap = plt2.colors.ListedColormap(('red','green')))
plt.xlim(personal_details_plot.min(), personal_details_plot.max())
plt.ylim(personal_details_plot2.min(), personal_details_plot2.max())
for i,j in enumerate(np.unique(purchase_set)):
    plt.scatter(personal_details_set[purchase_set == j, 0], personal_details_set[purchase_set == j, 1], c = plt2.colors.ListedColormap(('red','green'))(i), label = j)
plt.title('Purchase of Car kNN')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
