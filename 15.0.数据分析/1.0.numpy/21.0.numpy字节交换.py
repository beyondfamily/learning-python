import numpy as np
# 我们已经看到，存储在计算机内存中的数据取决于 CPU 使用的架构。 它可以是小端（最小有效位存储在最小地址中）或大端（最小有效字节存储在最大地址中）。


# numpy.ndarray.byteswap()函数在两个表示：大端和小端之间切换。
a = np.array([1,  256,  8755], dtype = np.int16)
print(a)
# 以十六进制表示内存中的数据：
print(map(hex,a))
# byteswap() 函数通过传入 true 来原地交换
print(a.byteswap(True))
# 十六进制形式：
print(map(hex,a))


