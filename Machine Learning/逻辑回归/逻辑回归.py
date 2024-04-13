import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# 载入数据
path = '/Users/zhong/Desktop/logistic_regression.pkl'
data = np.load(path,allow_pickle=True)
# 定义数据 前两列分别为参数1，参数2，第三列为结果（0/1）
data = pd.DataFrame(data,columns=["parameter1","parameter2","result"])
print(data.head()) # 数据检测
# 创造画布（fig）与坐标轴（ax）
fig, ax = plt.subplots(figsize=(12,8))
# 自规定 将结果为1的分为positive类 ， 将结果为0的分为negative类，以用于数据的逻辑回归分类
positive = data[data['result'].isin([1.])]
negative = data[data['result'].isin([0.])]
# 设置散点图（传入各种参数）
ax.scatter(positive['parameter1'], positive['parameter2'], s=50, c='b', marker='o', label='positive')
ax.scatter(negative['parameter1'], negative['parameter2'], s=50, c='r', marker='x', label='negative')
# 设置图例 就是右上角那一小块
ax.legend()
# 设置横纵坐标标签
ax.set_xlabel('parameter1')
ax.set_ylabel('parameter2')
# 显示图像
plt.show()
data.insert(0,'ones',1) # 插入全一列
# 数据打乱
data = data.sample(frac = 1).reset_index(drop = True)
# 设置划分比例
ratio = 0.8 # 0.8为训练集 ，0.2 为测试集
# 数据集划分
train_data = data.sample(frac = ratio,random_state=1)
valid_data = data.drop(train_data.index)

# 数据载入（转换为numpy）(提取X与y)
train_X=np.array(train_data.iloc[:,0:3])
train_y=np.array(train_data.iloc[:,3])
valid_X=np.array(valid_data.iloc[:,0:3])
valid_y=np.array(valid_data.iloc[:,3])


# 试着检测你的数据
print(data.head())
print(train_X.shape)
print(train_y.shape)
theta = np.zeros((1,3))
def sigmoid(z):
    y = 1 / (1+np.exp(-z))
    return y
# 注意X，与theta的形状 train_X为(1638, 3) theta为（1,3）
def mylinear(X, theta):
    y = np.dot(X,theta.T)
    return y
def mymodel(X, theta):
    y_pre = sigmoid(mylinear(X, theta))
    return y_pre
def myloss(y,X, theta):
    y_pre=mymodel(X,theta)
    coeff1 = (-y * np.log(y_pre) - (1 - y) * np.log(1-y_pre)).mean()#求取均值
#损失函数
    return coeff1
def one_epoch_gradient(y, theta, X):
    y_pre = mymodel(X, theta)
    gradient = np.dot(X.T,(y_pre - y)) / y.shape[0]
    return gradient
def train_gradient_decent(X, theta, Y, epoch=1000, batch_size=10, lr=0.0001):
    for epoch_idx in range(epoch):
        loss_avg = 0
        batch_idx = 0
        loss = []
        for i in range(int(len(X) / batch_size)):
            x, y = X[batch_idx:batch_idx + batch_size], Y[batch_idx:batch_idx + batch_size]
            z = mylinear(x,theta)
            h = sigmoid(z)
            g = one_epoch_gradient(y,theta,x)
            theta -= lr * g.T
            z = mylinear(X,theta)
            h = sigmoid(z)
            loss.append(myloss(y,x, theta))
            batch_idx += batch_size
        loss = np.array(loss)
        l = len(loss)
        if epoch % 100 == 0:
            print(f'epoch:{epoch_idx} loss_avg:{loss.sum() / l}')
    return theta
result = train_gradient_decent(train_X,theta,train_y.reshape(train_y.shape[0],1))
print(result)
x = valid_X
y = valid_y
y = y.reshape(y.shape[0],1)
y_pre_eval = mymodel(X=x,theta=result)
for i in range(len(y)):
    if y_pre_eval[i] >= 0.5:
        y_pre_eval[i] = 1
    else:
        y_pre_eval[i] = 0
correct=(y_pre_eval==y).astype(int)
print(f'acc:{correct.sum()/len(y)}')





