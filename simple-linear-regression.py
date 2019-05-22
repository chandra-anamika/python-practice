#Importing libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Salary_Data.csv')

#Splitting into independent and dependent data
yoe = dataset.iloc[:, :-1].values
salary= dataset.iloc[:, 1].values

#Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
yoe_train, yoe_test, salary_train, salary_test = train_test_split(yoe,salary, test_size = 1/3, random_state=0)

#Fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(yoe_train,salary_train)

#Predicting the test set results
salary_pred =regressor.predict(yoe_test)

#Visualizing the training set results
plt.scatter(yoe_train, salary_train, color='blue')
plt.plot(yoe_train,regressor.predict(yoe_train), color='green')
plt.title('Salary & Experience plot')
plt.xlabel('Year of Experience (Yrs)')
plt.ylabel('Salary ($)')
plt.show()