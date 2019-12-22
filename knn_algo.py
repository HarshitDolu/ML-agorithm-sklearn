# -*- coding: utf-8 -*-
"""Knn Algo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nY3HzVUQSbxT1botqICxTX2Wa2Lyi543
"""

from google.colab import drive
from google.colab import files
#drive.mount('/content/drive')
import pandas as pd
import numpy as np
import csv

data=pd.read_csv("/content/iris_dataset.csv")

data.head(5)

###splitting data sets ############
data.count()
train=data[:70]
test=data[70:]

def eudis(d1,d2,length):
  dis=0
  for x in range(length):
    dis=dis+m.pow((d1[x]-d2[x]),2)
    return m.sqrt(dis)

import operator
def neighbor(train,tinst,k):
  dis=[]
  p=len(tinst)
  for i in range (len(train)):
    di=eudis(train[i],tinst,p)
    dis.append((train[i],di))
  dis.sort(key=operator.itemgetter(1))
  nebors=[]
  for x in range(k):
    nebors.append(dis[x][0])
  return nebors

train.count()

trn=train.values.tolist()
tst=test.values.tolist()
tst[1]

import random
trn1=random.shuffle(trn)
neighbor

