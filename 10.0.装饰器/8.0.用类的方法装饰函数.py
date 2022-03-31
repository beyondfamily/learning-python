class outer():
    def newinner(func):
        outer.func=func    # 把传递进来的函数定义为类方法
        return outer.inner # 同时返回一个新的类方法

    @staticmethod
    def inner():
        print('拿到妹子大的微信')
        outer.func()
        print('看一场午夜电影')

@outer.newinner # outer.newinner(love) ==> outer.inner
def love():
    print('和妹子谈谈人生喝喝茶')

love()