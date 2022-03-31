from functools import reduce

# range()函数
'''
功能：能够生成一个指定的数字序列
参数：
    start : 开始的值 ，默认值为0
    stop  ： 结束的值
    [, step]： 可选，步进值 默认值为1
返回值： 可迭代的对象，数字序列
  左闭右开
  res = range(10,0,-1) #这样也是左闭右开
# 三个参数， 参数1是开始值，参数2是结束值，参数三是步进值
'''
# 提取range()函数返回的数字序列的方法：
'''
# 1。转为list列表数据
# print(list(res))

# 2。通过 for循环 进行遍历
# for i in res:
#     print(i)

# 3。转为迭代器，使用next函数调用
# res = iter(res)
# print(next(res))
# print(next(res))
'''

# zip() 函数
'''
功能：zip 函数是可以接受多个可迭代的对象，然后把每个可迭代对象中的第i个元素组合在一起，形成一个新的迭代器
参数：*iterables，任意个的 可迭代对象
返回值： 返回一个元组的迭代器
例：
  var1 = '1234'
  var2 = ['a','b','c','d']
  var3 = ('A','B','C','D')
  res = zip(var1,var2,var3)
  print(list(res)) # [('1', 'a', 'A'), ('2', 'b', 'B'), ('3', 'c', 'C'), ('4', 'd', 'D')]
  for i in res:
    print(i)

  ('1', 'a', 'A')
  ('2', 'b', 'B')
  ('3', 'c', 'C')
  ('4', 'd', 'D') 

# zip() 与 * 运算符相结合可以用来拆解一个列表:
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
zipped = zip(x, y, z)
print(list(zipped))#[(1, 4, 7), (2, 5, 8), (3, 6, 9)] # 获取x，y，z，的[0]组成新的元组

print(zip(x, y, z))  # 迭代器对象，
print(*zip(x, y, z))  # 组合好的多个元组数据(1, 4, 7) (2, 5, 8) (3, 6, 9) 

'''


# 其他内置函数
'''
+ int() 将其它类型数据转为整型
+ float() 转为浮点类型
+ bool() 转为布尔类型
+ complex() 转为复数
+ str() 转为字符串类型
+ list 转为列表类型
+ tuple 转为元组类型
+ dict 转为字典类型
+ set 转为集合类型


+ id()    获取当前数据的ID标识
+ type()  获取当前数据的类型字符串
+ print() 数据的打印
+ input() 获取输入的数据
+ isinstance() 检测是否为指定的数据类型
'''


# 数学相关函数
'''
# 获取一个数的绝对值
# print(abs(-99.99))

# 求和 从 start 开始自左向右对 iterable 中的项求和并返回总计值
# print(sum([1,2,3]))

# 获取最大值
# print(max([1,2,3]))
# print(max(99,12,45))

# 获取最小值
# print(min([2,1,6,-9]))
# print(min(6,7,1,0,-2))

# 幂运算  返回 x 的 y 次幂
# print(pow(2,3))

# 四舍五入
# r = round(3.1415926)
# r = round(3.1415926,2) # 小数点保留几位

# r = round(4.5) # 奇进偶退  1.5 = 2,2.5=2,3.5=4,4.5=4 整数另外算
# print(r)
'''


# Ascii相关的函数
'''
# 将字符转为 ascii
r = ord('a')
print(r)

# 将ascii转为字符
r = chr(65)
print(r)
'''


# 高阶函数
# sorted()
'''
sorted(iterable,[reverse,key])
sorted()
运行原理：
    把可迭代数据里面的元素，一个一个的取出来，放到key这个函数中进行处理，
    并按照函数中return的结果进行排序，返回一个新的列表
功能： 排序
参数：
    iterable 可迭代的数据 （容器类型数据，range数据序列，迭代器）
    reverse  可选，是否反转，默认为False，不反转， True反转
    key      可选， 函数，可以是自定义函数，也可以是内置函数
返回值： 排序后的结果
'''


# 默认按照从小到大的方式进行排序
arr = [3,7,1,-9,20,10]
res = sorted(arr)  # [-9, 1, 3, 7, 10, 20]
print(res)

# 可以按照从大到小的方式进行排序
res = sorted(arr,reverse=True)  # [20, 10, 7, 3, 1, -9]
print(res)

# 使用abs这个函数(求绝对值）作为sorted的key关键字参数使用
res = sorted(arr,key=abs)
print(res)

res = sorted(arr,key=abs,reverse=True)
print(res) # [20, 10, -9, 7, 3, 1]

