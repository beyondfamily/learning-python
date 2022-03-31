import threading,time

def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(),'Exiting')

def manager():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(),'Exiting')

w=threading.Thread(name='worker',target=worker)
w.start()
print('worker start join')
w.join(1.5)
print('worker start join')
m=threading.Thread(name='manager',target=manager)
m.start()
print('manager start join')
m.join(2)
print('manager end join')
print('目前共有%d线程在工作'%threading.active_count())
for thread in threading.enumerate():
    print('线程名称：',thread.name)






