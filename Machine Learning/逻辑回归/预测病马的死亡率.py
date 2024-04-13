import numpy as np
import matplotlib.pyplot as plt
import logic_library
from sklearn.model_selection import train_test_split
data = np.loadtxt('horseColicTraining.txt')
numof = data.shape[1]
l = data.shape[0]
w = np.ones(numof).reshape(numof,1)
print(w)
X = data[:,:numof-1]
X = (X - X.mean(0)) / X.std(0)
X = np.insert(X,0,1,1)
y = data[:,numof-1:]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=17)
epochs = 1000
lr = 0.01
lamda = 0.5
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

