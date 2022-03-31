class kuozhan():
    def __call__(self, cls):
        # 把接收的类，赋值给当前对象，作为一个属性
        self.cls = cls
        # 返回一个函数
        return self.newfunc

    def newfunc(self):
        self.cls.name='我是在类装饰器中追加的新属性 name'
        self.cls.func2=self.func2 # 向传进来的类中添加fun2函数
        return self.cls()

    def func2(self):
        print('我是类装饰器中追加的新方法')

@kuozhan()
class Demo():
    def func(self):
        print('我是Demo类中定义的func方法')

print(type(Demo())) # <class '__main__.Demo'>  return self.cls() 的原因
obj=Demo()
obj.func()
obj.func2()
print(obj.name)


# 思考： 此时的obj这个对象，是哪个类的对象 Demo还是kuozhan
print(obj) # 此时的obj依然是Demo类的实例化对象，只不过经过装饰后，增加了新的属性和方法
# <__main__.Demo object at 0x00000142E8F19250>


print(kuozhan.__dict__)
