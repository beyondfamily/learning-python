# 这个程序会对全局变量进行存取,为了保护处理原则,存取前先锁定全局变量,处理完成后再解锁

import threading,logging,random,time
# 1.0.锁
# class MyThread(threading.Thread): # 这是threading.Thread的自类别
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#
#     def run(self): # 定义线程工作
#         global data
#         datalock.acquire()  # 锁定
#         data=data+5
#         print('data=',data)
#         datalock.release()  # 解锁
#
#
# data=10
# datalock=threading.Lock() # 建立对象
# ts=[]
# for t in range(10):
#     t=MyThread()
#     ts.append(t)   # 加入线程列表
# for t in ts:
#     t.start()      # 启动所有线程
# for t in ts:       # 等待所有线程退出
#     t.join()


# 2.0.锁死
# logging.basicConfig(level=logging.DEBUG)
# datalock=threading.Lock()  # Lock对象
# datalock.acquire()         # 进入锁定
# logging.debug('Enter locked mode')
# datalock.acquire()         # 进入锁死程序 如果再次锁定 就会产生锁死，造成程序错误
# datalock.release()
# datalock.release()


# 3.0.资源锁定与解锁 Threading.RLock
# logging.basicConfig(level=logging.DEBUG)
# datalock=threading.RLock()      # RLock对象
# datalock.acquire()              # 进入锁定
# logging.debug('Enter locked mode')
# datalock.acquire()              # 不会死锁
# logging.debug('Trying to locked again')
# datalock.release()
# datalock.release()

# 4.0.高级锁定 threading.Condition
'''
这是python的另一种锁定,就像它的名称一样是可以有条件(condition),首先程序使用acquire()
进入锁定状态,如果需要符合一定的条件才处理数据,此时可以使用wait(),让自己进入睡眠状态
程序设计时需要用notify()通知其它线程,然后放弃锁定release()

上述而言,若再增加了一个消费之可以使用notifyAll()通知

'''
def producer():
    while True:
        condition.acquire()
        if len(data)>=5:
            print('生产线是 waiting...')
            condition.wait()
        else:
            data.append(random.randint(1,100))
            print('生产线库存--',data)
            time.sleep(1)
        condition.notify()
        condition.release()

def consumer():
    while True:
        condition.acquire()
        if not data:
            print('消费者是 waiting...')
            condition.wait()
        else:
            print('消费者取走商品：',data.pop(0))
            print('目前库存：',data)
            time.sleep(1)
        condition.notify()
        condition.release()

condition=threading.Condition()
data=[]

p=threading.Thread(name='producer',target=producer)
c=threading.Thread(name='consumer',target=consumer)

p.start()
c.start()
p.join()
c.join()



