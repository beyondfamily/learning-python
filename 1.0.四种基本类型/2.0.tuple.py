# 元组用()列表用[]
# 元组的值无法改变
vart = (1, 2, 3, 'a', 'b')
print(vart, type(vart))

vart = ('abc')  # 结果为字符串
vart = (123)  # 结果为数字
# 如果元组中只有一个元素，那么需要加逗号 ,
vart = ('abc',)
print(type(vart))

# 元组定义的其他方式
vart1 = 1, 2, 3, 4
print(type(vart1))
'''
1.列表使用中括号定义
2.元组使用小括号定义
3.列表的值可以改变
4.元组的值不可以改变
'''
# 定义列表
list1 = [1, 2, 3]
list1[2] = 22
print(list1)
