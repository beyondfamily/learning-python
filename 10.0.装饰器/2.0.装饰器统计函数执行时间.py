
import time

# 定义一个统计函数执行时间的 装饰器
def runtime(f):
    def inner():
        start=time.perf_counter()
        f()
        end=time.perf_counter()-start
        print(f'函数的调用执行时间为：{end}')
    return inner

# 定义一个函数
@runtime  #此处使用的@runtime的语法就是把runtime作为了装饰器，等同于 func=runtime(func)
def func():
    for i in range(10):
        print(i,end=' ')
        time.sleep(0.5)

