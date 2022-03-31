class outer():

    # 魔术方法：当把该类的对象当做函数调用是，自动触发 obj()
    def __call__(self,func):
        self.func=func # 把传进来的函数作为对象的成员方法
        return self.inner # 返回一个函数

    # 在定义的需要返回的新方法中，去进行装饰和处理
    def inner(self,who):
        print('拿到妹子的微信。。。')
        self.func(who)
        print('看一场午夜电影。。。')


@outer() # outer() 当成函数使用
def love(who):
    print(f'{who}和妹子谈谈人生和理想')

love('小明')

print(love)
