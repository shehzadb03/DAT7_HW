# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:17:06 2015

@author: shehzadbashir
"""

import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

import seaborn as sns

# Read yelp.csv into DataFrame

data = pd.read_table('yelp.csv', sep=',')
data.head(5)

#JSON to CSV

with open('yelp.json', 'rU') as f:
    data = [json.loads(row) for row in f]

yelp = pd.DataFrame(data)

yelp.head()

yelp['cool']=[row['votes']['cool'] for row in data]
yelp['useful']=[row['votes']['useful'] for row in data]
yelp['funny']=[row['votes']['funny'] for row in data]

yelp.head()

yelp.to_csv('hw_results.csv', index=False)
    

# Explore the relationship between each of the vote types (cool/useful/funny) and the number of stars.

data.corr()
sns.heatmap(data.corr())
sns.pairplot(data, x_vars=['cool', 'useful', 'funny'], y_vars='stars', size=6, aspect=.7, kind='reg')
#Scatterplot

#Define cool/useful/funny as the features, and stars as the response.

feature_cols = ['cool', 'useful', 'funny']
X = data[feature_cols]
y = data.stars

#Fit a linear regression model and interpret the coefficients. Do the coefficients make intuitive sense to you? Explore the Yelp website to see if you detect similar trends.

        # instantiate and fit
linreg = LinearRegression()
linreg.fit(X, y)

        # print the coefficients
linreg.intercept_
linreg.coef_

zip(feature_cols, linreg.coef_)

   # An additional cool vote would mean .27 increase in star rating 
   # An additional useful vote would mean a decrease of .147 in star rating
   # An additional funny vote would mean a decrese of .136 in star rating

# Evaluate the model by splitting it into training and testing sets and computing the RMSE. Does the RMSE make intuitive sense to you?

def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

feature_cols = ['cool', 'useful', 'funny']
X = data[feature_cols]
train_test_rmse(X, y)

# Try removing some of the features and see if the RMSE improves.

feature_cols = ['cool', 'useful']
X = data[feature_cols]
train_test_rmse(X, y)

#Bonus: Think of some new features you could create from the existing data that might be predictive of the response. 
#(This is called "feature engineering".) 
#Figure out how to create those features in Pandas, add them to your model, and see if the RMSE improves.
data.head(5)
   # Text Analysis? 
text_list=[1 if len(row) < 100 else 0 for row in data.text]

len(data.text)
len(text_list)

text_list

data['text_list'] = text_list

text_length=[len(row) for row in data.text]

text_length

data['text_length'] = [len(row) for row in data.text]
data.head()

feature_cols = ['cool', 'useful', 'funny', 'text_length', 'text_list']
X = data[feature_cols]
train_test_rmse(X, y)

zip(feature_cols, linreg.coef_)


# Bonus: Compare your best RMSE on testing set with the RMSE for the "null model", 
# which is the model that ignores all features and simply predicts the mean rating 
# in the training set for all observations in the testing set


# Bonus: Instead of treating this as a regression problem, treat it as a 
# classification problem and see what testing accuracy you can achieve with KNN.


# Bonus: Figure out how to use linear regression for classification, 
# and compare its classification accuracy to KNN.






