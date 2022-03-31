class a():
    pass
class b():
    pass
class c():
    pass

class demo(a,b,c):
    '''
    此处是类的说明文档
    '''
    name='a'
    age=20

    def say(self):
        print('会说唱rap')

obj=demo()
obj.san='a'

# 获取类/对象的所属成员 类/对象.__dict__
res=demo.__dict__  # 获取当前类的所属成员 {'__module__': '__main__', '__doc__': '\n    此处是类的说明文档\n    ', 'name': 'a', 'age': 20, 'say': <function demo.say at 0x0000023FBBC78820>}
res=obj.__dict__   # 获取当前对象的所属成员  {'san': 'a'}

# 获取类的文档信息  类/对象.__doc__
res=demo.__doc__ # '\n    此处是类的说明文档\n    '
res=obj.__doc__ # '\n    此处是类的说明文档\n

# 获取类名称组成的字符串
res=demo.__name__ # demo

# 获取类所在的文件名称，如果是当前文件，显示位__main__
res=demo.__module__ # __main__

# bases 获取当前类的父类列表
res=demo.__bases__    #  获取继承的所以的父类 (<class '__main__.a'>, <class '__main__.b'>, <class '__main__.c'>)
res=demo.__base__   # 获取继承的第一个父类


# mro列表 获取当前类的继承链
res=demo.__mro__ # (<class '__main__.demo'>, <class '__main__.a'>, <class '__main__.b'>, <class '__main__.c'>, <class 'object'>)

print(res)