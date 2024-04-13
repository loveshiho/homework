import matplotlib.pyplot as plt
x = ["September"+" "+str(i)+"th"for i in range(18,28)]
y1 = [33,33,34,35,34,33,32,32,32,32]
y2 = [25,26,26,26,26,26,25,25,24,25]
plt.plot(x,y1,color = "y",label = 'highest',linestyle = '--',marker = 'o',alpha = 1.0)
plt.plot(x,y2,color = 'b',label = 'lowest',linestyle = ':',marker = 'x',alpha = 1.0)
plt.xticks(rotation = 15)
plt.ylabel("temperature",fontsize = 14,rotation = 90,labelpad= 20)
plt.xlabel("days",fontsize = 14,labelpad= 13)
plt.legend()
plt.show()
