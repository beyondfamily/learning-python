import threading
import time

def worker():
    print(threading.currentThread().getName(),'Start')
    time.sleep(3)
    print(threading.currentThread().getName(),'Exit')

w=threading.Thread(name='worker',target=worker)
w.start()
print('start join')
w.join(2)
print('是否仍在工作?',w.is_alive())
time.sleep(2)
print('是否仍在工作?',w.is_alive())
print('end join')




