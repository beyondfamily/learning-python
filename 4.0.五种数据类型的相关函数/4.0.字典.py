# **是字典解包，这个*是列表解包
# 把arr的内容分解，作为参数传递给zip，至于arr是几阶，影响不大
# 字典的定义
'''
+ 字典可以通过将以逗号分隔的 '键: 值' 对列表包含于花括号之内来创建字典
+ 也可以通过 [`dict`] 构造器来创建
{'jack': 4098, 'sjoerd': 4127}` 或 `{4098: 'jack', 4127: 'sjoerd'}

# 1.使用{}定义
vardict = {'a':1,'b':2,'c':2}

# 2.使用 dict(key=value,key=value) 函数进行定义
vardict = dict(name='zhangsan',sex='男',age=22)

# 3.数据类型的转换  dict(二级容器类型) 列表或元组，并且是二级容易才可以转换
vardict = dict([['a',1],['b',2],['c',3]])  # {'a': 1, 'b': 2, 'c': 3}

# 4.zip压缩函数，dict转类型
var1 = [1,2,3,4]
var2 = ['a','b','c','d']
# 转换的原理和上面的第三种 是一个原理
vardict = dict(zip(var1,var2))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(vardict)
'''


# 字典的操作
'''
var1 = {'a': 1, 'b': 2, 'c': 3}
var2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# res = var1 +  var2 # XXXX  TypeError
# res = var1 * 3 # xxxx TypeError

# 获取元素
res = var1['a']

# 修改元素
res = var1['a'] = 111

# 删除元素
del var1['a']

# 添加元素
var1['aa'] = 'AA' #{'a': 1, 'b': 2, 'c': 3, 'aa': 'AA'}

# 如果字典中的key重复了，会被覆盖
# var1['a'] = 'aa'
'''


# 成员检测和获取
'''
var1 = {'a': 1, 'b': 2, 'c': 3}
# 成员检测和获取,只能检测key，不能检测value
res = 'AA' in var1   #为True或False
res = 'AA' not in var1

# 获取当前字典的长度 只能检测当前有多少个键值对
res = len(var1)

# 获取当前字典中的所有 key 键
res = var1.keys() #dict_keys(['a', 'b', 'c'])
print(list(res))

# 获取字典中所有的 value 值
res = var1.values()#dict_values([1, 2, 3])

# 获取当前字典中所有 键值对
res = var1.items()#dict_items([('a', 1), ('b', 2), ('c', 3)])
'''


# 字典的遍历
'''
var1 = {'a': 1, 'b': 2, 'c': 3}
# 1.0.在遍历当前的字典时，只能获取当前的key
for i in var1:
    print(i,end=' ') # 只能获取 key
    print(var1[i],end=' ') # 通过字典的key获取对应value
    # a 1 b 2 c 3 

# 2.0.遍历字典时，使用 items() 函数，可以在遍历中获取key和value
for k,v in var1.items():
    print(k)  # 遍历时的 key
    print(v)  # 遍历时的 value  

# 3.0.遍历字典的所有key
for k in var1.keys():
    print(k) 

# 4.0.遍历字典的所有 value
for v in var1.values():
    print(v)
'''


# 字典的相关函数
'''
# len(dict) #获取字典的键值对个数
# dict.keys() # 获取当前字典的所有key 键，组成的列表
# dict.values() # 获取当前字典的所有 value 值，组成的列表
# dict.items() # 返回由字典项 ((键, 值) 对) 组成的一个新视图
# iter(dict) 返回以字典的键为元素的迭代器。

vardict = {'a':1,'b':2,'c':3}

# 通过 key 从当前字典中弹出键值对  删除
# res = vardict.pop('a')
# print(res) #1
# print(vardict) #{'b': 2, 'c': 3}

# LIFO: Last in, First out.后进先出
# res = vardict.popitem()  # 把最后加入到字典中的键值对删除并返回一个元组
# print(res)#('c', 3)
# print(vardict)#{'a': 1, 'b': 2}

# 使用key获取字典中不存在元素，会报错
# print(vardict['aa'])#KeyError: 'aa'
# 可以使用get获取一个元素，存在则返回，不存在默认返回None
# res = vardict.get('aa') #None
# res = vardict.get('a','c') #1  只会读取第一个‘a’，不会读取‘c’

# dict.update(),更新字典,如果key存在，则更新，对应的key不存在则添加
# vardict.update(a=11,b=22)  #具体的颜色会变，注意看颜色就行了
# var1.update({'a':33,'d':44})
# print(vardict) # {'a': 33, 'b': 2, 'c': 3, 'd': 44}

# dict.setdefault(key，value)
# 如果字典存在键 key ，返回它的值。
# 如果不存在，插入值为 default 的键 key ，并返回 default 。
# default 默认为 None。

vardict = {'a':1,'b':2,'c':3}
vardict.setdefault('a',123)
print(vardict) # {'a': 1, 'b': 2, 'c': 3}
vardict.setdefault('aa')
print(vardict) # {'a': 1, 'b': 2, 'c': 3, 'aa': None}
vardict.setdefault('bb',123)
print(vardict) # {'a': 1, 'b': 2, 'c': 3, 'aa': None, 'bb': 123}
---------------------
其实如果key在字典中不存在，setdefault(key,value)方法与dict[key] = value形式是完全一样的，区别就是当key在字典中存在的情况下。
setdefault(key,value)并不会改变原值，而dict[key] = value是会改变原值的。
所以setdefault方法主要用于向字典中添加一个key-value对，而不是修改key对应的值。
---------------------
'''


# 字典推导式
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 字典推导式格式 : {key:value for循环 if判断}
# (1)把字典中的键值对位置进行交换 {'a':1,'b':2,'c':3}
vardict = {'a':1,'b':2,'c':3}

# 1.0.普通方法实现 字典中的键值交换
newdict = {}
for k,v in vardict.items():
    newdict[v] = k
print(newdict)
# 2.0.使用字典推导式完成
newdict = {v:k for k,v in vardict.items()}
print(newdict)

# 注意：以下推导式，返回的结果是一个集合，集合推导式
newdict = {v for k,v in vardict.items()}  # 因为就只返回了一个v
print(newdict,type(newdict))   #关键在于  key:value

# (2)把以下字典中的是偶数的值，保留下来，并且交换键值对的位置
vardict = {'a':1,'b':2,'c':3,'d':4}

# 1.0.普通方式完成  {2: 'b', 4: 'd'}
newdict = {}
for k,v in vardict.items():
    if v % 2 == 0:
        newdict[v] = k
print(newdict)


# 2.0.字典推导式完成  {2: 'b', 4: 'd'}
newdict = {v:k for k,v in vardict.items() if v % 2 == 0}
print(newdict)



