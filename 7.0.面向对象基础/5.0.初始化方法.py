# 魔术方法 初始化方法
'''
魔术方法：
   魔术方法也和普通方法一样都是类中定义的成员方法
   魔术方法就是不需要去手动调用的，魔术方法会在某种情况，自动触发（自动换行）
   魔术方法还有一个比较特殊的地方：就是多数魔术方法 前后有两个连续的下划线
   魔术方法不是我们自己定义的，而是系统定义好的，我们来使用

__init__ 初始化方法
    触发机制：在通过类实例化对象后，自动触发的一个方法
    作用：可以在对象实例化后完成对象的初始化，（属性的赋值,方法的调用）
    应用场景： 文件的打开，数据的获取。。。干活前的一些准备功能
'''
class person1():
    # 成员属性
    name=None
    age=None
    sex=None
    #  __init__ 初始化方法
    def __init__(self,a,b,c):
        # 完成对象属性的初始化
        self.name=a
        self.age=b
        self.sex=c
        #自动调用方法
        self.say()

    # 成员方法
    def say(self):
        print(f'大家好，我是{self.name},是兄弟就来砍我')

class person2():
    # 成员属性
    name=None
    age=None
    sex=None
    #  __init__ 初始化方法
    def __init__(self,a,b,c):
        # 完成对象属性的初始化
        #自动调用方法
        self.say()
        self.name=a
        self.age=b
        self.sex=c


    # 成员方法
    def say(self):
        print(f'大家好，我是{self.name},是兄弟就来砍我')

# 实例化对象
zzh1=person1('张家辉',56,'男')
zzh2=person2('张家辉',56,'男')


