# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:18:35 2015

@author: shehzadbashir
"""

import pandas as pd

# Read Yelp.csv into a DataFrame
yelp = pd.read_csv('yelp.csv')
data = pd.DataFrame(yelp)

# Create a new DataFrame that only contains the 5-star and 1-star reviews.
data2 = data[(data.stars==5) | (data.stars==1)]

# Split the new DataFrame into training and testing sets, 
# using the review text as the feature and the star rating as the response.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data2.text, data2.stars, random_state=1)

# Use CountVectorizer to create document-term matrices from X_train and X_test.
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)

# Use Naive Bayes to predict the star rating for reviews in the testing set, 
# and calculate the accuracy.
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(train_dtm, y_train)

y_pred_class = nb.predict(test_dtm)

from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class)

#Calculate the AUC 
 ## Not complete- need to assign probability 
y_pred_prob = nb.predict_proba(test_dtm)[:, 1]
metrics.roc_auc_score(y_test, y_pred_prob)

# Plot the ROC curve.

# Print the confusion matrix, and calculate the sensitivity and specificity
metrics.confusion_matrix(y_test, y_pred_class)
# Sensitivity =  813 / (813+25)
# Specificity = 126 / (126+58)

#Browse through the review text for some of the false positives and false negatives. 
#Based on your knowledge of how Naive Bayes works, do you have any theories 
# about why the model is incorrectly classifying these reviews?

X_test[y_test < y_pred_class] # show false positives
X_test[y_test > y_pred_class] # show false negatives
## Could not come to a solid conclusion but my guess is that it the reviews may have some
## trigger words that may have misclassified the review into a different bucket. 


# Let's pretend that you want to balance sensitivity and specificity. 
# You can achieve this by changing the threshold for predicting a 5-star review. 
# What threshold approximately balances sensitivity and specificity?




##Bonus: Turn this into a 5-class classification problem by predicting the 
#star rating using the original DataFrame (from step 1). 
# Calculate the accuracy and print the confusion matrix. Comment on the results.