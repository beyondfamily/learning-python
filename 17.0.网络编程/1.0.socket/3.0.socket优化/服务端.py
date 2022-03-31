import socket

# 1. 创建socket     套接字的类型       基于TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2. 绑定ip 和 端口
s.bind(('192.168.215.58',8888))

# 3. 最大挂起的链接数 5
s.listen(5)

# 4. 等待链接
conn,client_addr=s.accept()

print(client_addr)

# 5. 收发消息
while True:  # 通信循环
    try:
        data=conn.recv(1024) # 收1024个字节 接收的最大数
        print('这是客户端的数据：',data.decode('utf8'))
        conn.send(data.upper())
    except ConnectionError:
        break


# 6. 结束通信
conn.close()

s.close()


