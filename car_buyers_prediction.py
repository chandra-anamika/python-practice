#Importing libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Startups-data.csv')

#Splitting into independent and dependent data
spend = dataset.iloc[:, :-1].values
profit=dataset.iloc[:, 4].values

#Encode categorical variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
spend_encoder= LabelEncoder()
spend[:,3] = spend_encoder.fit_transform(spend[:,3])
onehotencoder = OneHotEncoder(categorical_features= [3])
spend = onehotencoder.fit_transform(spend).toarray()

#Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
spend_train, spend_test, profit_train, profit_test = train_test_split(spend,profit, test_size = 0.2, random_state=0)

#Fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(spend_train,profit_train)

#Predicting the test set results
profit_pred =regressor.predict(spend_test)

#Building optimal model using backward elimination
import statsmodels.formula.api as sm
spend=np.append(arr = np.ones((50,1)).astype(int), values= spend, axis = 1)
spend_optimal = spend[:,[0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = profit, exog = spend_optimal).fit()
regressor_ols.summary()
spend_optimal = spend[:,[0,1,2,3,4]]
regressor_ols = sm.OLS(endog = profit, exog = spend_optimal).fit()
regressor_ols.summary()

