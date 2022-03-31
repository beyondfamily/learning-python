import re

a='python12314534564java-python'

# 1.0.findall()
qi=re.findall('1',a) # (匹配规则,数据)
# print(qi) # ['1', '1']

# 2.0.re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
print(re.match('python', a)) # 获取的是一个对象 <re.Match object; span=(0, 6), match='python'>
print(re.match('python', a).group()) # 读取对象 python
print(re.match('python', a).span()) # 读取长度 (0, 6)

# 3.0.re.search 匹配整个字符串，直到找到一个匹配。
print(re.search('ython',a)) # <re.Match object; span=(1, 6), match='ython'>
print(re.search('ython',a).group()) # ython

