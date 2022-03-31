'''
序列化是指可以把python中的数据，以文本或二进制的方式进行转换，并且还能反序列化为原来的数据
数据在程序与网络中进行传输和存储时，需要以更加方便的形式进行操作，因此需要对数据进行序列化
对数据进行序列化的主要方法有以下两种

 + 二进制序列化模块 pickle  （python专用）
 + 文本序列化模块 json       （互联网通用）
'''
# pickle 序列化
'''
+ dumps() 序列化，可以把一个python的任意对象序列化成为一个二进制
  + 返回一个序列化后的二进制数据 
  + pickle.dumps(var)
+ loads() 反序列化，可以把一个序列化后的二进制数据反序列化为python的对象
  + 返回一个反序列化后的python对象  
  +  pickle.loads(var)

+ dump() 序列化，把一个数据对象进行序列化并写入到文件中
  + 参数1，需要序列化的数据对象
  + 参数2，写入的文件对象
  + pickle.dump(var,fp)
+ load() 反序列化，在一个文件中读取序列化的数据，并且完成一个反序列化
  + 参数1，读取的文件对象
  +  pickle.load(fp)
'''
import pickle
# dump()和load()主要操作文件
# pickle可以将对象以文件的形式存放在磁盘上。
# python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}
with open('1.0.data.pickle', 'wb') as f:
    # 将 data以pickle形式写入文件
    # pickle.HIGHEST_PROTOCOL=5 决定选用什么模式
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

with open('1.0.data.pickle', 'rb') as f:
    data2 = pickle.load(f)
print(data2)


class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(self.name+"_"+str(self.age))

aa = Person("JGood", 2)
with open('1.0.person.txt', 'wb') as f:
    pickle.dump(aa,f,0)


with open('1.0.person.txt', 'rb') as f:
    data3=pickle.load(f)
data3.show()

var=[1,2,3,4,5,6]
t1=pickle.dumps(var)
print(t1)
t2=pickle.loads(t1)
print(t2)

