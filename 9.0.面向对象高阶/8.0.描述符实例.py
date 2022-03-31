'''
# 要求：学员的分数只能在0-100范围中
解决方法：
    1.在__init__方法中检测当前分数范围
        if score>=0 and score<=100:
            self.score=score
     这个解决方案只能在对象初始化时有效。
    2.定义一个setattr魔术方法检测
    检测如果给score分数进行赋值时，进行分数的检测判断
    if key=='score':
        if value >= 0 and value <= 100:
            object.__setattr__(self, key, value)
        else:
            print('当前分数不符合')
    else:
        object.__setattr__(self, key, value)

    假如 学员的分数不止一个时怎么版，比如 语文分数 数学分数 英语分数
    另外就是当前这个类中的代码是否就比较多了

     3.可以思考使用描述夫来代理我们这个分数属
        1.定义Score描述符类
        2.把学生类中的score这个成员交给描述符类进行代理
        3.只在在代理的描述符类中对分数进行赋值和获取就ok

'''
# 定义一个学生类 需要记录 学员的id 名字 分数
class Student():
    def __init__(self,id,name,score):
        self.id=id
        self.name=name

        # 检测分数范围
        if score>=0 and score<=100:
            self.score=score
        else:
            print('当前分数不符合')

    def returnMe(self):
        info = f'''
        学员编号：{self.id}
        学员姓名：{self.name}
        学院分数：{self.score}
        '''
        print(info)

    def __setattr__(self, key, value):
        # 检测是否给score进行赋值操作
        if key=='score':   # 是给类中score成员进行赋值才会触发
            if value >= 0 and value <= 100:
                object.__setattr__(self, key, value)
            else:
                print('当前分数不符合')
        else:
            object.__setattr__(self, key, value)


obj=Student(1,'xu',80)
# print(obj.id) # 1
obj.score=-20
print(obj.score) # 当前分数不符合

print('='*80)

# 定义描述符类 代理分数的管理
class Score():
    # __score1='tm老子就看看你调用的是不是老子'
    __score=0
    def __get__(self, instance, owner): # 调用时触发
       # return self.__score1
       return self.__score

    def __set__(self, key, value):      # 赋值
        if value>=0 and value<=100:
            self.__score=value
        else:
            print('分数不符合要求')


# 使用描述符类代理score分数属性
class Student():

    score = Score()
    def __init__(self,id,name,score):
        self.id=id
        self.name=name
        self.score=score

    def returnMe(self):
        info = f'''
        学员编号：{self.id}
        学员姓名：{self.name}
        学院分数：{self.score}
        '''
        print(info)


# 实例化对象
zs=Student(1011,'张三丰',99)
zs.returnMe()
zs.score=-20
zs.returnMe()
zs.score=55
zs.returnMe()




