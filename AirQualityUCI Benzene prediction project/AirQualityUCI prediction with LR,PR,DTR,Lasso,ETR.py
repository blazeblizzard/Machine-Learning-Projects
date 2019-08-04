# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:26:12 2019

@author: pawan
"""

"""Air QualityUCI data"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#importing and visualizing data
air_data = pd.read_excel('AirQualityUCI.xlsx')

air_data.head()
air_data.shape

#dropping ueless information from the data

air_data.dropna(axis=0, how='all')

features=air_data
features = features.drop('Date', axis=1)
features = features.drop('Time', axis=1)
features = features.drop('C6H6(GT)', axis=1)
features = features.drop('PT08.S4(NO2)', axis=1)
features

labels = air_data['C6H6(GT)']
#features=features.values

#training and testing 

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(features,labels,test_size=.2)


#applying differebt regression models

#1. Linear

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred=regressor.predict(X_test)


#2. Polynomial 

from sklearn.preprocessing import PolynomialFeatures
Poly=PolynomialFeatures(degree=4)
X_train_poly=Poly.fit_transform(X_train)
X_test_poly=Poly.fit_transform(X_test)
regressor.fit(X_train_poly,Y_train)
Y_pred_poly=regressor.predict(X_test_poly)

#3. Support Vector Regression

     #feature scaling
     
from sklearn.preprocessing import StandardScaler
X_sc=StandardScaler()
Y_sc=StandardScaler()
Y_train=Y_train.values.reshape(-1,1) #<did this to resshape 1D to 2D>
X_train_sc=X_sc.fit_transform(X_train)
Y_train_sc=Y_sc.fit_transform(Y_train)
#Y_test=Y_test.values.reshape(-1,1)
X_test_sc=X_sc.fit_transform(X_test)
Y_test_sc=Y_sc.fit_transform(Y_test)

   #building the svr
from sklearn.svm import SVR
svmregressor=SVR(kernel='rbf',C=1000)
svmregressor.fit(X_train_sc,Y_train_sc)

Y_pred_svr=svmregressor.predict(X_test_sc)

Y_pred_svr=Y_sc.inverse_transform(Y_pred_svr)


#4. Decision tree regression

from sklearn.tree import DecisionTreeRegressor

DT=DecisionTreeRegressor()
DT.fit(X_train,Y_train)
  #feature importances in DTR
print(DT.feature_importances_)
featureimpDT=np.argsort(DT.feature_importances_)[::-1]
Y_pred_DT=DT.predict(X_test)


#5. Lasso Regression

from sklearn.linear_model import Lasso

classifier=Lasso(alpha=1)
classifier.fit(X_train,Y_train)

Y_pred_L=classifier.predict(X_test)

#6. ExtraTreeRegressor

from sklearn.ensemble import ExtraTreesRegressor
etr=ExtraTreesRegressor(n_estimators=300)
etr.fit(X_train,Y_train)

#Feature Importances on ETR
print(etr.feature_importances_)
indecis = np.argsort(etr.feature_importances_)[::-1]
plt.figure(num=None, figsize=(14, 10), dpi=80, facecolor='w')
plt.title("Feature importances")
plt.bar(range(X_train.shape[1]), etr.feature_importances_[indecis],
       color="r", align="center")
plt.xticks(range(X_train.shape[1]), indecis)
plt.show()
