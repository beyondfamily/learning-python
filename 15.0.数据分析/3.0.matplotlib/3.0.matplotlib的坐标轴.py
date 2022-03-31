import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=5.0,linestyle='--')

# 设置坐标轴 的取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
# 设置坐标轴的注释
plt.xlabel('I am X')
plt.ylabel('I am Y')

# 设置新的小标
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
# y轴换一些部分文字上去
# 通过$来选取字体
# \alpha 显示阿尔法
plt.yticks([-2,-1.8,-1,1.22,3],
            [r'$really\ bad$',r'$bad$','normal',r'$good\ \alpha$','$really\ good$'])

# gca='get current axis'
# 拿出轴
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 坐标轴的代替
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# x轴绑定在y轴的-1上
# ax.spines['bottom'].set_position(('data',-1))
# ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# axes 根据百分比来调整位置
ax.spines['bottom'].set_position(('axes',0.6))

plt.show()














