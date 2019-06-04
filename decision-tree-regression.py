#Importing libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Position_Salaries.csv')

#Splitting into independent and dependent data
position = dataset.iloc[:, 1:2].values
salary=dataset.iloc[:, 2].values


#Fitting decision tree regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(position,salary)

#Predicting salary with decision tree regression
salaryPred = regressor.predict([[6.5]])

#Visualizing decision tree regression model
positionGrid = np.arange(min(position), max(salary), 0.1)
positionGrid = positionGrid.reshape((len(positionGrid),1))
plt.scatter(position,salary, color='green')
plt.plot(positionGrid,regressor.predict(positionGrid), color = 'red')
plt.title('Position & Salary Decision Tree Reg')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()
