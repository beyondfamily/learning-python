class a():
    pass
class b(a):
    pass
class c(a):
    ccc='abc'

class d(b,c):
    name='a'
    age=20

    def say(self):
        pass

D=d()

# 1.0.issubclass(子类,父类) 检测一个类是否是另一个类的子类
# res=issubclass(b,a) # b类是否位a类的子类
# print(res) # True

# 2.0.isinstance(对象,类) 检测一个对象是否是指定类的实例化对象或该类的子类的实例化结果
# res=isinstance(D,d) # True
# res=isinstance(D,b) # True
# print(res)

# 3.0.hasattr(对象/类,'成员名称') 检测类/对象是否包含指定名称的成员
# res=hasattr(d,'name') # True
# res=hasattr(d,'ccc')  # d继承了c中的成员 # True
# print(res)

# 4.0.getattr()  获取类/对象的成员的值
# res=getattr(d,'ccc')  #abc 可以获取继承的类/对象的成员的值
# print(res) # abc

# 5.0.setattr(对象/类,'成员名称','成员的值') 设置类/对象的成员的属性值
# res=setattr(d,'name','ooo')
# print(d.name) # ooo
# print(res) # None

# 6.0.delattr(类/对象,'成员名称') 删除类/对象的成员属性 和del直接删除对象的成员是一样的结果
# res=delattr(D,'name')
# print(res)

# 7.0.dir() 获取当前对象所以可以访问的成员列表
# res=dir(D)
# print(res) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'ccc', 'name', 'say']




