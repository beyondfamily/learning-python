'''
被特殊语法封装的成员，会有不同的访问的权限

封装的级别
      成员  ==》 公有的
      _成员 ==》 受保护的 （约定俗成，而python没有具体实现）
      __成员==》 私有的
          共有的 public   受保护的 protected   私有的  private
在类的内部    OK                OK                 OK
在类的外部    OK                NO(python可以)      NO

在python中给成员进行私有化，其实就是改了成员的名字
私有化==》_类名 __成员
'''
class person():
    name='名字'
    _age='年龄'  # 在成员面前加一个 _ 受保护的成员
    __sanwei='三维' # 在成员面前加两个_ 私有的成员

    # 初始化的方法
    def __init__(self,n,a,s):
        self.name=n
        self._age=a  # 内部也需要加_
        self.__sanwei=s # 内部也需要加__

    def func(self):
        # 在类的内部可以操作任意成员
        print(self.__sanwei)
        self.__kiss()

    # 成员的方法
    def say(self):
        print('聊聊人生和理想。。。')

    def _sing(self):  # 使成员的方法受保护
        print('高歌一曲，豪放一生。。。')

    def __kiss(self): # 使成员的方法私有
        print('打个kiss。。。')



# 实例化对象
# ym=person('杨幂',28,'70 50 60')
# print(ym.age) #在类的外部不能操作 受保护的成员（但python可以）
# print(ym.sanwei) #在类的外部不能操作 私有成员属性
# ym.sing() # ok
# ym.kiss() # 在类的外部不能操作 私有成员属性
# print(ym._person__sanwei) # 可以使用特殊的语法获取私有成员
# 查看对象的所以成员
# print(ym.__dict__)  # 可以获取当前对象的所以属性


