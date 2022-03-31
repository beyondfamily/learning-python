import threading, time, random, queue

bufSize = 10
q = queue.Queue(bufSize)


def producer():
    while True:
        if not q.full():  # 如果queue有空间
            item=random.randint(1,100)
            q.put(item)
            print('生产者Putting存入 %2s:queue数量 %s'%(str(item),str(q.qsize())))
            time.sleep(2)

def consumer():
    while True:
        if not q.empty():
            item=q.get()
            print('消费者Getting取得 %2s：queue数量 %s'%(str(item),str(q.qsize())))
            time.sleep(2)

p=threading.Thread(name='producer',target=producer)
c=threading.Thread(name='consumer',target=consumer)
p.start()
time.sleep(3.5)
c.start()
time.sleep(2)

