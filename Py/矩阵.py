import numpy as np
data1 = np.array([[5,-3,1,1,-3],[2,-1,0,1,-2],[3,-2,1,1,1],[4,-3,2,-1,0]])
data2 = np.array([[20],[9],[14],[13]])
data3 = np.linalg.inv(data1.T.dot(data1)).dot(data1.T).dot(data2)
print(data3)