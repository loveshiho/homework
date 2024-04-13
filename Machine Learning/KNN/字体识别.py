import numpy as np
from sklearn.model_selection import train_test_split
import scipy.io
mnist = scipy.io.loadmat('mnist-original.mat')
data = np.array(mnist['data']).T
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i][j] != 0:
            data[i][j] = 1
#6 转化为可执行的向量
target = np.array(mnist['label']).T
X_train,X_test,y_train,y_test = train_test_split(data,target,test_size = 0.2)
#12 划分训练集、测试集
def myKNN(onetest_X,X_train,y_train,k):
    numsamples = X_train.shape[0]
    diff = []
    for i in range(numsamples):
        diff.append(onetest_X - X_train[i])
    diff = np.array(diff)
    squarediff = diff**2
    squaredist = np.sum(squarediff,axis=1)
    distance = squaredist**0.5
#17 计算欧式距离
    sorted_indices = np.argsort(distance)
#24 排序
    map_label = {}
    for j in range(k):
        lab = y_train[sorted_indices[j]]
        lab = tuple(lab)
        map_label[lab] = map_label.get(lab,0)+1
#27 标记
    maxCount = 0
    for key,value in map_label.items():
        if (value > maxCount):
            maxCount = value
            maxIndex = key
    return maxIndex
#33 索引出现次数最多的数字
#KNN算法
numtestsamples = X_test.shape[0]
correct = 0
for i in range(numtestsamples):
    predict = myKNN(X_test[i],X_train,y_train,3)
    print(f"{i} result is: {predict},real result is: {y_test[i]}")
    if predict == y_test[i]:
        correct += 1
accuracy = float(correct) / numtestsamples
#42 测试模型
print(accuracy)


