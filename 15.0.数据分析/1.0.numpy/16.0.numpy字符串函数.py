import numpy as np
# 以下函数用于对dtype为numpy.string_或numpy.unicode_的数组执行向量化字符串操作。 它们基于 Python 内置库中的标准字符串函数。
'''
1.	add() 返回两个str或Unicode数组的逐个字符串连接
2.	multiply() 返回按元素多重连接后的字符串
3.	center() 返回给定字符串的副本，其中元素位于特定字符串的中央
4.	capitalize() 返回给定字符串的副本，其中只有第一个字符串大写
5.	title() 返回字符串或 Unicode 的按元素标题转换版本
6.	lower() 返回一个数组，其元素转换为小写
7.	upper() 返回一个数组，其元素转换为大写
8.	split() 返回字符串中的单词列表，并使用分隔符来分割
9.	splitlines() 返回元素中的行列表，以换行符分割
10.	strip() 返回数组副本，其中元素移除了开头或者结尾处的特定字符
11.	join() 返回一个字符串，它是序列中字符串的连接
12.	replace() 返回字符串的副本，其中所有子字符串的出现位置都被新字符串取代
13.	decode() 按元素调用str.decode
14.	encode() 按元素调用str.encod
'''


# 1.0.numpy.char.add() 函数执行按元素的字符串连接。
print(np.char.add(['hello'],[' xyz']))
print(np.char.add(['hello', 'hi'],[' abc', ' xyz']))

# 2.0.numpy.char.multiply() 这个函数执行多重连接。
print(np.char.multiply('Hello ',3))

# 3.0.numpy.char.center() 此函数返回所需宽度的数组，以便输入字符串位于中心，并使用fillchar在左侧和右侧进行填充。
print(np.char.center('hello',30,fillchar = '*'))

# 4.0.numpy.char.capitalize() 函数返回字符串的副本，其中第一个字母大写
print(np.char.capitalize('hello world'))

# 5.0.numpy.char.title() 返回输入字符串的按元素标题转换版本，其中每个单词的首字母都大写。
print(np.char.title('hello how are you?'))

# 6.0.numpy.char.lower() 函数返回一个数组，其元素转换为小写。它对每个元素调用str.lower。
print(np.char.lower(['HELLO','WORLD']))
print(np.char.lower('HELLO'))

# 7.0.numpy.char.upper() 函数返回一个数组，其元素转换为大写。它对每个元素调用str.upper。
print(np.char.upper(['HELLO','WORLD']))
print(np.char.upper('HELLO'))

# 8.0.numpy.char.split() 此函数返回输入字符串中的单词列表。 默认情况下，空格用作分隔符。 否则，指定的分隔符字符用于分割字符串。
print(np.char.split ('hello how are you?'))
print(np.char.split ('TutorialsPoint,Hyderabad,Telangana', sep = ','))

# 9.0.numpy.char.splitlines() 函数返回数组中元素的单词列表，以换行符分割。
# '\n' '\r' 都会用作换行符。
print(np.char.splitlines('hello\nhow are you?'))
print(np.char.splitlines('hello\rhow are you?'))

# 10.0.numpy.char.strip() 函数返回数组的副本，其中元素移除了开头或结尾处的特定字符。
print(np.char.strip('ashok arora','a'))
print(np.char.strip(['arora','admin','java'],'a'))

# 11.0.numpy.char.join()  这个函数返回一个字符串，其中单个字符由特定的分隔符连接。
print(np.char.join(':','dmy'))
print(np.char.join([':','-'],['dmy','ymd']))

# 12.0.numpy.char.replace() 这个函数返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代。
print(np.char.replace ('He is a good boy', 'is', 'was'))

# 13.0.numpy.char.decode()  这个函数在给定的字符串中使用特定编码调用str.decode()。
a = np.char.encode('hello', 'cp500')
print(a)
print(np.char.decode(a,'cp500'))

# 14.0.numpy.char.encode() 此函数对数组中的每个元素调用str.encode函数。 默认编码是utf_8，可以使用标准 Python 库中的编解码器。
a = np.char.encode('hello', 'cp500')
print(a)






