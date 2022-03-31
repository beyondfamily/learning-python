'''
在当前脚本中，同一个类只能实例化一个对象，去使用

实例单例的案例：
单例和婚姻的关系，特别像，一个人只能有一个结婚对象
在社会中如何完成一夫一妻制呢？
如果要结婚，必须到 民政局去登记
民政局 需要检测两个人的户口本 看上面是否属于 结婚状态
如果已婚 肯定是出去了
如果没有结婚 可以盖个章 开始登记

那么按照这个思路

1.需要有一个方法，可以去控制当前对象的创建
    析构方法__new__
2.需要有一个标识来存储和表示是否有对象
    创建一个属性，进行存储，默认值为None
3.在创建对象的方法中去检测和判断是否有对象？
    如果没有对象，则创建对象，并且把对象存储起来
    如果存储的是对象，则直接返回对象，就不需要创建新的对象了

'''
class Demo():
    # 2.定义私有属性存储对象，默认值为None
    __obj = None

    # 1.定义构造方法
    # cls是把类给传进来而不是把对象传进来
    def __new__(cls, *args, **kwargs):
        # 3.在创建对象的过程中，判断是否有对象
        if cls.__obj:
            # 就证明有对象
            return cls.__obj
        else:
            # 如果没有对象，则创建对象，并存储起来
            obj = object.__new__(cls)
            # 并且存储起来
            cls.__obj = obj
            # 返回对象
            return obj

class Demo2():
    # 2.定义私有属性存储对象，默认值为None
    __obj = None

    # 1.定义构造方法
    # cls是把类给传进来而不是把对象传进来
    def __new__(cls, *args, **kwargs):
        # 3.在创建对象的过程中，判断是否有对象
        if cls.__obj:
            # 就证明有对象
            return cls.__obj
        else:
            # 如果没有对象，则创建对象，并存储起来
            obj = object.__new__(cls)
            # 并且存储起来
            cls.__obj = obj
            # 返回对象
            return obj

# 实例化对象 只会在第一次创建对象
a=Demo() # <__main__.Demo object at 0x0000020BE2485D90>
b=Demo() # <__main__.Demo object at 0x0000020BE2485D90>
print(a,b)

class demo2():
    pass

a1=demo2() # <__main__.demo2 object at 0x000001D7EBC5F190>
b2=demo2() # <__main__.demo2 object at 0x000001D7EBC5FEE0>
print(a1,b2)




