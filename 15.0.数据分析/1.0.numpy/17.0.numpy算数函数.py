import numpy as np
a = np.array([0,30,45,60,90])
# 正弦
print(np.sin(a*np.pi/180))
# 余弦
print(np.cos(a*np.pi/180))
# 正切
print(np.tan(a*np.pi/180))


# 含有正弦值的数组
a = np.array([0,30,45,60,90])
sin = np.sin(a*np.pi/180)
# 计算角度的反正弦，返回值以弧度为单位：
inv = np.arcsin(sin)
print(inv)


# 舍入函数
# numpy.around(a,decimals)
'''
1.	a 输入数组
2.	decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
'''
a = np.array([1.0,5.55,  123,  0.567,  25.532])
print(a)
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))


# numpy.floor()
# 此函数返回不大于输入参数的最大整数。 即标量x 的下限是最大的整数i ，使得i <= x。 注意在Python中，向下取整总是从 0 舍入。
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(a)
print(np.floor(a))


# numpy.ceil()
# ceil()函数返回输入值的上限，即，标量x的上限是最小的整数i ，使得i> = x。
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(a)
print(np.ceil(a))
















