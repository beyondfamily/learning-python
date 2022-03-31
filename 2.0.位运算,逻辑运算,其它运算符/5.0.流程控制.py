# year = int(input('请输入四位数的年份:'))
# print(year, type(year))

vars = 'abcdefg'
vars1 = [1, 2, 3, 4, 5]
for i in vars1:
    print(i, end=' ')

for i in range(0, 10):  # 左闭右开
    print(i, end=' ')
# range()是一个函数，返回一个迭代对象

# break 结束，跳出
# continue 跳过
# pass 占位

# num = 0
# while num <= 10:
#     num += 1
#     if num % 2 == 0:
#         continue  # 跳过本次循环，继续执行下一次
#     else:
#         print(num)
#     if num==7:
#         break   #跳出循环，后面不在执行，结束循环


# 1.exit()和quit()是直接退出程序
num = 1
while num <= 100:
    print('⭐', end=' ')
    # 判断是否需要换行
    if num % 10 == 0:
        print()
    num += 1

# 九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{x}X{y}={x * y}', end=" ")

    print()  # 默认为换行
# 反向输出九九乘法表
# for x in range(9,0,-1):
#     for y in range(1,x+1):
#         print(f'{x}X{y}={x * y}', end=" ")
#
#     print()

# 斐波那契数
num = int(input('你需要计算到第几项：'))

n1 = 1
n2 = 1
count = 2
if num <= 0:
    print('请输入一个正数')
elif num == 1:
    print(f'斐波那契数列:{n1}')
else:
    while count < num:
        n3 = n1 + n2
        print(n3, end=" ")
        # 更新数据
        n1, n2 = n2, n3
        count += 1
