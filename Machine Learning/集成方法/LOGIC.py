import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
# 载入数据
path = '/Users/zhong/Desktop/logistic_regression.pkl'
data = np.load(path,allow_pickle=True)
# 定义数据 前两列分别为参数1，参数2，第三列为结果（0/1）
data = pd.DataFrame(data,columns=["parameter1","parameter2","result"])
x = np.array(data.iloc[:,:2])
y = np.array(data.iloc[:,2:])
y = np.ravel(y)
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 17)
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