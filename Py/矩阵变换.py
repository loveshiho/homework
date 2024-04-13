import numpy as np
np.set_printoptions(suppress=True)
np.set_printoptions(precision=4)
data1 = np.array([[2,2,3],[-2,4,5],[4,7,7]])
print(data1)
data2 = np.array([[3],[-7],[1]])
print(data2)
data3 = (np.dot(np.linalg.inv(data1),data2))
print(data3)