# 使用自定义函数
def func(num):
    return num % 2
arr = [3,2,4,6,5,7,9]
res = sorted(arr,key=func)
print(res)

# 优化版
arr = [3,2,4,6,5,7,9]
res = sorted(arr,key=lambda x:x%2)
print(res) # [2, 4, 6, 3, 5, 7, 9]

res = sorted(arr,key=lambda x:x%2,reverse=True)
print(res) # [3, 5, 7, 9, 2, 4, 6]


# map()
'''
对传入的可迭代数据中的每个元素进行处理，返回一个新的迭代器
map(func, *iterables)
功能： 对传入的可迭代数据中的每个元素放入到函数中进行处理，返回一个新的迭代器
参数：
    func 函数  自定义函数|内置函数
    iterables：可迭代的数据
返回值：迭代器
'''
# (1)把一个字符串数字的列表转为 整型的数字列表
# ['1','2','3','4']  # ==> [1,2,3,4]
# 1.0.普通的处理方法
varlist = ['1','2','3','4']  # ==> [1,2,3,4]
newlist = []
for i in varlist:
    newlist.append(int(i))
print(newlist)

# 2.0.使用map函数进行处理
varlist = ['1','2','3','4']
res = map(int,varlist) # <map object at 0x104ea8890>
print(list(res))

# (2) [1,2,3,4] ==> [1,4,9,16]
# 1.0.普通方法
varlist = [1,2,3,4]
newlist = []
for i in varlist:
    res = i ** 2
    newlist.append(res)
print(newlist)

# 2.0.使用map函数处理这个数据
varlist = [1,2,3,4]
def myfunc(x):
    return x ** 2
res = map(myfunc,varlist)
print(res,list(res))

# 3.0.优化版
res = map(lambda x:x**2,varlist)
print(res,list(res))


# (3) ['a','b','c','d'] ==> [65,66,67,68]
var=['a','b','c','d']
newvar=map(lambda x:str(ord(x)-32),var)
print(list(newvar))


# reduce()
'''
reduce(func,iterable)
功能：
    每一次从 iterable 拿出两个元素，放入到func函数中进行处理，得出一个计算结果，
    然后把这个计算结果和iterable中的第三个元素，放入到func函数中继续运算，
    得出的结果和之后的第四个元素，加入到func函数中进行处理，以此类推，直到最后的元素都参与了运算
参数：
    func： 内置函数或自定义函数
    iterable： 可迭代的数据
返回值：最终的运算处理结果
注意： 使用 reduce函数时，需要导入 from functools import reduce
'''
# (1)[5,2,1,1] ==> 5211

# 1.0.普通方法
varlist = [5,2,1,1]
res = ''
for i in varlist:
    res += str(i)
res = int(res)
print(res)

# 2.0.使用reduce完成
def myfunc(x,y):
    return x*10+y
varlist = [5,2,1,1]
res = reduce(myfunc,varlist)
print(res,type(res))

#  (2)把字符串的 '456' ==> 456
#  要求不能使用int方法进行类型的转换时，如何解决上面的问题

# 定义函数，给定一个字符串的数字，返回一个整型的数字
def myfunc(s):
    vardict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return vardict[s]

# 1.先使用 map函数，把数字字符串，转为整型的数字
iter1 = map(myfunc,'456') #是一个一个读取的  可迭代的数据 ‘456’再迭代器中‘4’ ‘5’ ‘6’ 所以是一个一个读取

# 2. 把数字列表中的值，使用lambda进行二次处理
iter2 = reduce(lambda x,y:x*10+y,iter1)
# iter2 = reduce(lambda x,y:int(x)*10+int(y),'456')
print(iter2)


# filter()
'''
filter(func,iterable)
功能： 过滤数据，把 iterable 中的每个元素拿到 func 函数中进行处理，
        如果函数返回True则保留这个数据，返回False则丢弃这个数据
参数：
    func  自定义函数
    itereble： 可迭代的数据
返回值：保留下来的数据组成的 迭代器
'''

# (1)保留所有的偶数，丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9]

# 1.0.普通方法实现
newlist = []
for i in varlist:
    if i % 2 == 0:
        newlist.append(i)
print(newlist)

# 2.0.使用 filter 进行处理
def myfunc(n):
    if n % 2 == 0:
        return True
    else:
        return False
it = filter(myfunc,varlist)
print(it,list(it))

# 3.0.优化版
it = filter(lambda n:True if n % 2 == 0 else False,varlist)
print(it,list(it))




