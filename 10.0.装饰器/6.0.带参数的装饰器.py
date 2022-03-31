# 如果你的装饰器需要有参数，那么给当前的装饰器套一个壳，用于接收装饰器的参数
def kuozhan(var):
    def outer(func):
        def inner1():
            print('妹子给你了微信')
            func()
        def inner2():
            print('妹子给你介绍了个大妈')
            func()


        # 装饰器壳的参数，可以用于在函数内去做流程控制

        if var=='高富帅':
            return inner1
        else:
            return inner2
    return outer

@kuozhan('高富帅') # love1=outer(love1) outer同时接收了'高富帅'
def love1():
    print('谈谈人生。。。')
love1()

@kuozhan('煞笔') # love2=outer(love1) outer同时接收了'煞笔'
def love2():
    print('谈谈人生。。。')
love2()
