# 普通参数，默认参数，收集参数，命名关键字参数，关键字参数收集
# 普通参数 就是位置参数，也叫顺序参数，也是必须传递的参数

# 默认参数
# def funa(x,y):
#     print(x,y)
# funa(1,2)
#
# def funb(x,y,i=100):#设置默认值
#     print(x,y,i)
#
# funb(1,2,3)
# funb(1,2)#掉用时未传递参数使用默认参数

# 收集参数
# 定义一个行参，专门收集多余的实参
# 接收到的多余的函数，会储存在args中，形成一个元组
def func(x='+', *args):  # *args不是固定的格式  重要的是args前面的*
    # print(args,type(args)) # (100, 200, 300) <class 'tuple'>
    if x == '+':
        print('加法运算', sum(args))
    else:
        print('减法运算', args)


func('+', 100, 200, 300)


def func2(x='+', *a):
    if x == '+':
        print('加法运算', sum(a))
    else:
        print('减法运算', a)


func2('+', 100, 200, 300)


# 命名关键字参数
def love(a, b, c=3, *args, name):
    print(a, b, c)
    print(args)
    print(name)


love(1, 2, 2, 4, 5, 6, 7, 8, 9, name='admin')

# 关键字参数收集 kw==keyword

# def love(a, b, c=3, *args, name, age, **kwargs):
#     print(a, b, c)
#     print(args)  # 普通收集参数会把多余的参数收集成为 元组
#     print(name, age)
#     print(kwargs)  # 关键字参数，会把多余的关键字参数收集为字典
# love(1, 2, 3, 112.123, name='aaa', age=222, sex='ccc', aa='aa', bb='bb')

# 函数的返回值
# 在一个函数中，可以返回一下内容，也可以不返回
# 没有返回值的函数，或者理解为，没有知道返回内容
# def love(a, b):
#     print(f'{a} i love you {b}')

# 如果需要在函数中知道返回内容，可以使用return 关键字
# def love(a, b):
#     res = f'{a} i love you {b}'
#     return res
#
# r = love('a', 'b')
# print(r)

'''
函数可以分为两类
    1。执行过程函数： 函数体内完成一定的功能既可，没有返回值
    2。具有返回值的函数： 函数体内完成一定的功能，并且返回一个结果到函数调用处
'''

# num=10
# def func():
#     print(num) #在函数内可以获取函数外部的变量
#     num+=10 #在函数内不能直接更改函数外的变量


# 在函数外定义的变量，在函数内也可以更改
varlist = [1, 2, 3]
vardict = {'a': 'a', 'b': 'b'}
live = '666'


def func():
    varlist[2] = 'aa'
    vardict['a'] = 'aa'
    global live  # global还有引用全局变量 并可以更改
    print('1-'+live)
    live = 'iloveyou'
    print('2-'+live)

func()  # 666
print(varlist)
print(vardict)
print(live)#函数内定义的全局变量

#在函数内定义的函数，称为局部函数，函数外无法使用
#在内函数中如何使用上一层函数中的局部变量？

#定义一个外层函数
def outer():
    num=10
    #内函数，局部函数，在函数内部定义的函数
    def inner():
        nonlocal num  # 可以引用上一层函数中定义的局部变量，但依然不能提升为全局变量
        num+=1
        print(num)
    inner()
    print(num)

outer()
