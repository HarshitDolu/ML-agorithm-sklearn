# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cgxa6UXOeEWtondH10LzmAJxR9TDfzvr
"""

########################################################IRIS  DATASET ###############################
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
############################### USING SKLEARN Loading dataset
iris=datasets.load_iris()
####################################### features and labels
x=iris.data
y=iris.target

import numpy as np
x=iris["data"][:,3:]
y=(iris["target"]==2).astype(np.int)
clf=LogisticRegression()
clf.fit(x,y)
#import sklearn.model_selection as model_selection
#xtrain,xtest,ytrain,ytest=model_selection.train_test_split(x,y,test_size=0.2,random_state=4)
ex=clf.predict([[2.6]])
print(ex)
pred=clf.predict(x)
print(len(pred))

x_new=np.linspace(0,3,150).reshape(-1,1)
#print(x_new[:,0])
#y_prob=clf.predict_proba(x_new)
y_actual=clf.predict(x_new)
print(y_actual)
#print(y_prob[:,1])

import matplotlib.pyplot as plt
plt.plot(x_new,y_prob[:,1],"g-",Label="virginica")
plt.show()

#print(y_prob[:,1])
from sklearn.metrics import classification_report
print(classification_report(y_actual,pred))

