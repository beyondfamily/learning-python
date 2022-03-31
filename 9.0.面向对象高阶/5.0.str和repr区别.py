num=521
r1=str(num)
r2=repr(num)

# str和repr函数都可以把其他类型的值转化为字符串
print(r1,type(r1)) # 521 <class 'str'>
print(r2,type(r2)) # 521 <class 'str'>


s='521'
s2="511"
r1=str(s)
r2=repr(s)
r3=repr(s2)

# repr解析的结果带了单引号
print(r1,type(r1)) # 521 <class 'str'>
print(r2,type(r2)) # '521' <class 'str'>
print(r3,type(r3)) # '511' <class 'str'>

'''
str和repr函数都能把其他类型的数据转化为字符串类型
str函数会把对象 转化为 更适合人类阅读的形式
repr函数会把对象 转化为 解释器读取的形式

如果数据对象没有更明显的区别的化，str和repr结果是一样的
'''



