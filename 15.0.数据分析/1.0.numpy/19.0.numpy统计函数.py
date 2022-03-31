import numpy as np

# numpy统计函数

# numpy.amin() 和 numpy.amax()
# 这些函数从给定数组中的元素沿指定轴返回最小值和最大值。
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(a)
print(np.amin(a,1))
print(np.amin(a,0))
print(np.amax(a))
print(np.amax(a, axis=0))


# numpy.ptp()
# numpy.ptp()函数返回沿轴的值的范围（最大值 - 最小值）
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(np.ptp(a))
print(np.ptp(a, axis =  1))
print(np.ptp(a, axis =  0))


# numpy.percentile(a, q, axis)
# 百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比。
'''
1.	a 输入数组
2.	q 要计算的百分位数，在 0 ~ 100 之间
3.	axis 沿着它计算百分位数的轴
'''
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.percentile(a,50))
print(np.percentile(a,50,axis=1))
print(np.percentile(a,50,axis=0))


# numpy.median()
# 中值定义为将数据样本的上半部分与下半部分分开的值。 numpy.median()函数的用法如下面的程序所示。
a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print(np.median(a))
print(np.median(a,axis=0))
print(np.median(a,axis=1))


# numpy.mean()
# 算术平均值是沿轴的元素的总和除以元素的数量。 numpy.mean()函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(np.mean(a))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))


# numpy.average()
# 加权平均值
# 考虑数组[1,2,3,4]和相应的权重[4,3,2,1]，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
# 加权平均值 = (1*4+2*3+3*2+4*1)/(4+3+2+1)
a = np.array([1,2,3,4])
# 不指定权重时相当于 mean 函数
print(np.average(a))
wts = np.array([4,3,2,1])
print(np.average(a,weights = wts))
# 如果 returned 参数设为 true，则返回权重的和
print(np.average(a,weights = wts,returned=True))
# 在多维数组中，可以指定用于计算的轴。
a = np.arange(6).reshape(3,2)
print(a)
wt = np.array([3,5])
print(np.average(a, axis=1, weights=wt))
print(np.average(a, axis=1, weights=wt,returned=True))


# 标准差
# 标准差是与均值的偏差的平方的平均值的平方根。
# std = sqrt(mean((x - x.mean())**2))
# 如果数组是[1，2，3，4]，则其平均值为2.5。 因此，差的平方是[2.25,0.25,0.25,2.25]，并且其平均值的平方根除以4，即sqrt(5/4)是1.1180339887498949。
print(np.std([1,2,3,4]))


# 方差
# 方差是偏差的平方的平均值，即mean((x - x.mean())** 2)。 换句话说，标准差是方差的平方根。
print(np.var([1,2,3,4]))



























