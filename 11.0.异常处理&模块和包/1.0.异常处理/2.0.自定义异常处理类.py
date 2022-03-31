'''
在出现异常后，对异常进行处理，并且把异常信息写入日子
日志的基本格式
    日期时间 异常级别
    异常信息：引发的异常类，异常的信息 文件及行号
'''
import traceback
import logging

# 通过 traceback 模块获取异常信息
try:
    int('aa')
except:
     # 通过 traceback模块获取异常信息
     errormsg=traceback.format_exc()
     print(errormsg)    # ValueError: invalid literal for int() with base 10: 'aa'

print('='*80)

# 自定义异常日志处理类
class Myexception():
    def __init__(self):
        import traceback
        import logging

        # logging的基本配置
        logging.basicConfig(
            filename='./error.txt', # 日志存储的文件及目录
            format='%(asctime)s %(levelname)s\n %(message)s', #格式化存储的日志模式
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 写入日志
        logging.error(traceback.format_exc())

try:
    int('a')
except:
     Myexception() # 在异常处理的代码中去调用自定义异常日志处理类
