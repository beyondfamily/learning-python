import matplotlib.pyplot as plt
import numpy as np


n=1024
# 分布的均值是0 分布的标准差是1
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
# for color value
T=np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# plt.scatter(np.arange(5),np.arange(5))

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
# 隐藏ticks值
plt.xticks(())
plt.yticks(())

plt.show()



