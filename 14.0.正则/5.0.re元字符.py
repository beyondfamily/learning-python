import re

# 1.0. .除了换行符和行结束符不可以匹配 别的都行 包括空格
part1=re.compile('.monkey')
str='this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
    // is a c9monkey is a monkey is a &monkey'
res_1=re.findall(part1,str) # ['wmonkey', '1monkey', '-monkey', '9monkey', '9monkey', ' monkey', '&monkey']


# 2.0. \w 查找单词字符 数字也算是单词，特殊符号不算
part1=re.compile('\wmonkey')
str='this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
     is a c9monkey is a monkey is a &monkey'
res_1=re.findall(part1,str) # ['wmonkey', '1monkey', '9monkey', '9monkey']


# 3.0. \W 查找非单词字符
part1=re.compile('\Wmonkey')
str = 'this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
       is a c9monkey is a monkey is a &monkey'
res_1=re.findall(part1,str) # ['-monkey', ' monkey', '&monkey']


# 4.0. \d 查找数字开头的
part1=re.compile('\dmonkey')
# part1=re.compile('[0-9]monkey') 与上面方法相同
str='this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
     is a c9monkey is a monkey is a &monkey is a 91monkey'
res_1=re.findall(part1,str) # ['1monkey', '9monkey', '9monkey', '1monkey']


# 5.0. \D 表示除了0-9
part1=re.compile('\Dmonkey')
str='this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
      is a c9monkey is a monkey is a &monkey is a 91monkey'
res_1=re.findall(part1,str) # ['wmonkey', '-monkey', ' monkey', '&monkey']


# 6.0. \s 查找空白字符 表示空格
part1=re.compile('\smonkey')
str='this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
     is a c9monkey is a monkey is a &monkey is a 91monkey'
res_1=re.findall(part1,str) # [' monkey']


# 7.0. \S 除了空白字符都找到
part1=re.compile('\Smonkey')
str='this is a wmonkey is a a1monkey is a b-monkey is a c9monkey\
     is a c9monkey is a monkey is a &monkey is a 91monkey'
res_1=re.findall(part1,str) # ['wmonkey', '1monkey', '-monkey', '9monkey', '9monkey', '&monkey', '1monkey']


# 8.0. \b 匹配单词的边界  \B表示不是边界
# 注意不加r的化\b会翻译成一个回退符
part1=re.compile(r'\d\dis\b')
part2=re.compile(r'\bis')
str='55is ais a island 123is 12is'
res_1=re.findall(part1,str) # ['55is', '23is', '12is']
res_2=re.findall(part2,str) # ['is']


# 9.0. \n 表示匹配换行符
part1=re.compile(r'is\n')
part2=re.compile(r'\nland')
str='this is a is\nland aisc'
res_1=re.findall(part1,str) # ['is\n']
res_2=re.findall(part2,str) # ['\nland']

print(res_2)






