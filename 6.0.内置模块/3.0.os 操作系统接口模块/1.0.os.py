import os
import time
# 1. os.getcwd() 获取当前的工作目录,注意获取的不是当前脚本的目录，
res = os.getcwd() # F:\PyProject\Learning_Python\6.0.内置模块\3.0.os 操作系统接口模块

# 2. os.chdir() # 修改当前的工作目录
# os.chdir('C://Users/24345/PycharmProjects/learn')
# 查看修改后的工作目录
# print(os.getcwd()) # C:\Users\24345\PycharmProjects\learn

#3. os.listdir() 获取当前或指定目录中的所有项（文件，文件夹，隐藏文件），组成的列表
res = os.listdir() # ['1.0.os.py']
res = os.listdir(path=r'F:\PyProject\Learning_Python\6.0.内置模块\2.0.math和random') # ['1.0.math.py', '2.0.random.py']

# 4. os.mkdir(文件夹路径，权限)  # 创建文件夹
# os.mkdir('a',0o777)  # 默认在工作目录创建一个个人文件夹

# abc/a/b/c 都不存在时，无法使用 mkdir进行递归创建
# os.mkdir('/users/yc/Desktop/code/abc/a/b/c')

# 5. os.makedirs() 可以递归创建文件夹
# os.makedirs('/users/yc/Desktop/code/abc/a/b/c/')

# 6. os.rmdir() 删除 空 文件夹
# os.rmdir('./a')  # a 是一个空文件夹
# os.rmdir('./b')  # b 是 含有一个文件夹的 目录 OSError: Directory not empty: './b'
# os.rmdir('./c')  # c 是 含有一个文件的  目录   OSError: [Errno 66] Directory not empty: './c'

# 7. os.removedirs() 递归删除空文件夹  #os.removedirs('./abc/a/b/c') 删完了

# 8. os.remove()  删除文件
# os.remove('./abc/.DS_Store')

# 9. os.rename() 修改文件或文件夹的名字
# os.rename('./a','./AAA')

# 10. os.system() 执行操作系统中的命令
os.system('print.py')
time.sleep(3)
os.system('print.py')
