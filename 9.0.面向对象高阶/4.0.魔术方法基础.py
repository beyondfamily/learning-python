'''

1.__init__ 初始化方法
   触发机制：当实例化对象之后就会立即触发的方法
   作用：   为当前创建的对象完成一些初始化的操作，比如：成员属性的数值，方法的调用，打开或创建一些资源
   参数：   一个self，接受当前对象，其它参数根据需要进行定义即可
   返回值：  无
   注意事项： 无

2.__new__ 构造方法
   触发机制： 实例化对象时自动触发(在__init__之前触发)
   作用：    管理控制对象创建的过程
   参数：    一个cls接受当前的类，其他参数根据初始化方法的参数进行决定
   返回值：   必须返回object.__new__(cls)进行对象的创建，如果没有返回值，则实例化对象的结果为None
   注意实现：
           __new__方法的参数和__init__方法的参数要保持一致，除了第一个参数
           必须返回object.__new__(cls)进行对象的创建，如果没有返回值，则实例化对象的结果为None
   应用场景：设计模式中的单例设计

3.__del__ 析构方法
    触发机制：当该类对象被销毁时自动触发
    作用：   关闭或释放对象创建时打开或创建的一些资源
    参数：   一个self，接受当前的对象
    返回值：  无
    注意事项： 无

4.__call__
    触发机制：把对象当做函数直接调用时自动触发
    作用：   一般用于归纳类或对象的操作步骤，方便调用
    参数：   一个self接收当前对象，其他参数根据调用需求确定
    返回值：  可有可无

1.__len__
    触发机制：当使用len函数去检测当前对象的时候自动触发
    作用：   可以使用len函数检测当前对象中某个数据的信息
    参数：   一个self，接受当前的对象
    返回值：  必须有，并且必须是一个整型
    注意事项： len要获取什么属性的值，就在返回值中返回那个属性的长度

2.__str__
    触发机制：当使用str或者print函数对对象进行操作时自动触发
    作用：   代码对象进行字符串的返回，可以自定义打印的信息
    参数：   一个self，接受当前的对象
    返回值：  必须有，并且必须是字符串类型的值

3.__bool__
    触发机制：可以使用bool函数转换当前对象时，自动触发，默认情况下，对象会转为True
    作用：   可以代替对象进行bool类型的转换，可以转换任何数据
    参数：   一个self，接受当前的对象
    返回值：  必须是一个布尔类型的返回值

'''

# 定义一个人类
class person():

    # 构造方法
    def __new__(cls,*args):
        print('触发了构造方法')
        print(args)
        # 如果在给方法中没有返回如下格式，则对象无法创建
        return object.__new__(cls)

    # 初始化方法
    def __init__(self,name,age,sex):
        print('触发了初始化方法')
        self.name=name
        self.age=age
        self.sex=sex

    def __call__(self, *args, **kwargs):
        print('你把对象当成了函数进行调用')

    #析构方法
    def __del__(self):
        print('触发了初析构方法')


    def hello(self):

        print(f'我叫{self.name},我今年{self.age},我的性别是{self.sex}')


# 实例化对象
zs=person('张三丰',180,'男')
zs.hello()
zs()



print('='*80)

class Demo():
    listurl = [1, 2, 3]

    # 可以代替对象使用len函数，并返回一个指定的整型
    def __len__(self):
        # 必须返回数字
        return len(self.listurl)

    # 可以代替对象使用str或者print的信息返回
    def __str__(self):
        return '<这是当前脚本中的一个_对象>'

    def __bool__(self):
        return bool(self.listurl)

# 实例化对象
obj=Demo()
res=len(obj)
print(res)
res=str(obj)
print(res)
print(obj)
res=bool(obj)
print(res)
print(type(res))
