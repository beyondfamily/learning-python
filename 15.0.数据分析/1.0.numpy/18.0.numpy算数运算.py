import numpy as np
# numpy - 算数运算
a = np.arange(9, dtype = np.float_).reshape(3,3)
b = np.array([10,10,10])
print(a)
print(b)

# 两个数相加
print(np.add(a,b))
# 两个数相减
print(np.subtract(a,b))
# 两个数相乘
print(np.multiply(a,b))
# 两个数相除
print(np.divide(a,b))


# numpy.reciprocal()
# 此函数返回参数逐元素的倒数，。 由于 Python 处理整数除法的方式，对于绝对值大于 1 的整数元素，结果始终为 0， 对于整数 0，则发出溢出警告。
a = np.array([0.25,  1.33,  1,  200,  100])
print(np.reciprocal(a)) # !!!
b = np.array([100], dtype =  int)
print(np.reciprocal(b))


# numpy.power()
# 此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
a = np.array([10,100,1000])
print(np.power(a,2))
b = np.array([1,2,3])
print(np.power(a,b))


# numpy.mod()
# 此函数返回输入数组中相应元素的除法余数。 函数numpy.remainder()也产生相同的结果。
a = np.array([10,20,30])
b = np.array([3,5,7])
print(np.mod(a,b))
print(np.remainder(a,b))

# 以下函数用于对含有复数的数组执行操作。
# numpy.real() 返回复数类型参数的实部。
# numpy.imag() 返回复数类型参数的虚部。
# numpy.conj() 返回通过改变虚部的符号而获得的共轭复数。
# numpy.angle() 返回复数参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示。
a = np.array([-5.6j,  0.2j,  11.  ,  1+1j])
print(a)
print(np.real(a))
print(np.imag(a))
print(np.conj(a))
print(np.angle(a))
# 再次调用 angle() 函数（以角度制返回）
print(np.angle(a, deg =  True))





























