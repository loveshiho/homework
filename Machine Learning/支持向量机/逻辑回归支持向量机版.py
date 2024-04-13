import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
# 载入数据
path = '/Users/zhong/Desktop/logistic_regression.pkl'
data = np.load(path,allow_pickle=True)
# 定义数据 前两列分别为参数1，参数2，第三列为结果（0/1）
data = pd.DataFrame(data,columns=["parameter1","parameter2","result"])
x = np.array(data.iloc[:,:2])
y = np.array(data.iloc[:,2:])
y = np.ravel(y)
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 17)
clf =  LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
 intercept_scaling=1, loss='squared_hinge', max_iter=1000,
 multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
 verbose=0)
clf.fit(X_train,y_train)
w = clf.coef_
b = clf.intercept_
score = clf.score(X_test,y_test)
error = 0
print(f'the martix of w is {w}')
print(f'the b is {b}')
pre = clf.predict(X_test)
for i in range(X_test.shape[0]):
    print(f'{i} the pre is {pre[i]}, the real result is {y_test[i]}')
    if pre[i] != y_test[i]:
        error += 1
print(f'the total error is {error}')
print(f'the accuracy is {score}')

