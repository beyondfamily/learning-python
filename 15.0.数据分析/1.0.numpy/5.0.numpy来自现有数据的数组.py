import numpy as np

# numpy.asarray
# 此函数类似于numpy.array，除了它有较少的参数。 这个例程对于将 Python 序列转换为ndarray非常有用。
# numpy.asarray(a, dtype = None, order = None)
'''
1.	a 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
2.	dtype 通常，输入数据的类型会应用到返回的ndarray
3.	order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
x = [1, 2, 3]
a = np.asarray(x)
print(a)

x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

x = (1, 2, 3)
a = np.asarray(x)
print(a)

# 来自元组列表的 ndarray
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x, dtype=object)
print(a)

# numpy.fromiter
# 此函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组。
# numpy.fromiter(iterable, dtype, count = -1)
'''
1.	iterable 任何可迭代对象
2.	dtype 返回数组的数据类型
3.	count 需要读取的数据数量，默认为-1，读取所有数据
'''
list = range(5)
it=iter(list)
# # 使用迭代器创建 ndarray
x = np.fromiter(it, dtype =  float)
print(x)


