import numpy as np

'''
1.	dot 两个数组的点积
2.	vdot 两个向量的点积
3.	inner 两个数组的内积
4.	matmul 两个数组的矩阵积
5.	determinant 数组的行列式
6.	solve 求解线性矩阵方程
7.	inv 寻找矩阵的乘法逆矩阵
'''

# numpy.dot()
# 此函数返回两个数组的点积。 对于二维向量，其等效于矩阵乘法。
# 对于一维数组，它是向量的内积。
# 对于 N 维数组，它是a的最后一个轴上的和与b的倒数第二个轴的乘积。
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
# [[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
print(np.dot(a,b))


# numpy.vdot()
# 此函数返回两个向量的点积。 如果第一个参数是复数，那么它的共轭复数会用于计算。 如果参数id是多维数组，它会被展开。
# 1*11 + 2*12 + 3*13 + 4*14 = 130
print(np.vdot(a,b))


# numpy.inner()
# 此函数返回一维数组的向量内积。 对于更高的维度，它返回最后一个轴上的和的乘积。
# 1*0+2*1+3*0
print(np.inner(np.array([1,2,3]),np.array([0,1,0])))
# 多维数字演示
a = np.array([[1,2], [3,4]])
b = np.array([[11, 12], [13, 14]])
# 1*11+2*12, 1*13+2*14
# 3*11+4*12, 3*13+4*14
print(np.inner(a,b))


# numpy.matmul()
# numpy.matmul()函数返回两个数组的矩阵乘积。
# 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播。
a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print(np.matmul(a,b))


# 二维和一维运算
a = [[1,0],[0,1]]
b = [1,2]
print(np.matmul(a,b))
print(np.matmul(b,a))


# 维度大于二的数组
a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print(np.matmul(a,b))


# numpy.linalg.det()
# 函数计算输入矩阵的行列式
a = np.array([[1,2], [3,4]])
print(np.linalg.det(a))

b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print(np.linalg.det(b))


# numpy.linalg.solve()
# 函数给出了矩阵形式的线性方程的解
'''
x + y + z = 6
2y + 5z = -4
2x + 5y - z = 27
'''
a=np.array([[1,1,1],[0,2,5],[2,5,-1]])
b=np.array([6,-4,27])
x=np.linalg.solve(a,b)
print(x)


# numpy.linalg.inv()
# 我们使用numpy.linalg.inv()函数来计算矩阵的逆。 矩阵的逆是这样的，如果它乘以原始矩阵，则得到单位矩阵。
x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x,y))

# 现在让我们在示例中创建一个矩阵A的逆。
a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
ainv = np.linalg.inv(a)
b = np.array([[6],[-4],[27]])
# 计算A^(-1)B
x = np.linalg.solve(a,b)
print(x)
# 这就是线性方向 x = 5, y = 3, z = -2 的解













































