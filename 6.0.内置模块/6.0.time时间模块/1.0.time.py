import time
'''
概念：
    1。 时间戳： 1574905882.6581771 表示从1970年1月1日0时0分0秒到现在的一个秒数，目前可以计算到2038年
    2。 时间字符串： Thu Nov 28 09:54:08 2019
    3。 时间元组： time.struct_time(tm_year=2019, tm_mon=11, tm_mday=28, tm_hour=9, tm_min=55, tm_sec=32, tm_wday=3, tm_yday=332, tm_isdst=0)
'''
# *** 1. 获取当前系统的时间戳
res = time.time() # 1646399021.1971083

# 2. 获取当前系统时间，时间字符串
res = time.ctime() # Fri Mar  4 21:03:54 2022

# 3. 获取当前系统时间， 时间元组
res = time.localtime() # time.struct_time(tm_year=2022, tm_mon=3, tm_mday=4, tm_hour=21, tm_min=4, tm_sec=5, tm_wday=4, tm_yday=63, tm_isdst=0)

# 4. 以上时间字符串和时间元组可以通过指定的时间戳来获取
t = 1564000082.6581771
res = time.ctime(t) # Thu Jul 25 04:28:02 2019
res = time.localtime(t) # time.struct_time(tm_year=2019, tm_mon=7, tm_mday=25, tm_hour=4, tm_min=28, tm_sec=2, tm_wday=3, tm_yday=206, tm_isdst=0)

# 5. 使用localtime方法获取的时间元组，如何格式化成为 xxxx年xx月xx日 时：分：秒  星期几
print(f'{res.tm_year}年{res.tm_mon}月{res.tm_mday}日 {res.tm_hour}：{res.tm_min}：{res.tm_sec} 星期{res.tm_wday+1}')

# *** 6. strftime() 格式化时间 年-月-日  时：分：秒 星期几
res = time.strftime('%Y-%m-%d %H:%M:%S %w')  # 2019年7月25日 4：28：2 星期4

# *** 7. sleep(秒) 在给定的秒数内暂停调用线程的执行。该参数可以是浮点数，以指示更精确的睡眠时间。
print(time.strftime('%Y-%m-%d %H:%M:%S %w')) # 2022-03-04 21:06:26 5
time.sleep(3)
print(time.strftime('%Y-%m-%d %H:%M:%S %w')) # 2022-03-04 21:06:29 5

# *** 8.计算程序的运行时间
res=time.perf_counter() # 3.0565643

# 100万次的字符串比较 需要执行的时间
start = time.perf_counter()
for i in range(1000000):
    if 'abc' > 'acd':
        pass
end = time.perf_counter()
print(end-start) # 0.044901199999999974

start = time.perf_counter()
for i in range(1000000):
    if 103 > 100 :
        pass
end = time.perf_counter()
print(end-start) # 0.03959769999999985

