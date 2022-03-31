import shutil
# 1.0.copy 复制文件  把一个文件拷贝到指定的目录中
# shutil.copy('123.jpg','./pic') # 保留原始格式
# shutil.copy('123.jpg','./pic/222.jpg') # 修改了文件名

# 2.0.copyfile(和1.0类似,但不建议) 拷贝文件的内容（打开文件，读取内容，写入到新的文件中）
shutil.copyfile('test_pic/1.6.jpg','pic/1.jpg')

# 3.0.copytree 可以把整个目录结构和文件全部拷贝到指定目录中，但是要求指定的目标目录必须不存在
# shutil.copytree('test_pic','result_pic')

# 4.0.rmtree() 删除整个文件夹
# shutil.rmtree('result_pic')

# 5.0.move 移动文件或文件夹到指定目录，也可以用于修改文件夹或文件的名称
# shutil.move('./test_pic','./pic/result_pic')




