import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect(('192.168.215.58',8888))


while True:
    msg=input('>>').strip()
    if not msg:continue
    s.send(msg.encode('utf-8'))
    data=s.recv(1024)


s.close()


