# os.path 路径模块
import os
# 1.0.将相对路径转化为绝对路径  ***
res = os.path.abspath('./')  # F:\PyProject\Learning_Python\6.0.内置模块\3.0.os 操作系统接口模块

# 2.0.获取路径中的主体部分 就是返回路径中的最后一部分
res = os.path.basename(r'F:\PyProject\Learning_Python\6.0.内置模块\2.0.math和random\2.0.random.py') # 2.0.random.py
res = os.path.basename(r'F:\PyProject\Learning_Python\6.0.内置模块\2.0.math和random') # 2.0.math和random

# 3.0.获取路径中的路径部分  返回路径中最后一部分之前的内容
res=os.path.dirname(r'F:\PyProject\Learning_Python\6.0.内置模块\2.0.math和random\2.0.random.py') # F:\PyProject\Learning_Python\6.0.内置模块\2.0.math和random

# 4.0.join()  链接多个路径，组成一个新的路径
res = os.path.join('./a/b/c/','2.jpg')  #./a/b/c/2.jpg

# 5.0.split() 拆分路径，把路径拆分为路径和主体部分，
res = os.path.split('./abc/def/aaa')  # ('./abc/def', 'aaa')

# 6.0.splitext() 拆分路径，可以拆分文件后缀名
res = os.path.splitext('./a/b/2.jpg') #('./a/b/2', '.jpg')

# 7.0.获取文件的大小  字节数
res = os.path.getsize('./a/b/c/123.jpg') # 328982

# 8.0.检测是否是一个文件夹,是否存在
res = os.path.isdir('/Users/24345/PycharmProjects/learn/a')  # False

# 9.0.检测文件是否存在  ***
res = os.path.isfile('/Users/24345/PycharmProjects/learn/a/b/2.jpg')  # False

# 10.0.exists() **** 检测路径是否存在，既可以检测文件，也可以检测路径
res = os.path.exists('/Users/24345/PycharmProjects/learn/a/b/2.jpg')  # False


# 11.0.检测两个path路径是否同时指向了一个目标位置 （两个路径必须真实）
a = r'F:\PyProject\Learning_Python\6.0.内置模块\2.0.math和random'
b = '../2.0.math和random'
res = os.path.samefile(a,b) # True




print(res)


