# 字典是键值对的存储方式  name:admin
# 键必须是字符串或数字类型，值可以是任意类型的
# 键名不可重复，值可以重复
vard = {'title': '<<鬼谷子>>', 'author': '鬼谷子', 'price': '29.99'}
# print(vard,type(vard))#{'title': '<<鬼谷子>>', 'author': '鬼谷子', 'price': '29.99'} <class 'dict'>


# 获取字典中的值
print(vard['title'])
print(vard.get('title'))

