import socket

# 1. 创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 解决端口占用
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 2. 通信
s.connect(('192.168.215.58',8888))

# 3. 发送信息
while True:
    msg=input('>>').strip()
    if not msg:continue
    s.send(msg.encode('utf-8'))
    data=s.recv(1024)

# 4. 关闭
s.close()


