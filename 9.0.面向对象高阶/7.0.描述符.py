# 定义描述符类
class PeronName():
    __name='abc'
    __name1='abcdefg'
    '''
    _:param self: _描述符对象本身
    _:param instance: _使用描述符的对象的实例
    _:param owner: _使用描述符的对象拥有者
    '''

    def __get__(self, instance, owner):  # 调用时触发 例如 zs.name
        print(1)
        # print(self,instance,owner)
        return self.__name1

    def __set__(self, instance, value): # 赋值   self.__name1=value 决定把值赋值给谁
        print(2)
        # print(self,instance,value)
        self.__name1=value

    def __delete__(self, instance): # 删除
        print(3)
        print(self,instance)
        print('不允许删除')


class person():
    # 把类中的一个成员属性交给一个描述符来实现
    # 一个类中的成员的值是另一个描述符类的对象
    # 那么对这个类中的成员进行操作时，可以理解为就是对另一个对象的操作
    name=PeronName()

# 实例化对象
zs=person()
print(zs.name,'!!!!!') # abcdefg !!!!!

zs.name='张三'
print(zs.name,'!!!!!!!!!!!!!!') # 张三 !!!!!!!!!!!!!!

del zs.name
# print(zs.name)
