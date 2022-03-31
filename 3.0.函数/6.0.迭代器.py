'''
python最具有特色的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住访问遍历的位置的对象
从集合的第一个元素开始访问，直到集合中所以的元素被访问完毕
迭代器只能从前往后一个一个的遍历，不能后退
能别next()函数调用，并不断返回下一个值的对象称为迭代器
'''

# range(10) 0--9  #返回一个可迭代的对象
# range(2,10) 2--9
# range(10,3,-1) 10--4 左开右闭

arr = ['a', 'b', 'c', 4, 5]
for i in arr:
    print(i, end=' ')

'''
iter()
   功能：把可迭代的对象，转化为一个迭代器对象
   参数：可迭代的对象（str,list,tuple,dict,set,range...)
   返回值：迭代器对象
注意：迭代器一定是一个可以迭代的对象，但是可迭代对象不一定是迭代器
'''

# 定义一个列表，是一个可迭代对象    能被for遍历的为可迭代对象
f1 = ['a', 'b', 'c', 'd']
# 把可迭代对象转化为迭代器使用
res = iter(f1)
print(res, type(res))
r = next(res)
print(r)
r = next(res)
print(r)
r = next(res)
print(r)
r = next(res)
print(r)
r = list(res)  # 全部取出来了，res就空了 迭代对象取出来就没了
print(r)

'''迭代器的取值方案
1. next() 调用一次获取一次，直到数据被取完
2. list() 使用list函数直接取出迭代器中的所有数据
3. for    使用for循环遍历迭代器的数据
迭代器取值的特点，取出一个少一个，直到都取完，最后再获取就会报错
'''

# 检测迭代器和可迭代对象的方法
from collections.abc import Iterator, Iterable

varstr = '123456'
res = iter(varstr)
# isinstance() 判断子类是否是一种父类类型，考虑继承关系
print(isinstance(varstr,Iterable)) # 是可迭代的对象
print(isinstance(varstr,Iterator)) # 不是迭代器
print(isinstance(res,Iterable))    # 是可迭代的对象
print(isinstance(res,Iterator))    # 是迭代器

