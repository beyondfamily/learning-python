'''
定义一个接口规范类，其他类都继承这个类，并实现（重写）父类中的方法
由于每个对象实现父类方法的方式或者过程都不相同，最后的结果是不一样的形态
'''


# 定义 USB
class usb():
    '''
    当前类的说明：
        这个类是一个接口规范类，需要子类继承并实现start方法
        start方法不做任何具体功能的实现
    '''
    # 在usb中类定义一个规范的接口，但是不实现任何功能
    def start1(self):
        print('老子是usb接口')

# 定义鼠标类
class mouse(usb):
    def start(self):
        print('鼠标启动成功，可以双击单击')

# 定义键盘类
class keybord(usb):
    def start(self):
        print('键盘启动成功了，赶紧双击666')

# 定义U盘类
class udisk(usb):
    def start(self):
        print('u盘启动了，赶紧看一下种子还在不在')

# 实例化对象
m=mouse()      # 鼠标对象
k=keybord()    # 键盘对象
u=udisk()      # u盘对象

m.start()
k.start()
u.start()
u.start1()
m.start1()

