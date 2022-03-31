import matplotlib.pyplot as plt
import numpy as np

# 计算高度函数
def f(x,y):
    # the height function
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
# 将x和y绑定成网格的输入值
X,Y=np.meshgrid(x,y)

# use plt.contourf to filling contours 是来绘制等高线的
# cmap 选择颜色类型 # 8 是等高线分成几份
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

# 绘制等高线线
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=0.5)

# 数据描述
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()













