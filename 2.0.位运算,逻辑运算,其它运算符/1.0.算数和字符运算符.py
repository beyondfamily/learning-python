# 算术运算符
a = 10
b = 15
print(b // a)  # 取整
print(2 ** 3)  # 幂次方
print(b % a)  # 求余数

# 1.字符串与数字不能直接参与运算
# 2.字符串和字符串使用+结果是字符串的拼接
# '1'+2 !错的
print('-' * 10)  # 结果 ----------

# 关于字符串的拼接
l = 'love'
i = 'i ' + l + ' you'
x = f'i {l} you'  # 前面必须加 f 否则认读不出来{} #f为format的缩写
y = 'i {l} you'.format(l=l)  # 传递信息
t = 'i {} you'.format(l)

print(i)
print(x)
print(y)
print(t)
