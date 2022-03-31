# 转义字符
'''
>>一个普通的字符出现在转义符 \的后面时，实现了另外一种意义
+ \ 转义符，续行符。
  + 作为转义符时，在\后面出现的字符可能会实现另外一种意义。
  + 作为续行符时，在行尾使用了\后，可以换行继续书写内容
+ \n 代表一个换行符
+ \r 代表光标位置（从\r出现的位置开始作为光标的起点）
+ \t 代表一个水平制表符（table 缩进）
+ \b 代表一个退格符
+ `\\` 反转义\，输出了\，取消\的转义效果

# \ 续行符
#续行符
# vars = '123' \
#        '456'
# print(vars)#'123456'

# \ 转义符，在字符出现的特定字符有着特定的意义
# \n  代表一个换行符
# vars = '岁月是把杀猪刀，\n\n但是它拿长得丑的人一点办法都没有。。。'

# \r 代表光标的位置（从\r出现的位置开始作为光标的起点）
# vars = '岁月是把杀猪刀，\r但是它拿长得丑的人一点办法都没有。。。'打印结果：但是它拿长得丑的人一点办法都没有。。。

# \t 水平制表符（table 缩进）
# vars = '岁月是把杀猪刀，\t但是它拿长得丑的人一点办法都没有。。。' 打印结果：岁月是把杀猪刀，	但是它拿长得丑的人一点办法都没有。。。

# \b 退格符
# vars = '岁月是把杀猪刀，\b但是它拿长得丑的人一点办法都没有。。。'打印结果：岁月是把杀猪刀但是它拿长得丑的人一点办法都没有。。。

# ！！！！！！！把转义字符作为普通字符输出,在字符串的前面加 r''
'''


#字符串的相关操作
'''
+ 字符串 + 操作
+ 字符串 * 操作
字符串 [] 切片操作
  + 字符串[开始值：结束值：步进值]
    开始值：默认为0，结束值默认是最后一个下标，步进值默认为1
    
# - 字符串 + 操作
vara = '君不见，黄河之水天上来，奔流到海不复回.'
varb = '君不见，高堂明镜悲白发，朝如青丝暮成雪'
# res = vara + varb
res = '将进酒 '+'李白'
# print(res)

# - 字符串 * 操作
# vars = '鸡你太美,' * 5
# print(vars)
# 鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美

# - 字符串 [] 切片操作 ****
# 字符串的索引操作，字符串中只能使用[]下标 访问，不能修改

0 1 2 3 4 5 6 7 8 9 10 ....
君不见，黄河之水天上来，奔流到海不复回
                    -4 -3 -2 -1

vars = '君不见，黄河之水天上来，奔流到海不复回'
# print(vars[5])
# print(vars[-5])

字符串的切片操作
str[开始值：结束值：步进值]
开始值：默认为0，结束值默认是最后一个下标，步进值默认为1
# print(vars)
# print(vars[5]) # 写一个值就是获取指定下标的元素
# print(vars[2:5]) # 从2下标开始取值，一直到下标5之前，能取到2，取不到5
# print(vars[4:8:2]) # 黄河之水 ==> 黄之
# print(vars[::]) # 从头取到尾
# print(vars[::2]) # 从头取到尾，每隔一个取一个
# print(vars[::-1])  # 字符串倒转过来
# print(vars[::-2])  # 字符串倒转过来，每隔一个取一个
# print(vars[1::])  # 不见，黄河之水天上来，奔流到海不复回
# print(vars[1::2])  # 不，河水上，流海复         
'''


