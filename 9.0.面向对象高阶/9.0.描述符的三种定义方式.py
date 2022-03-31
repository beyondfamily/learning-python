
# 格式一 通过定义 描述符类来实现
class ScoreManage():
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

class Student():
    score=ScoreManage()

# 格式二 使用 property函数来实现
class Student():

    # 在当前需要被管理的类中 直接定义类似下面三个方法
    def getscore(self):    # 调用时触发
        print('getscore')

    def setscore(self,value): # 赋值时触发
        print('setscore',value)

    def delscore(self): # 删除时触发
        print('delscore')


    # 在函数中 指定对象的三个方法
    # 对应的方法 1.__get__ 2.__set__ 3.__delete
    score=property(getscore,setscore,delscore)

zs=Student()
print(zs.score,'!!!!!!!!!') # None !!!!!!!!!
zs.score=200
del zs.score

# 格式三 使用@property 装饰器语法来实现
class Student():
    __socre=None

    @property       # 调用
    def score(self):
        print('get')
        return self.__socre

    @score.setter   # 赋值
    def score(self,value):
        print('set')
        self.__score=value

    @score.deleter  # 删除
    def score(self):
        print('delete')
        del self.__score

zs=Student()
print(zs.score,'!!!!!!!!') # 首先调用了zs.score print('get')  然后返回return self.__socre
zs.score=199 # set
print(zs.score,'@@@@@@@@') # 首先调用了zs.score print('get')  然后返回return self.__socre
del zs.score


