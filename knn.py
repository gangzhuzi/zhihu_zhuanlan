# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:07:23 2018

@author: ZHUGANGGGANG
"""

import math
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#生成数据
np.random.seed(42)
df = pd.DataFrame(np.random.randn(30, 2),
                columns=['a', 'b'])
plt.scatter(df['a'],df['b'])

#打上标签，以经过直线 y=-2x-0.5 区分数据,记住loc、ilocde 用法
for i in range(30):
    temp = df.iloc[i]
    if 2*temp['a'] + temp['b'] + 0.5 <= 0 :
        df.loc[i,'label'] = 0
        plt.scatter(temp['a'],temp['b'],marker='o',c='green',s=40,hold=True)
    else:
        df.loc[i,'label'] = 1
        plt.scatter(temp['a'],temp['b'],marker='*',c='red',s=40,hold=True)

#knn的算法

def KNN(k,point):
    topk = list()    
    for i in range(30):
        dist = math.sqrt((point[0]-df.iloc[i]['a'])**2+(point[1]-df.iloc[i]['b'])**2)
        topk.append((df.iloc[i],dist))
        topk.sort(key=operator.itemgetter(1))
           
    for i in range(k):
        sum = 0
        sum = sum +topk[i][0][2]
    if sum < k/2:
        return point.append(0)
    else:
        return point.append(1) 
  
def test():
    point = [-1,1]   
    print point
    KNN(3,point)
    print point

    