import numpy as np
'''
numpy.empty
它创建指定形状和dtype的未初始化数组。 它使用以下构造函数：
numpy.empty(shape, dtype = float, order = 'C')
1.	Shape 空数组的形状，整数或整数元组
2.	Dtype 所需的输出数组类型，可选
3.	Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''

# 数组元素为随机值，因为它们未初始化。
x = np.empty([3,2], dtype =np.int8)
print(x)


# numpy.zeros 返回特定大小，以 0 填充的新数组.
# numpy.zeros(shape, dtype = float, order = 'C')
# 含有 5 个 0 的数组，默认类型为 float
x = np.zeros(5)
print(x)

x = np.zeros((5,), dtype = np.int8)
print(x)


# 自定义类型
x = np.zeros((2,2), dtype =  [('x',  'i4'),  ('y',  'f4')])
print(x)
print(x['x'])
print(x['y'])


# numpy.ones
# 返回特定大小，以 1 填充的新数组。 numpy.ones(shape, dtype = None, order = 'C')
x = np.ones(5)
print(x)


x = np.ones([2,2], dtype =np.int32)
print(x)
































