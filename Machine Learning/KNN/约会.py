import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('datingTestSet.txt',sep = '\t',names = ['D_road','P_game','C_ic','feeling'])
data.loc[data[data.feeling == 'largeDoses'].index.tolist(),'feeling'] = 3
data.loc[data[data.feeling == 'smallDoses'].index.tolist(),'feeling'] = 2
data.loc[data[data.feeling == 'didntLike'].index.tolist(),'feeling'] = 1
#索引出数据并进行赋值，需反复学习。
data = np.array(data,dtype = float)
value = data[:,:3]
target = data[:,3:]
value = (value - value.mean(0)) / value.std(0)
lenofvalue = len(value)
ratio = 0.8
train_X = value[:int(lenofvalue * ratio),:]
train_y = target[:int(lenofvalue * ratio),:]
test_X = value[int(lenofvalue * ratio):,:]
test_y = target[int(lenofvalue * ratio):,:]
def myKNN(onetest,train_X,train_y,k):
    diff = train_X - onetest
    dis = (diff**2).sum(1)
    distance = dis**0.5
    sortedDistance = np.argsort(distance)
    classcount = {}
    #返回，值从小到大排列的索引，返回的是一串索引。
    for i in range(k):
        votelabel = train_y[sortedDistance[i]]
        votelabel = tuple(votelabel)
        classcount[votelabel] = classcount.get(votelabel,0) + 1
    max_num = 0
    for key,value in classcount.items():
        if max_num < value:
            max_num = value
            ans = key
    return ans
lenoftest = len(test_X)
errorCount = 0
for i in range(lenoftest):
    pre = myKNN(test_X[i],train_X,train_y,3)
    print(f"the predict is {list(pre)}, the real result is {test_y[i]}")
    if pre != test_y[i]:
        errorCount += 1
print(f"the total error is {errorCount}")
print(f'the accuracy is {(lenoftest-errorCount) / lenoftest}')