# 字符串格式化的方法
'''
+ format
+ f

# 1 format  普通方式
a = '李白'
# vars = '{}乘舟将欲行，互闻岸上踏歌声'.format(a)
# vars = '{}乘舟将欲行，互闻岸上{}'.format(a,'踏歌声')

# 2 format  通过索引传参                     0   1   2
# vars = '{2}乘舟将欲行，互闻岸上{1}'.format('a','b','c')

# c='李白'
# b='踏歌声'
# vars = '{2}乘舟将欲行，互闻岸上{1}'.format(a,b,c) # 李白乘舟将欲行，互闻岸上踏歌声

# 3 format  关键字传参
# vars = '{a}乘舟将欲行，互闻岸上{b}'.format(a='李白',b='踏歌声')

# 4.1 format  容器类型数据传参
# vars = '豪放派：{0[0]} {1[0]}，婉约派：{0[1]} {1[1]}，蛋黄派：{0[2]} {1[2]}'.format(['李白','辛弃疾','达利园'],[1,22,333])
# 豪放派：李白 1，婉约派：辛弃疾 22，蛋黄派：达利园 333

# 4.2 format  容器类型数据传参
data = {'a':'辛弃疾','b':'蛋黄派'}
vars = '{a}乘舟将欲行，互闻岸上{b}'.format(**data)   # 括号中的a和b对应的是字典中的key

# data1 = ['李白','踏歌声']
# vars1 = '{}乘舟将欲行，互闻岸上{}'.format(*data1)  
# print(vars1)

# 4.3 format  容器类型数据传参  # python 3.7中新增的 格式化方法 f方法
data = {'a':'辛弃疾','b':'蛋黄派'}
vars = f'{data["a"]}乘舟将欲行，互闻岸上{data["b"]}'

# 限定小数的位数
# vars = '圆周率是多少：{:.2f}'.format(3.1415926)
# print(vars)
#{:.2f} 表示打印输出小数点保留两位小数；
#{:.0f}表示打印输出不保留小数位；
'''


# 字符串相关函数
# (一) 英文字符与字符检测相关函数
'''
vars = 'i love you'
# 返回字符串的副本，该字符串的首个字符大写，其余小写。
res = vars.capitalize() # I love you
# 把字符串中的每个单词的首字母大写
res = vars.title() # I Love You
# 把字符串全部改为 大写
res = vars.upper()
# 把字符串全部改为 小写
res = vars.lower()
# 字符串中的大小写字符转换，大写转小写，小写转大写
res = vars.swapcase()

# 检测字符串是否为全部大写字母组成
res = vars.isupper()
# 检测字符串是否为全部小写字母组成
res = vars.islower()
# 检测字符串是否符合标题title的要求#开头大写
res = vars.istitle()
# 检测字符串是否由数字和字母组成，如果字符串中包含来非数字字母的其它字符，则返回False
res = vars.isalnum()
# 检测字符串是否全部由字符(包含英文字符和中文)组成
res = vars.isalpha()
# 检测字符串是否由纯数字字符组成
res = vars.isdigit()
# 检测当前字符串是否为 空格 字符组成 ' '
res = vars.isspace()

# 检测字符串是否以指定的字符开始的，也可以指定开始和结束的位置
res = vars.startswith('y')
# res = vars.startswith('y',5)
# 检测字符串是否以 指定的字符 结束的，也可以指定开始和结束的位置
# res = vars.endswith('y')
res = vars.endswith('e',1,5)
'''


# （二）字符串 查找与操作相关函数 重点重点重点
'''
#  1.0.find() 方法 ，找到则返回字符中符合条件的第一个字符出现的索引位置。未找到返回 -1
res = vars.find('you')  #第一个字符的位置是0
# print(vars[res:res+3])

# 2.0.index() 方法
# res = vars.index('youe') # 找到则返回索引位置，未找到则报错 ValueError
# print(res)

# 3.0.split() 方法 可以按照指定的分隔符，把字符串分隔成列表
vars = 'user.txt_admin_id_123'
# res = vars.split('_') # ['user.txt', 'admin', 'id', '123'] #分解为num+1个从左到右
# res = vars.split('_',2)  # ['user.txt', 'admin', 'id_123']  #分解出来两个
# res = vars.split('_',1)  # ['user.txt', 'admin_id_123'] # 分解出来一个

# 4.0.rsplit() 方法是从右向左进行，从后向前
# res = vars.rsplit('_')  # ['user.txt', 'admin', 'id', '123'] #分解为num+1个从右到左
# res = vars.rsplit('_',2)  # ['user_admin', 'id', '123'] #分解为3个

# 5.0.join() 方法 ，使用指定的字符串，把一个容器中的元素链接成一个字符串
varlist = ['user.txt', 'admin', 'id', '123']
res = '_'.join(varlist)  #user.txt_admin_id_123

# 6.0.strip() 去除字符串左右两侧的指定字符 默认为空格或换行符
# rstrip() 去除字符串右侧的指定字符， lstrip() 去除字符串左侧的指定字符
vars = '  zhangsan  '
res = vars.strip(' ')
vars = '@admin'
res = vars.strip('@')

# 7.0.len() 函数可以获取当前字符串的长度
# print(len(vars))
# print(len(res))

# 8.0.replace() 替换函数
vars = 'iloveyou'
# 找到 love  替换为 live
res = vars.replace('love','live')

vars = 'aabbccddeeabcdef'
#  可以限制替换的次数
res = vars.replace('b','B',2)
# print(res)


'''

