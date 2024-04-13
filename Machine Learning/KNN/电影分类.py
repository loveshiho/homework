import numpy as np
import matplotlib.pyplot as plt
def createDataset():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
def myKNN(inputdata,dataset,labels,k):
    numspace = dataset.shape[0]
    diff = dataset - inputdata
    dis = (diff**2).sum(1)
    distance = dis**0.5
    sorteddistance = np.argsort(distance)
    classcount = {}
    for j in range(k):
        votelabel = labels[sorteddistance[j]]
        classcount[votelabel] = classcount.get(votelabel,0) + 1
    max_num = 0
    for key,value in classcount.items():
        if value > max_num:
            max_num = value
            ans = key
    return ans
group,labels = createDataset()
plt.figure(figsize = (12,8))
plt.scatter(group[:2,0],group[:2,1],c = 'r',marker = 'x',label = 'A')
plt.scatter(group[2:,0],group[2:,1],c = 'b',marker = 'o',label = 'B')
data = np.array([0,-1])
plt.scatter(data[0],data[1],c = 'black',marker = '^',label = 'p')
plt.legend(loc = 'best')
plt.show()
predict = myKNN(data,group,labels,3)
print(f"the predict is {predict}")



