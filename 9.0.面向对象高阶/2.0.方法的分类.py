# 方法就是函数的另称

'''
1.对象方法
   特征：
      1.在类中定义的方法，含有self参数
      2.含有self的方法，只能使用对象进行调用
      3.该方法会把调用的对象传递进来
2.类方法
   特征：
      1.在类中定义的方法，使用装饰器 @classmethod 进行装饰
      2.方法中有cls形参
      3.不需要实例化对象，直接使用类进行调用
      4.会把调用这个方法的类直接转递进来
3.绑定类方法
    特征：
      1.在类中定义的方法，没有任何参数
      2.只能使用类进行调用
      3.不会传递任何参数进来
4.静态方法
     特征：
      1.在类中定义的方法，没有任何参数
      2.使用 装饰器 @staticmethod 进行了修饰
      3.可以使用对象或者类进行调用
      4.不会传递对象或者类进来
'''

class demo():

    # 对象方法
    def func1(self):
        print(self)
        print('this is object function func1')

    # 类方法
    @classmethod
    def func2(cls):
        print(cls)
        print('this is class function func2')

    # 绑定类方法
    def func3(): # 忽略报错
        print('this is bind class function func3')

    # 静态方法
    @staticmethod
    def func4(a,b):  # 也可以传参数
        print(a+b)
        print('this is static method func4')


# 对象方法 实例化对象
obj=demo()
obj.func1()
try:
    demo.func1()
except Exception as e: # 通用类错误
    print(e)

print('='*80)

# 类方法
demo.func2() # 可以使用类直接调用
obj.func2()  # 即便使用对象进行调用，传递进去的依然是类

print('='*80)

# 绑定类方法
demo.func3() # 可以使用类调用绑定类方法
try:
    obj.func3()  # 不能使用对象调用绑定类方法
except Exception as e:
    print(e)

print('='*80)

# 静态方法
demo.func4(2,2) # 可以使用类调用绑定类方法
obj.func4(2,2)  # 可以使用对象调用绑定类方法











