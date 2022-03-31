# 随机模块 random
import random
# random.random()  返回 0 - 1 之间的随机小数 (左闭右开)
res = random.random()


# random.randrange([开始值]，结束值，[步进值]) 随机获取指定范围内的整数
res = random.randrange(5) # 一个参数，从0到整数之间的值，左闭右开
res = random.randrange(5,10) # 两个参数，从第一个值到第二个值之间的随机数，左闭右开
# res = random.randrange(5,10,2) # 三个参数，按照指定步进值从第一个值到第二个值之间的随机数，左闭右开
# 随机数的应用场景：数字验证码，高并发下的订单号。。。

# random.randint() 随机产生指定范围内的随机整数
res = random.randint(5,10)

# random.uniform() 获取指定返回内的随机小数
res = random.uniform(5,10)

# random.choice() 随机获取容器类型中的值
res = random.choice('123')
res = random.choice([1,2,3,4])

# random.shuffle() 随机打乱当前列表中的值,没有返回值，直接打乱原数据
arr = [1,2,3,4,5]
res = random.shuffle(arr)






