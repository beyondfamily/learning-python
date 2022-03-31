# 回调函数
# 定义一个函数,函数中的参数要求是另一个函数
# def func(f):
#     print(f, type(f))
#     f()  # 并且在函数中调用了传递进来的行参函数
#
# def love():
#     print('123')
# func(love)


# 闭包函数
# 在一个函数内返回了一个内函数，并且这个返回的内函数还使用了外函数中的局部变量
money = 0


# 工作
def work():
    global money
    money += 100


# 加班
def overwork():
    global money
    money += 200


# 购物
def buy():
    global money
    money -= 50


work()
work()
work()
overwork()
buy()
# 银行垮台了，没钱了。。。 外部可以轻易影响
money = 0
work()
print(money)


# 对程序进行改造

def person():
    money = 0

    # 工作  在外函数中定义的内函数
    def work():
        nonlocal money  # 在内函数中使用了外函数的临时变量
        money += 100
        print(money)

    # 在外函数中返回了内函数，这个内函数就是闭包函数
    return work


res = person()  # return work res=work
res()
res()


# 此时 就不能够在全局变量中对money这个变量进行影响
# 闭包的作用：保护了函数中的变量不受外部的影响，但又是能够使用


# 匿名函数 lambda 表达式
# 语法：lambda [参数列表]：返回值
# 封装一个函数加法运算
# 1.0.普通函数
def jia(x, y):
    return x + y


print(jia(2, 3))

# 2.0.lambda表达试
res = lambda x, y: x + y
print(res(5, 7))

# 3.0.带有分支结构的lambda表达式
# lambda 参数列表：真区间 if 表达式判断 else 假区间
res1 = lambda sex: '很man' if sex == '男' else '很nice'  # 注意只能用else不能用elif
print(res1('女'))
