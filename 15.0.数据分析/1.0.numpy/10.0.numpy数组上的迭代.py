import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a)
# 使用nditer对它进行迭代。
for x in np.nditer(a):
    print(x)
# 只会降低一个维度
for i in a:
    print(i)

# 迭代的顺序匹配数组的内容布局，而不考虑特定的排序。 这可以通过迭代上述数组的转置来看到。
b = a.T
# 倒叙输出
for x in np.nditer(b):
    print(x)

# 迭代顺序
# 如果相同元素使用 F 风格顺序存储，则迭代器选择以更有效的方式对数组进行迭代。
a = np.arange(0,60,5)
a = a.reshape(3,4)
b = a.T
print('以 C 风格顺序排序：')
c = b.copy(order='C')
for x in np.nditer(c):
    print(x)
print('以 F 风格顺序排序：')
c = b.copy(order='F')
for x in np.nditer(c):
    print(x)


# 可以通过显式提醒，来强制nditer对象使用某种顺序：
a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a, order =  'C'):
    print(x)
for x in np.nditer(a, order =  'F'):
    print(x)





















