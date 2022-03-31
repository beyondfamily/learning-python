import time
import threading

semaphore=threading.BoundedSemaphore(5) # 限制计数器最大值

def func():
    if semaphore.acquire():
        print(threading.currentThread().getName()+' 取得锁')
        print('Working...')
        time.sleep(2)
        semaphore.release()
        print(threading.currentThread().getName()+' 释放锁')

for i in range(10):
    t=threading.Thread(target=func)
    t.start()

