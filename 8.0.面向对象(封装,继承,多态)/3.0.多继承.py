# 父亲类
class F():

    def eat(self):
        print('大口喝酒，大口吃肉。。。')

# 母亲类
class M():

    def eat(self):
        print('动作优雅，浅尝即止。。。')


# 孩子类
class C(F,M):


    def eat1(self):
        self.eat()   # 函数名字重复时  调用靠第一个类
        print('吃也哭，不吃也哭。。。')

# 实例化对象
# c = C()
# c.eat1()

# 父亲类
class F2():

    def eat2(self):
        print('大口喝酒，大口吃肉。。。')

# 母亲类
class M2():

    def eat3(self):
        print('动作优雅，浅尝即止。。。')

# 孩子类
class C2(F2,M2):


    def eat4(self):
        self.eat3()
        self.eat2()
        print('吃也哭，不吃也哭。。。')


c2=C2()
c2.eat4()








