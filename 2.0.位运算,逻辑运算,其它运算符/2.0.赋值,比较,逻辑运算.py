# 赋值运算 与 逻辑运算

# 赋值运算
# a=20
# a+=20 #a=a+20
# a-=20 #a=a-20
# a*=20 #a=a*20

# 比较运算
# a=10
# b=20
# print(a==b)#是否等于
# print(a!=b)#是否不等于
# print(a<=b)

# 逻辑运算 and or not

a = True
b = False
print(a and b)
print(a or b)
print(a and not b)  # not优先级高 and优先级比or高
# print(20 and 30)#都有数据返回的是后一个数据

# print(10 or 20) #10
# print(20 or 10) #20
# print(0 or 20) #20
# print(20 or 0) #20
# 符合要求的真返回第一个

c = 0
d = 1
# 先执行的使not
print(c or not d)  # false
