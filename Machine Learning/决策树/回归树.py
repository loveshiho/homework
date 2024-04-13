import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
np.set_printoptions(suppress = True)
from sklearn.model_selection import train_test_split
names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','GE','DIS','RAD','TAX','PRTATIO','B','LSTAT','PRICE']
data = pd.read_csv("/Users/zhong/Desktop/housing.data.csv",names = names,delim_whitespace=True)
#6 读取数据
print(data)
print("*"*100)
boston = np.array(data)
#10 向量化
target = boston[:,13]
data = boston[:,:13]
#12 13 切片
data = (data - data.mean(0)) / data.std(0)
# data = np.insert(data,0,1.,axis=1)
#16 加一列1 方便后续矩阵运算
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size = 0.2,random_state = 20)
clf = DecisionTreeRegressor(criterion = 'squared_error',random_state = 17)
clf.fit(X_train,y_train)
w = clf.feature_importances_ # 特征权重，属于该分类器的属性。
print(w)
score = clf.score(X_test,y_test)
pre = clf.predict(X_test)
for i in range(X_test.shape[0]):
    print(f'the pre is {pre[i]}, the real result is {y_test[i]}')
cost = (0.5*(pre - y_test)**2).mean()
print(cost)
