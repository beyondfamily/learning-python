# 打印九九乘法表，矩阵，十二生肖

# 定义函数，打印九九乘法表
def jiujiu(n=0):
    #n这个参数控制正向输出还是反向输出
    if n==0:
        rs=range(1,10)
    else:
        rs=range(9,0,-1)
    for x in rs:
        for y in range(1,x+1):
            print(f'{x}x{y}={x*y}',end=' ')
        print()

jiujiu(1)

#封装打印矩形
def juxing(n,x,y):
    print('#'*x)
    for t in range(1, y+1):
        if n == 1:
            print('#'*x)
        elif n == 0:
            print('#'+' '*(x-2)+'# ')
    print('#'*x)

juxing(n=0,x=10,y=10)
print('\n')
juxing(n=1,x=10,y=10)