import socket
from threading import Thread


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.97.58',8989))

# 接收
def recv_fun():
    while True:
        recv_data=s.recvfrom(1024)
        print('>>%s:%s'%(recv_data[1],recv_data[0].decode('gbk')))

# 发送
def send_fun():
    while True:
        addr=('192.168.97.58',8888)
        data=input('<<:')
        s.sendto(data.encode('gbk'),addr)


if __name__=='__main__':
    # 创建两个线程
    t1=Thread(target=send_fun)
    t2=Thread(target=recv_fun)
    t1.start()
    t2.start()




