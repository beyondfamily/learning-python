import threading,time

# 1.0.不带参数
# def wakeUp():
#     print('threadObj线程开始')
#     time.sleep(10)
#     print('threadObj线程结束')
#
# print('程序阶段1')
# threadObj=threading.Thread(target=wakeUp)
# threadObj.start()
# time.sleep(1)
# print('程序阶段2')


# 2.0.带参数
# def wakeUp(name,blessingWord):
#     print('threadObj线程开始')
#     time.sleep(10)
#     print(name,' ',blessingWord)
#     print('threadObj线程结束')
#
#
# print('程序阶段1')
# threadObj=threading.Thread(target=wakeUp,args=['小明','生日快乐'])
# threadObj.start()
# time.sleep(1)
# print('程序阶段2')


# 3.0.参看线程名
# def worker():
#     print(threading.currentThread().getName(),'Starting')
#     time.sleep(2)
#     print(threading.currentThread().getName(),'Exiting')
#
# def manager():
#     print(threading.currentThread().getName(),'Starting')
#     time.sleep(3)
#     print(threading.currentThread().getName(),'Exiting')
#
#
# m=threading.Thread(target=manager)
# w=threading.Thread(target=worker)
#
# m.start()
# w.start()


# 4.0.自行命名线程名
def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(),'Exiting')

def manager():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(),'Exiting')

m=threading.Thread(target=manager)
w=threading.Thread(target=worker)
w2=threading.Thread(name='Manager',target=worker)

m.start()
w.start()
w2.start()


