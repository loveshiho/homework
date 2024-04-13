from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
import scipy.io
mnist = scipy.io.loadmat('mnist-original.mat')
data = np.array(mnist['data']).T
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i][j] != 0:
            data[i][j] = 1
#6 转化为可执行的向量
target = np.ravel(mnist['label'])   # 报错，标签不要用二维数组，用一维列表或一维数组。
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size = 0.2)
num = 100
error = 0
clf = AdaBoostClassifier(n_estimators = num)
clf.fit(X_train,y_train)
w = clf.feature_importances_ # 特征权重，属于该分类器的属性。
print(w)
score = clf.score(X_test,y_test)
pre = clf.predict(X_test)
for i in range(X_test.shape[0]):
    print(f'the pre is {pre[i]}, the real result is {y_test[i]}')
    if pre[i] != y_test[i]:
        error += 1
print(f'the total error is {error}')
print(f'the accuracy is {score}')

