import numpy as np


dt = np.dtype(np.int32)
print(dt)


#int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
dt = np.dtype('i8')
print(dt)


# 使用端记号
dt = np.dtype('>i4')
print(dt)


# 首先创建结构化数据类型
dt = np.dtype([('age',np.int8)])
print(dt)


# 现在将其应用于 ndarray 对象
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)


dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])


# 以下示例定义名为 student 的结构化数据类型，其中包含字符串字段name，整数字段age和浮点字段marks。 此dtype应用于ndarray对象
student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])
print(student)


student = np.dtype([('name','S20'),  ('age',  'v1'),  ('marks',  'f4')])
a = np.array([('abc',  21,  50),('xyz',  18,  75)], dtype = student)
print(a)
print(a['name'])
print(a['age'])

'''
每个内建类型都有一个唯一定义它的字符代码：
'b'：布尔值

'i'：符号整数

'u'：无符号整数

'f'：浮点

'c'：复数浮点

'm'：时间间隔

'M'：日期时间

'O'：Python 对象

'S', 'a'：字节串

'U'：Unicode

'V'：原始数据（void）
'''








