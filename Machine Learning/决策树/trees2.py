from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
import numpy as np
iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)
clf = tree.DecisionTreeClassifier(criterion='entropy')
# 从sklearn中导入tree，啊，那我自己花一下午在干嘛。
clf = clf.fit(x,y)
score = clf.score(x_test,y_test)
print(score)
pre = clf.predict(x_test)
print(pre)
error = 0
for i in range(len(pre)):
    print(f'the pre is {pre[i]}, the real result is {y_test[i]}')
    if pre[i]!=y_test[i]:
        error += 1
print(f'the total error is {error}')
data = np.array([  [1,1],
                [1,1],
                [1,0],
                [0,1],
                [0,1],
                [1,1]])
target = np.array([1,1,0,0,0,1])
test = np.array([[1,1],[0,1]])
result = np.array([1,0])
clf2 = tree.DecisionTreeClassifier(criterion='entropy')
clf2 = clf2.fit(data,target)
score = clf2.score(test,result)
print(score)
pre = clf2.predict(test)
error2 = 0
for i in range(test.shape[0]):
    print(f'the pre2 is {pre[i]}, the real result2 is {result[i]}')
    if pre[i]!=result[i]:
        error2 += 1
print(f'the total error2 is {error2}')


