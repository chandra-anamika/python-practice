#Importing libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Position_Salaries.csv')

#Splitting into independent and dependent data
position = dataset.iloc[:, 1:2].values
salary=dataset.iloc[:, 2].values

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
linRegressor = LinearRegression()
linRegressor.fit(position,salary)

#Fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
polyRegressor = PolynomialFeatures(degree = 4)
position_poly = polyRegressor.fit_transform(position)
linPolyRegressor = LinearRegression()
linPolyRegressor.fit(position_poly,salary)

#Visualizing linear regression model
plt.scatter(position,salary, color='green')
plt.plot(position,linRegressor.predict(position), color = 'blue')
plt.title('Position & Salary Linear Reg')
plt.xlabel('Position')
plt.ylabel('Salary')

#Visualizing polynomial regression model
plt.scatter(position,salary, color='red')
plt.plot(position,linPolyRegressor.predict(polyRegressor.fit_transform(position)), color = 'blue')
plt.title('Position & Salary Polynomial Reg')
plt.xlabel('Position')
plt.ylabel('Salary')

#Predicting salary with linear regression
linRegressor.predict([[6.5]])

#Predicting salary with polynomial regression
linPolyRegressor.predict(polyRegressor.fit_transform([[6.5]]))