import numpy as np

# ndarray.shape  这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)


# 这会调整数组大小
a = np.array([[1,2,3],[4,5,6]])
a.shape =  (3,2)
print(a)


# numpy也提供了reshape函数来调整数组大小。
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)


# ndarray.ndim这一数组属性返回数组的维数。
# 等间隔数字的数组
a = np.arange(24)
print(a)
print(a.ndim)
# 现在调整其大小
b = a.reshape(2,4,3)
print(b)
print(b.ndim)

print('='*80)

# numpy.itemsize 这一数组属性返回数组中每个元素的字节单位长度。
# 数组的 dtype 为 int8（一个字节）
x = np.array([1,2,3,4,5], dtype = np.int8)
print(x.itemsize)


# 数组的 dtype 现在为 float32（四个字节）
x = np.array([1,2,3,4,5], dtype = np.float32)
print(x.itemsize)


# numpy.flags
# ndarray对象拥有以下属性。这个函数返回了它们的当前值。
'''
1.	C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
2.	F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
3.	OWNDATA (O) 数组的内存从其它对象处借用
4.	WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
5.	ALIGNED (A) 数据和任何元素会为硬件适当对齐
6.	UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新
'''

x = np.array([1,2,3,4,5])
print(x.flags)























