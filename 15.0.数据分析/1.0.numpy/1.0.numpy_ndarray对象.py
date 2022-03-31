import numpy as np

# 一个维度
a = np.array([1,2,3])
print(a)

# 两个维度
a = np.array([[1,  2],  [3,  4]])
print(a)


# 最小维度
a = np.array([1,2,3,4,5],ndmin=3)
print(a)


# dtype 参数 # complex 表示复数
a = np.array([1,2,3], dtype = complex)
print(a)




