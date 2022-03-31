# 其他运算符
s = 'iloveyoutosimida'
x = ['i', 'love', 'you']
y = ('i', 'love', 'you')
z = {'i', 'love', 'you'}
t = {1: 'i', 2: 'love', 3: 'you'}

print('love' in s)  # 检查 love字符是否在 s变量中
print('love' in x)
print('love' in y)
print('love' in z)

print(1 in t)  # 如果是字典类型只能检查 键
print('love' not in t)  # 检查love字符串不在t变量中
