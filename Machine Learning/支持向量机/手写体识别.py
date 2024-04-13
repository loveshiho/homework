import numpy as np
from sklearn.model_selection import train_test_split
import scipy.io
from sklearn.svm import LinearSVC
mnist = scipy.io.loadmat('mnist-original.mat')
data = np.array(mnist['data']).T
target = np.ravel(mnist['label'])
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i][j] != 0:
            data[i][j] = 1
#6 转化为可执行的向量
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size = 0.2,random_state = 17)
clf =  LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
 intercept_scaling=1, loss='squared_hinge', max_iter=10000,
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
    print(f'the pre is {pre[i]}, the real result is {y_test[i]}')
    if pre[i] != y_test[i]:
        error += 1
print(f'the total error is {error}')
print(f'the accuracy is {score}')



