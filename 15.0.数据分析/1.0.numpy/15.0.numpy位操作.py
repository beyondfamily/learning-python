import numpy as np
'''
1.	bitwise_and 对数组元素执行位与操作
2.	bitwise_or 对数组元素执行位或操作
3.	invert 计算位非
4.	left_shift 向左移动二进制表示的位
5.	right_shift 向右移动二进制表示的位
'''

# 通过np.bitwise_and()函数对输入数组中的整数的二进制表示的相应位执行位与运算。
a,b = 13,17
print(bin(a),bin(b))
# '13 和 17 的位与：'
print(np.bitwise_and(13, 17))

# 通过np.bitwise_or()函数对输入数组中的整数的二进制表示的相应位执行位或运算。
print(np.bitwise_or(13, 17))

# invert
# 此函数计算输入数组中整数的位非结果。 对于有符号整数，返回补码。
# 例：求-5的补码。
# -5对应带符号位负数5（10000101）→除符号位外所有位取反（11111010）→加 00000001为 (11111011)
# +9的补码是00001001

# '13 的位反转，其中 ndarray 的 dtype 是 uint8：'
print(np.invert(np.array([13], dtype = np.uint8)))
# '13 的二进制表示：'
print(np.binary_repr(13, width = 8))
# '242 的二进制表示：'
print(np.binary_repr(242, width = 8))


# numpy.left shift()函数将数组元素的二进制表示中的位向左移动到指定位置，右侧附加相等数量的 0。
# '将 10 左移两位：'
print(np.left_shift(10,2))
print(np.binary_repr(10, width = 8))
print(np.binary_repr(40, width = 8))


# numpy.right_shift()函数将数组元素的二进制表示中的位向右移动到指定位置，左侧附加相等数量的 0。
# '将 40 右移两位：'
print(np.right_shift(40,2))
print(np.binary_repr(40, width = 8))
print(np.binary_repr(10, width = 8))







