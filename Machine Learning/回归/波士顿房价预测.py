import pandas as pd
import numpy as np
np.set_printoptions(suppress = True)
from sklearn.model_selection import train_test_split
names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','GE','DIS','RAD','TAX','PRTATIO','B','LSTAT','PRICE']
data = pd.read_csv("/Users/zhong/Desktop/housing.data.csv",names = names,delim_whitespace=True)
#6 读取数据
print(data)
print("*"*10)
data2 = data.iloc[:,0:1]
print(data2)
boston = np.array(data)
#10 向量化
target = boston[:,13:]
data = boston[:,:13]
data = (data - data.mean(0)) / data.std(0)
#12 13 切片
data = np.insert(data,0,1,axis=1)
#16 加一列1 方便后续矩阵运算
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size = 0.2)
print(data[1])
w = np.ones(14).reshape(14,1)
w = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)
#20 最小二乘法
print(w)
loss = (0.5*(X_train.dot(w) - y_train)**2).mean()
print(f"损失为{loss}")
numtestsamples = y_test.shape[0]
for i in range(numtestsamples):
    print(f"{i} result is: {X_test[i].dot(w)},the real answer is: {y_test[i]}")

