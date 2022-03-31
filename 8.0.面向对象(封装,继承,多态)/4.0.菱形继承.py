class HuMan():
    def eat(self):
        print('我是祖先类')

# 父亲类
class F(HuMan):
    def eat(self):
        super().eat()
        print('我是父亲类')


# 母亲类
class M(HuMan):
    def eat(self):
        super().eat()
        print('我是母亲类')


# 孩子类
class C(F,M):
    def eat(self):
        super().eat()
        print('我是孩子类')

# 实例化对象
c=C()
c.eat()
'''
我是祖先类
我是母亲类
我是父亲类
我是孩子类

继承关系：C->F->M->HuMan
最先输出最底层的

super()
   使用super去调用父级的方法时，实际上是在使用super调用MRO列表中的上一级中的方法
   使用super去调用父级的属性时，实际上是在使用super调用MRO列表中的上一级中的属性
   
super()本身调用父级方法是，传递的self对象，就是这个方法中的那个self对象自己      
'''
# mro() 获取MRO列表，就是类的继承光系
print(C.mro())
# [<class '__main__.C'>, <class '__main__.F'>, <class '__main__.M'>, <class '__main__.HuMan'>, <class 'object'>]
print(F.mro())
# [<class '__main__.F'>, <class '__main__.HuMan'>, <class 'object'>]
print(HuMan.mro()) # [<class '__main__.HuMan'>, <class 'object'>]
