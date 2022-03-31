import numpy as np

# ndarray对象的内容可以通过索引或切片来访问和修改，就像 Python 的内置容器对象一样。
# 基本切片是 Python 中基本切片概念到 n 维的扩展。 通过将start，stop和step参数提供给内置的slice函数来构造一个 Python slice对象。 此slice对象被传递给数组来提取数组的一部分。
a = np.arange(10)
s = slice(2,7,2)
print(s)
print(a[s])


a = np.arange(10)
b = a[2:7:2]
print(b)



a = np.arange(0,20,2)
b = a[5]
print(b)


# 对始于索引的元素进行切片
a = np.arange(10)
print(a[2:])


# 对索引之间的元素进行切片
a = np.arange(10)
print(a[2:5])


# 上面的描述也可用于多维ndarray。
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 对始于索引的元素进行切片
print(a[1:])

# 切片还可以包括省略号（...），来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的ndarray。
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# 第二列的元素
print(a[...,1])
# 第二行的元素
print(a[1,...])
# 现在我们从第二列向后切片所有元素：
print(a[...,1:])











