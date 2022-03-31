import socket

# 1. 创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2. 通信
s.connect(('192.168.215.58',8888))

# 3. 发送信息
s.send('hello xubaoke'.encode('utf-8'))

data=s.recv(1024)
print(data)

# 4. 关闭
s.close()


