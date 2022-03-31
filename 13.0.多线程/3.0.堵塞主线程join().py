import threading
import time

def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(),'Exit')

w=threading.Thread(name='Worker',target=worker)
w.start()
print(' start join')
w.join(2) # 里面的数字是时间 当时间恢复到主线程恢复工作 可以不填写
print('end join')

