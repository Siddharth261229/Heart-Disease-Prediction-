# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:00:04 2024

@author: hp
"""

import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
import statsmodels.api as sm
from sklearn import preprocessing 
'exec(% matplotlib inline)'
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns

#dataset
disease_df = pd.read_csv("C:/Users/hp/Downloads/framingham.csv")
disease_df.drop(['education'], inplace=True, axis=1)
disease_df.rename(columns = {'male': 'Sex_male'},
                  inplace = True)

# handling missing values
disease_df.dropna(axis=0, inplace=True)
print(disease_df.head() ,disease_df.shape)
print(disease_df.TenYearCHD.value_counts())

#Splitting the datasets into train and test

x = np.asarray(disease_df[['age', 'Sex_male', 'cigsPerDay', 
                           'totChol', 'sysBP', 'glucose']])
y = np.asarray(disease_df['TenYearCHD'])

# normalization of the dataset
x = preprocessing.StandardScaler().fit(x).transform(x)

# Train and Test Split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test  = train_test_split(x,y, test_size=0.3 , random_state=4)

print('Train set:', x_train.shape, y_train.shape)
print('Test Set:' , x_test.shape ,y_test.shape)

# counting no. of patients affected with CHD
plt.figure(figsize=(7,5))
sns.countplot(x='TenYearCHD', data=disease_df, palette='BuGn_r')
plt.show()

laste = disease_df['TenYearCHD'].plot()
plt.show(laste)

# Fitting Logistic Regression Model for Heart Disease Predicton
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
y_pred = logreg.predict(x_test)

# Evaluating Logistic Regression Model
from sklearn.metrics import accuracy_score
print('Accuracy of the model is=',
      accuracy_score(y_test, y_pred))

# Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report

cm=confusion_matrix(y_test, y_pred)
conf_matrix = pd.DataFrame(data =cm, columns=['Predicted:0', 'Predicted:1'], index =['Actual:0', 'Actual:1'])

plt.figure(figsize =(8,5))
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = "Greens")

plt.show()
print('The details for confusion matrix is =')
print (classification_report(y_test, y_pred))