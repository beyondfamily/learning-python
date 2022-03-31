import random,time,threading

def waiter(event,loop):
    for i in range(loop):
        print('%s 等待flag被设定'%(i+1))
        event.wait()                   # 等待flag
        print('等待完成时间：',time.ctime())
        event.clear()                  # 重置flag
        print()

def setter(event,loop):
    for i in range(loop):
        time.sleep(random.randint(2,5))
        event.set()             # 设立flag

event=threading.Event()
loop=random.randint(6,8)

w=threading.Thread(target=waiter,args=(event,loop))
w.start()
s=threading.Thread(target=setter,args=(event,loop))
s.start()
w.join()
s.join()
print('工作完成')







