# 1.装饰器的原型
# 利用闭包，把函数当做参数传递，并且在函数内去调用传递进来的函数，并返回一个函数

# 定义外函数,接收一个函数作为参数
def outer(f):
    # 定义内函数，并且在内函数中调用了外函数的参数

    def inner1():
        print('我是外函数中内函数1')
        f()
        print('我是外函数中内函数2')
    return inner1



# 定义普通函数
def old():
    print('我是一个普通函数')

# old() # 作为普通函数直接调用
a=outer(old) # outer返回了inner函数，赋值给了old  不需要待括号
a()          # 此时再调用old函数是，等同意调用了inner函数

print('='*80)

# 改为装饰器用法
@outer  # 此处使用的@outer的语法就是把outer作为了装饰器，等同于 old=outer(old)
def old():
    print('我是一个普通函数')

old() # old函数经过了 outer装饰器进行了装饰，代码和调用方法不变，但是函数的功能发生了改变





