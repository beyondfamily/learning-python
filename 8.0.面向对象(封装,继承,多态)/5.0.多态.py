# 对于同一个方法，由于调用的对象不同（或者传入的对象不同），最终实现了不同的结果

# 定义电脑类
class computer():
    # 在电脑类定义一个sub的规范接口 方法
    def usb(self,obj):
        obj.start()

# 定义鼠标类
class mouse():
    def start(self):
        print('鼠标启动成功，可以双击单击')

# 定义键盘类
class keybord():
    def start(self):
        print('键盘启动成功了，赶紧双击666')

# 定义U盘类
class udisk():
    def start(self):
        print('u盘启动了，赶紧看一下种子还在不在')


# 实例化对象
c=computer()   # 电脑对象
m=mouse()      # 鼠标对象
k=keybord()    # 键盘对象
u=udisk()      # u盘对象

# 把不同的设备插入到电脑的usb的接口中
c.usb(m)
c.usb(k)







