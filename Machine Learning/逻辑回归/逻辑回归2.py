import numpy as np
import math
import matplotlib.pyplot as plt
def sigmoid(train_x,w):
    z = train_x.dot(w)
    y_pre = 1 / 1 + np.exp(-z)
    return y_pre
def myloss(train_x,train_y,w):
    y_pre=sigmoid(train_x,w)
    loss_avg = (-train_y * np.log(y_pre) - (1 - train_y) * np.log(1-y_pre)).mean()
    return loss_avg
def mygradient(train_x,train_y,w):
    gradient = train_x.T.dot(sigmoid(train_x,w) - train_y) / train_x.shape(0)
    return gradient
def mygradient_decent(train_x,train_y,w,epoch,lr):
    loss = []
    for i in range(epoch):
        w -= lr * mygradient(train_x,train_y,w)
        loss.append(myloss(train_x,train_y,w))
        if i%100 == 0:
            print(f"{i}次迭代后损失为：{myloss(train_x, train_y, w)}")
    return w,loss
w,loss = mygradient_decent(train_x,train_y,w,epoch = 10000,lr = 0.01)
plt.plot(range(100),loss)
plt.title("the Epoch-error plot")
plt.xlabel("Epochs")
plt.ylabel("total error")
plt.show()
