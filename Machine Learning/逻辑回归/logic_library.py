import numpy as np
# 参数，特征，标签。
def sigmoid(z):
    g = 1 / (1 + np.exp(-z))
    return g
def my_pre(w,X_train):
    z = X_train.dot(w)
    y_pre = sigmoid(z)
    return y_pre
def my_gradient_regulation(X_train,y_train,w,lamda):
    numof = len(X_train)
    gradient_regulation = (X_train.T.dot(my_pre(w,X_train) - y_train) + lamda * w) / numof
    return gradient_regulation
def my_cost(X,y,w,lamda):
    numof = len(X)
    y_pre = my_pre(w,X)
    J_sum = (-y * np.log(y_pre) - (1 - y) * np.log(1 - y_pre)).sum() + (lamda/2 * w**2).sum()
    J = J_sum / numof
    return J
def my_gradient_decent(X_train,X_test,y_train,y_test,w,epochs,lr,lamda):
    loss_train = []
    loss_test = []
    for i in range(epochs):
        dJ_dw = my_gradient_regulation(X_train,y_train,w,lamda)
        w -= lr * dJ_dw
        if i%5 ==0:
            loss_train.append(my_cost(X_train,y_train,w,lamda))
            loss_test.append(my_cost(X_test,y_test,w,lamda))
    return w,loss_train,loss_test
def mypredict(X_test,w):
    numof = len(X_test)
    y_predict = [0]*numof
    y_pre = my_pre(w,X_test)
    for i in range(numof):
        if y_pre[i] >= 0.5:
            y_predict[i] = 1
    return y_predict
def my_evaluate(y_predict,y_test):
    numof = len(y_test)
    error = 0
    for i in range(numof):
        if y_predict[i] != y_test[i]:
            error += 1
    accuracy = (numof - error) / numof
    return error,accuracy




