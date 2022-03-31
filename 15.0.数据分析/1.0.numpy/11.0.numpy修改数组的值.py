import numpy as np
# nditer对象有另一个可选参数op_flags。 其默认值为只读，但可以设置为读写或只写模式。 这将允许使用此迭代器修改数组元素。

a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=x*2
print(a)




