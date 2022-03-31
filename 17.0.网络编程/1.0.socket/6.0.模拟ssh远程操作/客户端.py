import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect(('192.168.97.58',8888))


while True:
    cmd=input('>>').strip()
    if not cmd:continue
    s.send(cmd.encode('utf-8'))
    data=s.recv(2048) # 1024是一个坑
    print(data.decode('gbk'))

s.close()


