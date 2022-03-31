import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=0.1*x

plt.figure()
plt.plot(x,y,linewidth=2)
plt.ylim(-2,2)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    # bbox是label后面的框框
    # 去掉边框 加edgecolor='None
    label.set_bbox(dict(facecolor='white',alpha=0.7))


plt.show()





































