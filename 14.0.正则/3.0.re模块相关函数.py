import re

# 1.0.re.findall()
ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
print(ret)  # ['a', 'a']


# 2.0.re.search()
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
ret = re.search('an', 'eva egon yuan',).group()
print(ret)  # an


# 3.0.re.match()
# 同search,不过只在字符串开始处进行匹配
ret = re.match('a', 'ab cda').group()
print(ret)

# 4.0.re.split()
ret = re.split('-', 'a-b-c-d')
print(ret)  # ['a', 'b', 'c', 'd']
ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']


# 5.0.re.sub()
ret = re.sub('\d', 'H', 'eva3egon4yuan4', 2) # \d表示数字 #将数字替换成'H'，参数2表示只替换2个
print(ret) # evaHegonHyuan4


# 6.0.re.subn()
# 将数字替换成'H'，返回元组(替换的结果,替换了多少次)
ret = re.subn('\d', 'H', 'eva3egon4yuan4')
print(ret) # ('evaHegonHyuanH', 3)


# 7.0.re.compile()
obj = re.compile('\d{3}')  # 将正则表达式编译成为一个 正则表达式对象，规则要匹配的是2个数字
ret = obj.search('abc123eeee') # 正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  # 123


# 8.0.re.finditer()
ret = re.finditer('\d', 'ds3sy4784a') # finditer返回一个存放匹配结果的迭代器
print(ret) # <callable_iterator object at 0x0000020B2B4EA6D0>
print(next(ret).group()) # 3
print(next(ret).group()) # 4
print([i.group() for i in ret]) # ['7', '8', '4']


