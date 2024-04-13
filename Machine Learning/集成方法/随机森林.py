import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
path = "/Users/zhong/Desktop/diabetes_train.csv"
data = pd.read_csv(path) # 读取训练集
data = data[(data.BloodPressure != 0)&(data.BMI != 0)&(data.Glucose != 0)]
data = np.array(data) # 转化为narray
features = data[:,0:8] # 切片
target = data[:,8] # 切片
X_train,X_test,y_train,y_test = train_test_split(features,target,test_size = 0.2,random_state = 7)
num = 100
error = 0
clf = RandomForestClassifier(criterion = 'entropy',n_estimators = num)
clf.fit(X_train,y_train)
w = clf.feature_importances_
print(w)
score = clf.score(X_test,y_test)
pre = clf.predict(X_test)
for i in range(X_test.shape[0]):
    print(f'the pre is {pre[i]}, the real result is {y_test[i]}')
    if pre[i] != y_test[i]:
        error += 1
print(f'the total error is {error}')
print(f'the accuracy is {score}')