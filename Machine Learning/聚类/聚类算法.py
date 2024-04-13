import pandas as pd
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math
# 载入数据
path = '/Users/zhong/Desktop/logistic_regression.pkl'
data = np.load(path,allow_pickle=True)
# 定义数据 前两列分别为参数1，参数2，第三列为结果（0/1）
data = pd.DataFrame(data,columns=["parameter1","parameter2","result"])
x = np.array(data.iloc[:,0:2])
x = np.insert(x,0,0,axis = 1)
def myKmeans(x,k):
    center = np.array([[1, 1], [3, 3]])
    changed = True
    c_sum = 0
    while changed:
        changed = False
        for i in range(len(x)):
            minindex = 0
            mindistance = ((x[i,1:] - center[0])**2).sum()
            for j in range(k):
                if mindistance > ((x[i,1:] - center[j])**2).sum():
                    minindex = j
            if x[i,0] != minindex:
                x[i,0] = minindex
                changed = True
        for c in range(k):
            group = x[nonzero(x[:,0] == c)][:,1:]
            center[c] = group.mean(0)
        c_sum += 1
    return x,center,c_sum
k = 2
X,center,c_sum = myKmeans(x,k)
print(f"迭代{c_sum}次后收敛")
positive = X[nonzero(X[:,0] == 1)][:,1:]
negative = X[nonzero(X[:,0] == 0)][:,1:]
plt.figure(figsize = (12,8))
plt.scatter(positive[:,0],positive[:,1],c = 'r',marker = 'x',label = 'positive')
plt.scatter(negative[:,0],negative[:,1],c = 'b',marker = 'o',label = 'negative')
plt.legend()
plt.show()












