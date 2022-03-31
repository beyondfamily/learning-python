import re
'''
    ()作用
    1. 将原子 1，2，3，4，a,b,c 变成大原子
    2. 在括号可以 | (或)  的关系
    3. 反向引用 respace()
'''

# 1.0
part=re.compile('i(mo)+nkey')
str ='this is a imomomomomomonkey imooonkey imomonkey imnkey imoooooooonkey imonkey'
res=re.finditer(part,str) # findall只会读取括号内的内容和js不一样 ['mo', 'mo', 'mo']
print([i.group() for i in res]) # ['imomomomomomonkey', 'imomonkey', 'imonkey']

# 2.0
part=re.compile('i(mo|hello|abc)+nkey') # 读取有1个或多个中间是mo或hello或abc的
str ='this is a imomomomomomonkey ihellonkey iabcnkey imnkey imoooooooonkey imonkey'
res=re.finditer(part,str)
print([i.group() for i in res]) # ['imomomomomomonkey', 'ihellonkey', 'iabcnkey', 'imonkey']

