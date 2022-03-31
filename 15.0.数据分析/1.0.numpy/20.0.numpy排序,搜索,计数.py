import numpy as np

# NumPy中提供了各种排序相关功能。
'''
         种类	       速度	 最坏情况	工作空间	稳定性
'quicksort'（快速排序）	1	O(n^2)	     0	    否
'mergesort'（归并排序）	2	O(n*log(n))	 ~n/2	是
'heapsort'（堆排序）	    3	O(n*log(n))	 0	    否
'''

# numpy.sort(a, axis, kind, order)
'''
1.	a 要排序的数组
2.	axis 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
3.	kind 默认为'quicksort'（快速排序）
4.	order 如果数组包含字段，则是要排序的字段
'''

a = np.array([[3,7],[9,1]])
print(np.sort(a))
# 沿轴 0 排序
print(np.sort(a,axis=0))
# 在 sort 函数中排序字段
dt = np.dtype([('name',  'S10'),('age',  int)])
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print(np.sort(a, order ='name'))


# numpy.argsort()
# numpy.argsort()函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。
x = np.array([3,  1,  2])
y = np.argsort(x)
print(y)
# 以排序后的顺序重构原数组
print(x[y])


# numpy.lexsort()
# 函数使用键序列执行间接排序。
# 键可以看作是电子表格中的一列。 该函数返回一个索引数组，使用它可以获得排序数据。
# 注意，最后一个键恰好是 sort 的主键。
nm =('raju','anil','ravi','amar')
dv =('f.y.',  's.y.',  's.y.',  'f.y.')
ind = np.lexsort((dv,nm))
print(ind)
print([nm[i]  +  ", "  + dv[i]  for i in ind])


# numpy.argmax() 和 numpy.argmin()
# 这两个函数分别沿给定轴返回最大和最小元素的索引。
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print(np.argmax(a))
# 展开数组
print(a.flatten())
# 沿轴 0 的最大值索引：
print(np.argmax(a, axis=0))
# 沿轴 1 的最大值索引
print(np.argmax(a, axis=1))
minindex = np.argmin(a)
print(a.flatten()[minindex])


# numpy.nonzero()函数返回输入数组中非零元素的索引。
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print(np.nonzero(a))


# numpy.where()
# where()函数返回输入数组中满足给定条件的元素的索引。
x = np.arange(9.).reshape(3,  3)
y = np.where(x >  3)
print(x[y])


# numpy.extract()
# extract()函数返回满足任何条件的元素。
x = np.arange(9.).reshape(3,  3)
print(x)
condition = np.mod(x,2)  ==  0
print(np.extract(condition, x))














