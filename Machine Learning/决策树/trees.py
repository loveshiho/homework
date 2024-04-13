import numpy as np
class Node:
    def __init__(self,dataset,index):
        numof = dataset.shape[1]
        target = dataset[:, -1]
        data = dataset[:, :numof - 1]
        self.data = data
        self.target = target
        self.index = index
        self.left = None
        self.right = None
def calShannonEnt(dataSet):
    numof = len(dataSet)
    labelCounts = {}
    dataSet_label = dataSet[:,-1]
    for i in range(numof):
        currentLabel = dataSet_label[i]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    ShannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / numof
        ShannonEnt -= p* np.log2(p)
    return ShannonEnt
def createDataSet():
    dataSet = np.array([[1,1,1],
                        [1,1,1],
                        [1,0,0],
                        [0,1,0],
                        [0,1,0],
                        [1,1,1]])
    return dataSet
def cal_information_gain(dataSet,a):
    Ent = calShannonEnt(dataSet)
    numof = len(dataSet)
    labelCounts = {}
    dataSet_label = dataSet[:,a]
    for i in range(numof):
        currentLabel = dataSet_label[i]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            #给标签进行初始化
        labelCounts[currentLabel] += 1
    gain = calShannonEnt(dataSet[:,a].reshape(numof,1))
    return Ent - gain
def splitDataSet(dataset,index,value):
    numof = dataset.shape[1]
    retDataSet = []
    target = dataset[:,-1]
    data = dataset[:,:numof-1]
    x = np.delete(data,obj= index,axis=1)
    loc = data[:,index]
    for i in range(dataset.shape[0]):
        if loc[i] == value:
            retDataSet.append(np.append(x[i,:],target[i]))
    retDataSet = np.array(retDataSet)
    return retDataSet
def get_best_feature(dataSet):
    numof = dataSet.shape[1]
    best_feature = {}
    for i in range(numof):
        temp = cal_information_gain(dataSet,i)
        best_feature[i] = best_feature.get(i,0) + temp
    max_num = 0
    ans = 0
    for key,value in best_feature.items():
        if max_num < value:
            max_num = value
            ans = key
    return ans
def mytree(dataset):
    numof = dataset.shape[1]
    dataset = dataset[:,:numof-1]
    index = get_best_feature(dataset)
    x_left = splitDataSet(dataset,index,0)
    x_right = splitDataSet(dataset,index,1)
    node = Node(dataset,index)
    if cal_information_gain(dataset,index) < 0.0001:
        return node
    node.left = mytree(x_left)
    node.right = mytree(x_right)
    return node
