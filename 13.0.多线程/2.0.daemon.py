import threading,time

def daemonFun():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(),'Exiting')

def non_daemonFun():
    print(threading.currentThread().getName(),'Starting')
    print(threading.currentThread().getName(),'Exiting')

d=threading.Thread(name='daemon',target=daemonFun)
d.setDaemon(True) # 为true的时候其它非daemon程序结束则为True的程序就会结束
nd=threading.Thread(name='non_daemonFun',target=non_daemonFun)

d.start()
nd.start()





