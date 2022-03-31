import numpy as np
import numpy.matlib

# numpy.empty()函数返回一个新的矩阵，而不初始化元素。 该函数接受以下参数。
'''
1.	shape 定义新矩阵形状的整数或整数元组
2.	Dtype 可选，输出的数据类型
3.	order C 或者 F
'''
print(np.empty((2,2)))


# numpy.zeros()
# 此函数返回以零填充的矩阵
print(np.zeros((2,2)))


# numpy.ones()
# 此函数返回以1填充的矩阵
print(np.ones((2,2)))


# numpy.eye(n, M,k, dtype)
# 这个函数返回一个矩阵，对角线元素为 1，其他位置为零。
'''
1.	n 返回矩阵的行数
2.	M 返回矩阵的列数，默认为n
3.	k 对角线的索引
4.	dtype 输出的数据类型
'''
print(np.eye(3,4,k=0,dtype=np.int32))
print(np.eye(3,4,k=1,dtype=np.int32))


# numpy.identity()函数返回给定大小的单位矩阵。
# 单位矩阵是主对角线元素都为 1 的方阵。
print(np.identity(5,dtype=float))


# numpy.random.rand()
# 函数返回给定大小的填充随机值的矩阵。
print(numpy.random.rand(3,3))


# 注意，矩阵总是二维的，而ndarray是一个 n 维数组。 两个对象都是可互换的。
i=np.matrix('1,2;3,4')
print(i)
j=np.asarray(i)
print(j)
k=np.asmatrix(j)
print(k)















