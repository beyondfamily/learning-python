import logging

# 创建一个logging对象
logger = logging.getLogger()

# 创建一个文件对象
fh = logging.FileHandler('logging/标配版.log', encoding='utf-8')

# 创建一个屏幕对象
sh = logging.StreamHandler()

# 配置显示格式
formatter1 = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
formatter2 = logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(formatter1)
sh.setFormatter(formatter2)
logger.addHandler(fh)
logger.addHandler(sh)

# 总开关
logger.setLevel(10)

fh.setLevel(10)
sh.setLevel(40)

logging.debug('调试模式')  # 10
logging.info('正常模式')  # 20
logging.warning('警告信息')  # 30
logging.error('错误信息')  # 40
logging.critical('严重错误信息')  # 50
# 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
# debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
# info : 打印info,warning,error,critical级别的日志,确认一切按预期运
# warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
# error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
# critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行