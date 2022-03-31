# json 序列化
'''
> JSON (JavaScript Object Notation)
> JSON 是一个受 JavaScript 的对象字面量语法启发的轻量级数据交换格式。
> JSON 在js语言中是一个对象的表示方法，和Python中的字典的定义规则和语法都很像
> JSON 在互联网中又是一种通用的数据交换，数据传输，数据定义的一种数据格式

+ json.dumps()  完成json格式数据的序列化
+ json.loads()    完成json格式数据的反序列化
+ json.dump()   和pickle模块的dump方法一样
+ json.load()      和pickle模块的load方法一样
'''
import json
# json数据格式：
data1={'name':'admin','age':20,'sex':'男'}
data2=[1,2,3]
data3=[
  {'name':'admin','age':20,'sex':'男'},
  {'name':'aa','age':21,'sex':'m'}
]
# json.dumps 用于将 Python 对象编码成 JSON 字符串
data=json.dumps(data3)
print(data)

# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
data4='{"a":1,"b":2,"c":3,"d":4,"e":5}'
text=json.loads(data4)
print(text)

with open('../../5.0.zipfile压缩模块/待压缩/1.0.json.json', 'w') as f:
    json.dump(data3,f)

with open('../../5.0.zipfile压缩模块/待压缩/1.0.json.json', 'r') as f:
    data_0=json.load(f)

print(data_0)
print(type(data_0)) # <class 'list'>


