# 实现递归
def digui(num):
    print(num, end=' ')
    if num > 0:
        digui(num - 1)
    print(num, end=' ')


digui(3)  # 3 2 1 0 0 1 2 3


# 实现阶乘
def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n - 1)


res = jiecheng(7)
print(res)


# 实现斐波那契数列
def feibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feibo(n - 1) + feibo(n - 2)


res = feibo(6)
print(res)
