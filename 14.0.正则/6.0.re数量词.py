import re

# 1.0. n+ 匹配任何包含至少一个n的字符串 n可以是任意一个字符
part=re.compile('imo+nkey')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooooonkey'
res=re.findall(part,str) # ['imonkey', 'imooooooooonkey', 'imooooonkey', 'imooooonkey']


# 2.0. n*匹配任何包括零个或多个n的字符串
part=re.compile('imo*nkey')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooooonkey'
res=re.findall(part,str) # ['imnkey', 'imonkey', 'imooooooooonkey', 'imooooonkey', 'imooooonkey']


# 3.0. n? 匹配任何包含零个或一个n的字符串
part=re.compile('imo?nkey')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooooonkey'
res=re.findall(part,str) # ['imnkey', 'imonkey']


# 4.0. n{x} 匹配包含x个n的序列的字符串
part=re.compile('imo{3}nkey')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooonkey'
res=re.findall(part,str) # ['imooonkey']


# 5.0. n{x,y} 匹配包含x至y个n的序列的字符串
part=re.compile('imo{0,3}nkey')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooonkey'
res=re.findall(part,str) # ['imnkey', 'imonkey', 'imooonkey']


# 6.0. n{x,} 匹配包含至少x个n的序列的字符串
part=re.compile('imo{3,}nkey')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooonkey'
res=re.findall(part,str) # ['imooooooooonkey', 'imooooonkey', 'imooonkey']


# 7.0. n$ 匹配任何结尾为n的字符串
part=re.compile('imonkex$')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooonkey timonkex'
res=re.findall(part,str) # ['imonkex']


# 8.0. ^n 匹配任何开头为n的字符串
part=re.compile('^this')
str='this is a imnkey imonkey imooooooooonkey imooooonkey imooonkey timonkex'
res=re.findall(part,str) # ['this']


# 10.example
# 以非空白开始以非空白结束
part1=re.compile('^\S+$')
# ?=正向预查，在任何开始匹配圆括号内的正则表达式模式的位置来匹配搜索字符串
# ?!负向预查，在任何开始不匹配该正则表达式模式的位置来匹配搜索字符串
part2=re.compile('\d\dis(?=tt)') # 对其后紧跟 " all" 的 "is" 进行全局搜索： 匹配任何其后紧接指定字符串n的字符串
str="Is 55isall there 66istt"
res1=re.findall(part1,str) # []
res2=re.findall(part2,str) # ['55is']



print(res2)





















