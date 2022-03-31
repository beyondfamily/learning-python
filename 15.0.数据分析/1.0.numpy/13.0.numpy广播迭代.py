import numpy as np

# 如果两个数组是可广播的，nditer组合对象能够同时迭代它们。 假设数组a具有维度 3X4，并且存在维度为 1X4 的另一个数组b，则使用以下类型的迭代器（数组b被广播到a的大小）。


a = np.arange(0,60,5)
a = a.reshape(3,4)
b = np.array([1,  2,  3,  4], dtype =  int)
for x,y in np.nditer([a,b]):
    print("%d:%d" % (x, y))









