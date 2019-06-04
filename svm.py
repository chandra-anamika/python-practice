#Importing libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Position_Salaries.csv')

#Splitting into independent and dependent data
position = dataset.iloc[:, 1:2].values
salary=dataset.iloc[:, 2].values

#Feature scaling
from sklearn.preprocessing import StandardScaler
scaledPosition = StandardScaler()
scaledSalary = StandardScaler()
position = scaledPosition.fit_transform(position)
#salary = scaledSalary.fit_transform(salary)
salary = np.squeeze(scaledSalary.fit_transform(salary.reshape(-1, 1)))

#Fitting SVM to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(position,salary)

#Predicting salary with SVM
salaryPred = scaledSalary.inverse_transform(regressor.predict(scaledPosition.transform([[6.5]])))

#Visualizing SVM model
plt.scatter(position,salary, color='green')
plt.plot(position,regressor.predict(position), color = 'blue')
plt.title('Position & Salary SVM Reg')
plt.xlabel('Position')
plt.ylabel('Salary')

