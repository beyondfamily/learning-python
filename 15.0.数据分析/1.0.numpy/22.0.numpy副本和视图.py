import numpy as np
# 在执行函数时，其中一些返回输入数组的副本，而另一些返回视图。
# 当内容物理存储在另一个位置时，称为副本。
# 另一方面，如果提供了相同内存内容的不同视图，我们将其称为视图。

# 无复制
# 简单的赋值不会创建数组对象的副本。
# 相反，它使用原始数组的相同id()来访问它。
# id()返回 Python 对象的通用标识符，类似于 C 中的指针。
a = np.arange(6)
print(id(a))
b = a
print(id(b))
# 修改b的形状
b.shape =(3,2)
print(b)
# a的形状也修改了
print(a)


# 视图或浅复制
# NumPy 拥有ndarray.view()方法，它是一个新的数组对象，并可查看原始数组的相同数据。
# 与前一种情况不同，新数组的维数更改不会更改原始数据的维数。
a0 = np.arange(6).reshape(3,2)
print(a0)
# 创建 a 的视图
b0=a0.view()
print(b0)
# 两个数组的 id() 不同：
print(id(a0))
print(id(b0))
# 修改 b 的形状，并不会修改 a
b0.shape=(2,3)
print(b0)
print(a0)


# 数组的切片也会创建视图
a = np.array([[10,10],  [2,3],  [4,5]])
print(a)
s=a[:,:2]
print(s)


# ndarray.copy()函数创建一个深层副本。 它是数组及其数据的完整副本，不与原始数组共享。
a1= np.array([[10,10],  [2,3],  [4,5]])
print(a1)
b1=a1.copy()
# b1 与 a1 不共享任何内容
# 我们能够写入 b1 来写入 a1 吗？
print(b1 is a1)
b1[0,0]  =  100
print(b1)
print(a1)










