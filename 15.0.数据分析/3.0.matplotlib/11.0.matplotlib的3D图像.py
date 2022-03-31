import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig=plt.figure()
ax=Axes3D(fig,auto_add_to_figure=True)
# X,Y value
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
# height value
Z=np.sin(R)
# rstride和cstride 确定步长 精细度
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# zdir 确定等高线是从哪里压下了的'z' 是从上往下压 offset 从0压到-2
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
# 固定一下等高线的高度
ax.set_zlim(-2,2)


plt.show()







