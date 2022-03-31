import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50) # 50个点
y1=2*x+1
y2=x**2

# 第一组figure()的参数
plt.figure()
plt.plot(x,y1)

# 第二组figure()的参数
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
# 定义第二条线
plt.plot(x,y1,color='red',linewidth=5.0,linestyle='--')

plt.show()

