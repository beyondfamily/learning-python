# 在当前脚本中如果需要使用一些已经定义好的功能事，可以选则对应的某块，导入后使用

# 例如使用系统模块 time
# import time
# print(time.time())

import my

# 使用模块中定义的类
obj=my.myexception()
print(obj) # <my.myexception object at 0x0000027E497189D0>

# 使用模块中的函数
my.func()

# 使用模块中定义的变量
print(my.you)


# 想使用模块中的方法或者内容时，除了导入模块，还可以在指定模块中导入指定的内容
from my import you # 导入my模块中的you变量
from my import you as l # 导入my模块中的you变量，起个别名
print(you)
print(l)
