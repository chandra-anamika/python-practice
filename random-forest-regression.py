#Importing libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Position_Salaries.csv')

#Splitting into independent and dependent data
position = dataset.iloc[:, 1:2].values
salary=dataset.iloc[:, 2].values

#Fitting random forest regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(position, salary)

#Predicting salary with random forest regression
salaryPred = regressor.predict([[6.5]])

#Visualizing random regression model
positionGrid = np.arange(min(position), max(salary), 0.01)
positionGrid = positionGrid.reshape((len(positionGrid),1))
plt.scatter(position,salary, color='green')
plt.plot(positionGrid,regressor.predict(positionGrid), color = 'red')
plt.title('Position & Salary Random Forest Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()
