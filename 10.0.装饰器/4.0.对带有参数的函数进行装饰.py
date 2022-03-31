# 定义装饰

# 定义装饰
def outer(func):
    # 如果装饰器带有参数的函数，需要在内函数中定义行参，并传递给调用的函数
    # 因为调用原函数等于调用内函数
    def inner(var):
        print(f'找到{var}妹子，成功拿到微信。。。')
        func(var)
        print(f'约{var}妹子，看一场午夜电影。。。')
    return inner

# 有参数的函数
@outer   # love=outer(love)
def love(name):
    print(f'跟{name}妹子畅谈人生...')

love('思思') # love() ==> inner() love('思思')==>inner('思思')



