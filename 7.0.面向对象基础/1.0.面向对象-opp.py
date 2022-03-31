'''
 类名的书写规范，建议使用驼峰命名发
    大驼峰：MyCar XiaoMi
    小驼峰：myCar xiaoMi

一个类具有特征和功能两个内容组成：
    特征就是一个描述：颜色：白色，品牌：奥迪，排量：2.4L。。。
    功能就是一个能力：拉货，带美女兜风。。。

    特征在编程中就是一个变量，在类中称为 属性
    功能在编程中就是一个函数，在类中称为 方法

类中属性一般定义在前面，方法定义在后面
'''


# 定义一个汽车的类
class Cart():
    # 属性《==》特征《==》变量 通称
    color = '白色'  # 颜色
    brand = '艾迪'  # 品牌
    pailiang = 2.4  # 排量

    # 方法《==》功能《==》函数  通称
    def lahuo(self):
        print('小汽车能拉货')

    def doufeng(self):
        print('小汽车能兜风')

    def bamei(self):
        print('带妹子去嗨')

    def __len__(self):

        return 10

# 如何去使用这个类？
# 通过类实例化一个对象
obj=Cart()

#调用对象的方法
obj.bamei()

#获取对象的属性
print(obj.brand)



