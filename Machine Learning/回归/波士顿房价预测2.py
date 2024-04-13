import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress = True)
from sklearn.model_selection import train_test_split
names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','GE','DIS','RAD','TAX','PRTATIO','B','LSTAT','PRICE']
data = pd.read_csv("/Users/zhong/Desktop/housing.data.csv",names = names,delim_whitespace=True)
#6 读取数据
print(data)
print("*"*10)
boston = np.array(data)
#10 向量化
target = boston[:,13:]
data = boston[:,:13]
#12 13 切片
data = (data - data.mean(0)) / data.std(0)
data = np.insert(data,0,1.,axis=1)
#16 加一列1 方便后续矩阵运算
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size = 0.2,random_state = 20) #固定随机数种子，保证每次运行程序，得到相同结果
w = np.ones(14).reshape(14,1)
print(w)
num = X_train.shape[0]
loss = []
loss2 = []
epoch = 10000
lamda = 0.5
def mygradient_regulation(X_train,y_train,w,lamda):
    gradient = (X_train.T.dot(X_train.dot(w) - y_train) + lamda * w) /num
    return gradient
def myloss(X_train,y_train,w):
    loss = (0.5*(X_train.dot(w) - y_train)**2).mean()
    return loss
def mygradient_decent(X_train,y_train,w,epoch,lr=0.001):
    for j in range(epoch):
        w -= lr*mygradient_regulation(X_train,y_train,w,lamda)
        if (j%100 == 0):
            loss.append(myloss(X_train,y_train,w))
            loss2.append(myloss(X_test,y_test,w))
            print(f"{j}次迭代后损失为：{myloss(X_train,y_train,w)}")
    return w,loss,loss2
w,loss,loss2 = mygradient_decent(X_train,y_train,w,epoch)
print(w)
numtestsamples = y_test.shape[0]
for i in range(numtestsamples):
    print(f"{i} result is: {X_test[i].dot(w)},the real answer is: {y_test[i]}")
plt.figure(figsize = (12,8))
plt.plot(range(0,epoch,100),loss,color = 'blue',label = 'J_train')
plt.plot(range(0,epoch,100),loss2,color = 'red',linestyle = '--',label = 'J_test')
plt.title("the Epoch-error plot")
plt.xlabel("Epochs")
plt.ylabel("total error")
plt.legend(fontsize = 15)
plt.show()
