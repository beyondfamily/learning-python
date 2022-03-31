import threading

class MyThread(threading.Thread): # 这是threading.Thread的自类别

    def __init__(self):
        # 类的继承，调用父类的__init__方法。 Python的继承默认不调用父类的构造器函数，所以需要手动调用
        # threading.Thread.__init__(self) # 建立线程
        super(MyThread, self).__init__()
        # 1.0.super(子类，self).__init__(参数1，参数2，....)
        # 2.0.父类名称.__init__(self, 参数1，参数2，...)

    def run(self): # 定义线程工作
        print(threading.Thread.getName(self))
        print('Happy Python')

a=MyThread()
a.run()
a.run()
b=MyThread()
b.start()




