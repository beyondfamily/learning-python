import numpy as np
# nditer类的构造器拥有flags参数，它可以接受下列值
'''
1.	c_index 可以跟踪 C 顺序的索引
2.	f_index 可以跟踪 Fortran 顺序的索引
3.	multi-index 每次迭代可以跟踪一种索引类型
4.	external_loop 给出的值是具有多个值的一维数组，而不是零维数组
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a)
for x in np.nditer(a, flags =['external_loop'], order='F'):
    print(x)

for x in np.nditer(a, flags =['c_index'], order='F'):
    print(x)

for x in np.nditer(a, flags =['f_index'], order='F'):
    print(x)


















