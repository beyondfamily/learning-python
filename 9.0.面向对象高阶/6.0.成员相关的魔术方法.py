'''
1.__getattribute__   优先级最高
    触发机制：当访问对象成员时，自动触发，无论当前成员是否存在
    作用：   可以在获取对象成员时，对数据进行一些处理
    参数：   一个self接收对象，一个item接收当前访问的成员名称
    返回值：  可有可无，返回值就是访问的结果
    注意事项： 在当前的魔术方法中，禁止使用 对象.成员的方式进行访问，会触发递归
             如果想要在当前魔术方法中访问对象的成员必须使用 object.__getattribute__来访问
             格式：object.__getattribute__(self, item)

2.__getattr__
    触发机制：   当访问对象中不存在的成员时，自动触发
    作用：   防止访问不存在的成员时报错，也可以为不存在的成员进行赋值
    参数：   一个self接收当前对象，一个item接收当前访问的成员名称
    返回值：  可有可无
    注意事项： 当存在__getattribute__方法时，会去执行__getattribute__方法

3.__setattr__
    触发机制： 当给对象的成员进行赋值操作时会自动触发（包括添加，修改）
    作用：     可以限制或管理对象成员的添加和修改操作
    参数：     1.self 接收当前对象 2.设置的成员名 3.设置的成员值
    返回参数： 无
    注意事项： 在当前的魔术方法中禁止给当前对象的成员直接进行赋值操作，会触发递归操作
              如果想要给当前对象的成员进行赋值，需要借助 object
              格式： object.__setattr__(self,key,value)

4.__delattr__
    触发机制：   当删除对象成员时自动触发
    作用：       可以去限制对象成员的删除，还可以删除不存在成员时防止报错
    参数：       1.self接收当前对象  2.item 删除的成员名
    返回值：      无
    注意事项：    在当前魔术方法中禁止直接删除对象的成员，会触发递归操作
                如果想要删除当前对象的成员，那么需要借助 object
                格式： object.__delattr__(self,item)
'''
class person():
    name='名字'
    age='年龄'
    sex='性别'

    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.sex=s

    def say(self):
        print('聊聊人生，谈谈理想。。。')

    def sing(self):
        print('高歌一曲')

    # 获取对象成员时自动触发
    def __getattribute__(self, item):
        try:
            # 在方法中使用object来获取对应成员的属性值
            res=object.__getattribute__(self, item)
            # 在方法中可以对访问的成员数据进行处理
            return res[0] + '*' + res[-1]
        except:
            print('直接访问没有的成员会触发老子__getattribute__')
            return False
        # try和except可以实现__getattr__的效果

    #  当访问不存在的成员时自动触发
    def __getattr__(self, item):
        print('直接访问没有的成员会触发老子')
        return False

    # 当给对象成员进行赋值时触发，注意该方法中如果没有给对象成员进行赋值，那么成员对象赋值失败
    def __setattr__(self, key, value):
        print('有人给老子赋值了')
        object.__setattr__(self, key, value) # 进行赋值

    # 当删除对象时自动触发
    def __delattr__(self, item):
        print('有人把老子删除了')
        object.__delattr__(self, item)




zs=person('张三丰',120,'男')
print(zs.name) # 张*丰
print(zs.namee)

zs.abc='aabbccee' # a*e __setattr__(self, key, value): 无法直接给对象成员的属性进行赋值
print(zs.abc)
del zs.name
print(zs.name)
