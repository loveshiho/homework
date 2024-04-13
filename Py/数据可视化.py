import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,100)
y = np.cos(x)
plt.plot(x,y,marker = "x")
x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y,marker = "*",color = 'r')
plt.show()
