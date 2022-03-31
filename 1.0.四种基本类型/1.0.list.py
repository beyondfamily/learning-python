varlist = [192, 168, 200, 68]
# print(varlist,type(varlist))

# 列表中存储的数据可以是任意类型的
# 列表中存储的每一组数据，称为元素
varlist1 = ['a', 'b', 522, 'pai', 3.1451]
'''
正数  0   1   2    3     4 
   ['a','b',522,'pai',3.1451]
倒数 -5   -4  -3  -2     -1
'''
# print(varlist1[0],varlist1[-1])

# 列表中的元素可以也是一个列表
# 二位列表，二级列表
varlist2 = [1, 2, 3, [11, 22, 33], 'a', 'b', 'c']
print(varlist2[3])  # 读出[11,22,33]
print(varlist2[3][1])  # 读出11
