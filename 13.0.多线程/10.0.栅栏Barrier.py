import random,time,threading
'''
当线程抵达时,需要等待其它线程,当所有线程抵达是,才放开栅栏，这些线程才可以往下执行
'''


def player():
    name=threading.current_thread().getName()
    time.sleep(random.randint(0,5))
    print('%s 抵达栅栏时间：%s'%(name,time.ctime()))
    b.wait()

b=threading.Barrier(4)
print('比赛开始')
for i in range(4):
    t=threading.Thread(target=player)
    t.start()
for i in range(4):
    t.join()

print('比赛结束')
