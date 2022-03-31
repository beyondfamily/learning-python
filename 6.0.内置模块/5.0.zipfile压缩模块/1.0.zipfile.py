import json
import zipfile,os


# # 1.0.压缩文件
# with zipfile.ZipFile('spam.zip', 'w') as myzip:
#     # 操作的对象是filename
#     myzip.write('./待压缩/1.0.data.pickle')
#     myzip.write('./待压缩/1.0.json.json')
#     myzip.write('./待压缩/1.0.pic.jpg')

# 2.0.解压缩文件
with zipfile.ZipFile('spam.zip', 'r') as myzip:
    myzip.extractall('./')


# 3.0.使用shutil模块进行归档压缩
# import shutil
# # 参数1 创建的压缩文件名称，参数2，指定的压缩格式，zip，tar 参数3 要压缩的文件或文件夹路径
# shutil.make_archive('a','zip','./')

