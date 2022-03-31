class Cart():
    color='白色'
    brand='艾迪'
    pailiang=2.4


    def lahuo(self):
        print('小汽车能拉货')

    def doufeng(self):
        print('小汽车能兜风')

    def bamei(self):
        print('带妹子去嗨')


# 在类的外部，可以直接通过对类对成员进行操作
# 1.类成员属性的操作
a=Cart()
# 访问成员属性
print(Cart.brand) # 艾迪
# 修改类成员属性
Cart.brand='宝马'
print(Cart.brand) # 宝马
print(a.brand) # 宝马
# 给类添加成员属性
Cart.name='A6'
# 通过类创建的对象是否也有这个属性呢？之前创建的对象和之后创建的对象都会有这个属性
print(Cart.name) # A6

# 思考，如果通过类把属性进行修改，那么在通过这个类实例化的对象，它的属性是什么呢？那这群创建的对象呢？
b=Cart()

# 删除类的成员:在之前和之后创建的对象，都不在有这个属性了
# del Cart.name
# print(a.name)




