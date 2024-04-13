import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logic_library
from sklearn.model_selection import train_test_split
path1 = "/Users/zhong/Desktop/diabetes_train.csv"
data = pd.read_csv(path1)
data = data[(data.BloodPressure != 0)&(data.BMI != 0)&(data.Glucose != 0)]
data = np.array(data)
features = data[:,0:8]
target = data[:,8:]
#features[:,7] = features[:,7]**2
#features[:,6] = features[:,6]**3
#features[:,3] = features[:,3]**0.5
features = (features - features.min(0)) / (features.max(0) - features.min(0))
features = np.insert(features,0,1,1)
X_train,X_test,y_train,y_test = train_test_split(features,target,test_size=0.05,random_state=17)
l = features.shape[1]
w = np.ones(l).reshape(l,1)
epochs = 5000
lr = 0.01
lamda = 0.2
w,loss_train,loss_test = logic_library.my_gradient_decent(X_train,X_test,y_train,y_test,w,epochs,lr,lamda)
pre = logic_library.mypredict(X_test,w)
error,accuracy = logic_library.my_evaluate(pre,y_test)
print(f'the final w is {w}')
print(f'the total error is {error}')
print(f'the accuracy is {accuracy}')
x = range(0,epochs,5)
y1 = loss_train
y2 = loss_test
plt.figure(figsize=(12,8))
plt.plot(x,y1,color = 'b',label = 'J_train')
plt.plot(x,y2,color = 'r',linestyle = '--',label = 'J_test')
plt.xlabel('Epochs',fontsize = 15)
plt.ylabel('the cost',fontsize = 15)
plt.legend(fontsize = 15)
plt.show()

