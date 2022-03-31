# 日志类的封装
'''
日志类
   class Mylog
   功能：
      能够随时写入一个日志信息

   分析：
      日志文件在什么地方？默认在当前目录
      日志的文件名叫什么？当前日期 2021-9-17.log
      日志的格式是什么样的？ 2021-9-17 17:11:12 错误信息...


      属性：成员属性的作用就是存储信息，供成员方法来使用的
           fileurl 日志文件的地址
           filename 日志文件的名称
           fileobj  打开的文件对象

      方法：具体完成的一个功能的过程
         __init__() ==> 初始化方法，完成对象的初始化，并打开文件
        wlog()      ==> 负责接受用给的日志信息，并写入到日志文件中
        __del__()   ==> 析构方法，在对象被销毁时，关闭打开的文件
'''
import time
class mylog():
    #属性
    fileurl='./'
    filename=str(time.strftime('%Y-%m-%d'))+'.log'
    fileobj=None

    # 方法
    def __init__(self):
        # 打开文件
        self.fileobj=open(self.fileurl+self.filename,'a+',encoding='utf-8')

    def wlog(self,s):
        # 准备数，开始写入
        # 2021-9-17 17:11:12 错误信息...
        date=time.strftime('%Y-%m-%d %H:%M:%S')
        msg=date+' '+s+'\n'
        # 写入
        self.fileobj.write(msg)

    def __del__(self):
        # 关闭打开的文件
        self.fileobj.close()

w=mylog()
w.wlog(input('快点给爷写日志：'))


