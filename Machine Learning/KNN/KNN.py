import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# 载入数据
path = '/Users/zhong/Desktop/logistic_regression.pkl'
data = np.load(path,allow_pickle=True)
# 定义数据 前两列分别为参数1，参数2，第三列为结果（0/1）
data = pd.DataFrame(data,columns=["parameter1","parameter2","result"])
print(data.head()) # 数据检测
# 创造画布（fig）与坐标轴（ax）
fig, ax = plt.subplots(figsize=(12,8))
# 自规定 将结果为1的分为positive类 ， 将结果为0的分为negative类，以用于数据的逻辑回归分类
positive = data[data['result'].isin([1.])]
negative = data[data['result'].isin([0.])]
# 设置散点图（传入各种参数）
ax.scatter(positive['parameter1'], positive['parameter2'], s=50, c='b', marker='o', label='positive')
ax.scatter(negative['parameter1'], negative['parameter2'], s=50, c='r', marker='x', label='negative')
# 设置图例 就是右上角那一小块
ax.legend()
# 设置横纵坐标标签
ax.set_xlabel('parameter1')
ax.set_ylabel('parameter2')
# 显示图像
plt.show()
data.insert(0,'ones',1) # 插入全一列
# 数据打乱
data = data.sample(frac = 1).reset_index(drop = True)
# 设置划分比例
ratio = 0.8 # 0.8为训练集 ，0.2 为测试集
# 数据集划分
train_data = data.sample(frac = ratio,random_state=1)
valid_data = data.drop(train_data.index)

# 数据载入（转换为numpy）(提取X与y)
train_X=np.array(train_data.iloc[:,0:3])
train_y=np.array(train_data.iloc[:,3])
valid_X=np.array(valid_data.iloc[:,0:3])
valid_y=np.array(valid_data.iloc[:,3])

def myKNN(Pred_data,train_X,train_y,k):
    rows = train_X.shape[0]
    diff = np.tile(Pred_data,(rows,1)) - train_X
#遍历train_X，得出差值
    sqrt_dist = np.sum(diff ** 2,axis=1)
    distance = sqrt_dist ** 0.5
#计算欧式距离
    sorted_indices = np.argsort(distance)
#排序
    map_label = {}
    for i in range(k):
        label = train_y[sorted_indices[i]]
        map_label[label] = map_label.get(label,0)+1
    max_num = 0
    for key,value in map_label.items():
        if(value>max_num):
            max_num = value
            ans = key
    return ans
#标记，索引
correct = 0
numValid = valid_X.shape[0]
for i in range(numValid):
    predict = myKNN(valid_X[i],train_X,train_y,5)
    print("%d: predict result is %d, real result is %d"%(i,predict,valid_y[i]))
    if predict == valid_y[i]:
        correct+=1
accuracy = float(correct) / numValid
print("the total number of errors is: %d"%(numValid - correct))
print("the correct accuracy is: %f"%(accuracy))








