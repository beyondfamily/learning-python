# 使用函数装饰器，给类进行装饰，增加新的属性和方法

def kuozhan(cls1):
    def func2():
        print('我是在装饰器中追加的新方法，func2')
    cls1.func2=func2 # 把刚才定义的方法赋值给 类
    cls1.name='我是在装饰器中追加的新属性 name'

    # 返回时，把追加类成员的 类 返回去
    return cls1

@kuozhan
class Demo():
    @staticmethod
    def func():
        print('我是Demo类中定义的func方法')

Demo.func()
Demo.func2()
print(Demo.name)