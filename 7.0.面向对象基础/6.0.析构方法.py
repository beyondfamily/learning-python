# 析构方法 __del__
'''
__del__
   析构方法会在对象被销毁时自动触发
   作用：关闭一些开发的资源
   注意：是对象被销毁时触发了这个方法，而不是这个方法销毁了对象

对象会在那些情况下被销毁？
   1.当程序执行完毕，内存中所以的资源都会被销毁释放
   2.使用 del 删除时
   3.对象不在被引用时，会自动销毁
'''

'''
定义一个类，完成一个信息的记录
    调用这个对象的时候，传递一个日志信息
    这个对象会创建一个文件，开始写入，并在最后关闭这个文件
'''

import time
class writelog():
    # 成员属性
    # 文件路径
    fileurl='./'
    # 日志文件的名称
    filename = str(time.strftime('%Y-%m-%d %H-%M-%S')) + '.log'

    # 初始化 打开文件
    def __init__(self):  # 额外的参数在实例化对象时直接接收
        # 完成打开文件
        # print('初始化方法触发，完成打开文件')
        self.fileobj=open(self.fileurl+self.filename,'a+',encoding='utf-8')

    # 写日志的方法
    def log(self,s):
        # print(f'把日志：{s}写入文件中')
        # self.fileobj=open(self.fileurl+self.filename,'a+',encoding='utf-8')
        # 1.0.方法1
        # with open(f'{self.fileurl}{self.filename}', 'a+', encoding='utf-8') as fp:
        #     fp.write(s)
        # 2.0.方法2
        self.fileobj.write(s)


    # 析构方法
    def __del__(self):
        # print('析构触发了，关闭打开的文件')
        # 在对象被销毁时，关闭在初始化方法中关闭打开的文件对象
        self.fileobj.close()

# 实例化对象
# l=writelog()
# l.log(input('快点给老子输入你想要的内容：'))


'''
情况1

l=writelog()
l.log('今天天气不错！！')
print('.......')

初始化方法触发，完成打开文件
把日志：今天天气不错！！写入文件中
.......
析构触发了，关闭打开的文件
__del__在程序最后销毁时触发
'''

'''
情况2

初始化方法触发，完成打开文件
把日志：今天天气不错！！写入文件中
析构触发了，关闭打开的文件

writelog()
print('.......')

初始化方法触发，完成打开文件
析构触发了，关闭打开的文件
'''

# 思考一个问题？
class cart():
    brand=''
    def __init__(self,b):
        self.brand=b
        print(f'初始化方法被触发：创建{self.brand}汽车')

    def __del__(self):
        print(f'析构方法被触发：{self.brand}汽车已经销毁了')

# 问题1.请问下面程序的执行顺序？
bm=cart('宝马')
bc=cart('奔驰')
fll=cart('法拉利')
'''
初始化方法被触发：创建宝马汽车
初始化方法被触发：创建奔驰汽车
初始化方法被触发：创建法拉利汽车
析构方法被触发：宝马汽车已经销毁了
析构方法被触发：奔驰汽车已经销毁了
析构方法被触发：法拉利汽车已经销毁了
'''

# 问题1.请问下面程序的执行结果
cart('宝马')
cart('奔驰')
cart('法拉利')
'''
属于情况3 创建之后没有被引用 就被销毁了

初始化方法被触发：创建宝马汽车
析构方法被触发：宝马汽车已经销毁了
初始化方法被触发：创建奔驰汽车
析构方法被触发：奔驰汽车已经销毁了
初始化方法被触发：创建法拉利汽车
析构方法被触发：法拉利汽车已经销毁了
'''







