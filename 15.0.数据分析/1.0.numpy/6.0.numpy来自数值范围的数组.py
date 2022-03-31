import numpy as np

# numpy.arange
# 这个函数返回ndarray对象，包含给定范围内的等间隔值。
# numpy.arange(start, stop, step, dtype)
'''
1.	start 范围的起始值，默认为0
2.	stop 范围的终止值（不包含）
3.	step 两个值的间隔，默认为1
4.	dtype 返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
'''

x = np.arange(5)
print(x)


# 设置了 dtype
x = np.arange(5, dtype =  float)
print(x)


# 设置了起始值和终止值参数
x = np.arange(10,20,2)
print(x)


# numpy.linspace
# 此函数类似于arange()函数。 在此函数中，指定了范围之间的均匀间隔数量，而不是步长。 此函数的用法如下。
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
'''
1.	start 序列的起始值
2.	stop 序列的终止值，如果endpoint为true，该值包含于序列中
3.	num 要生成的等间隔样例数量，默认为50
4.	endpoint 序列中是否包含stop值，默认为ture
5.	retstep 如果为true，返回样例，以及连续数字之间的步长
6.	dtype 输出ndarray的数据类型
'''

x = np.linspace(10,20,5)
print(x)

# 序列中不包含stop值
x = np.linspace(10,20,  5, endpoint =  False)
print(x)


x = np.linspace(1,2,5, retstep =  True)
print(x)


# numpy.logspace
# 此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10。
# numpy.logscale(start, stop, num, endpoint, base, dtype)
'''
1.	start 起始值是base ** start
2.	stop 终止值是base ** stop
3.	num 范围内的数值数量，默认为50
4.	endpoint 如果为true，终止值包含在输出数组当中
5.	base 对数空间的底数，默认为10
6.	dtype 输出数组的数据类型，如果没有提供，则取决于其它参数
'''
a = np.logspace(1.0,2.0,num=10)
print(a)


a = np.logspace(1,10,num =  10,  base  =  3,dtype=int)
print(a)
