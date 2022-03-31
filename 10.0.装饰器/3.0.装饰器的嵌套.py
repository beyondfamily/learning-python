# 1.普通装饰器的定义
# 外函数
def outer(func):
    # 内函数
    def inner():
        print('找到门子，成功拿到微信 3')
        func() # 内函数中调用外函数的参数—函数
        print('约妹子，看电影 4')
    # 在外函数中返回内函数
    return inner

# 使用定义了一个装饰器
@outer
def love():
    print('跟妹子畅谈人生和理想')

love() # == inner()


# 2.再定义一个装饰器
def kuozhan(f):
    def kzinner():
        print('扩展1')
        f()
        print('扩展2')
    return kzinner

# 装饰器的嵌套 先执行下面的，再执行上面的
@kuozhan #2.再使用上面的 kuozhan装饰器 装饰 上一次返回的inner函数 又返回了kzinner函数
@outer   #1.先使用离得近的 outer装饰器 装饰love函数，返回了一个 inner函数 !!!  love=outer(love)
def love():
    print('跟妹子畅谈人生和理想 5')

love()

#1.先使用离得近的 outer装饰器 装饰love函数，返回了一个 inner函数 !!!  love=outer(love)
# 找到门子，成功拿到微信 3
# 跟妹子畅谈人生和理想 5
# 约妹子，看电影 4
#2.再使用上面的 kuozhan装饰器 装饰 上一次返回的inner函数 又返回了kzinner函数 !!! inner=kuozhan(inner)
# 扩展1
# 找到门子，成功拿到微信 3
# 跟妹子畅谈人生和理想 5
# 约妹子，看电影 4
# 扩展2

'''
扩展1
找到门子，成功拿到微信 3
跟妹子畅谈人生和理想 5
约妹子，看电影 4
扩展2

1.先使用离得近的 outer装饰器 装饰love函数，返回了一个 inner函数
2.再使用上面的 kuozhan装饰器 装饰 上一次返回的inner函数 又返回了kzinner函数

最后再调用love函数的时候是怎么执行的
    love()==kzinner()
             ===> 1
             ===> inner() 
                    ===> 3
                    ===> love() ===>5
                    ===> 4
             ===> 2

'''


