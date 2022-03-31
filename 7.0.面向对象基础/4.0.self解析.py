# 定义人类
# self 是 class person()
class person():
    # 成员属性
    name='名字'
    age='年龄'
    sex='性别'

    # 成员方法
    def sing(self): # 括号中self是传递person()属性进来
        print('会唱')

    def dance(self):
        print('会跳')

    def rap(self):
        print(f'我是{self.name}会rap')  #可以调用自己  # self是class person()


    def func(self):
        # #测试，在类的内部是否可以想类的外部一样，去访问和操作成员
        # print(self)
        # print(self.name)  #访问对象的属性
        # self.name='李四'  #修改对象的属性
        # print(self.name)
        # self.sanwei='00 00 00' #添加对象的属性
        # print(self.sanwei)
         self.rap() #调用对象的方法
        # #只要是对象能干的事，self都可以代表对象去完成
        # #比如：成员的所以操作（添加，删除，更新，访问，调用）


zs=person()
zs.func()
# zs.name='张三'
# 通过类实例化的对象，可以在类的外部去访问成员属性和成员方法 对象.成员
# print(zs) # <__main__.person object at 0x000001F14DC20610>
# zs.func() #<__main__.person object at 0x000001F14DC20610>
# zs.rap()
# zs.func2() #如果在类中定义的方法不含（self）这个形参时，这方法就不能
# person.func2() 可以调用
'''
self 单词本身的意思 自己
self 在类的方法中 代表 当前这个对象
self 代表调用这个方法的对象,谁调用了这个方法，self就代表谁
self 就可以在类的内部代替对象进行各种操作
如果在类中定义的方法不含（self）这个形参时，这方法就不能 （self形参，包括其他的代替都不可以）
不含self形参的方法，只能通过类去调用
这种不接受对象作为形参的方法，叫做绑定类的方法
'''

