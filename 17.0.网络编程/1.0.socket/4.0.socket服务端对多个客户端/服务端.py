import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('192.168.215.58',8888))
s.listen(5)

print('starting...')
while True: # 链接循环
    conn,client_addr=s.accept()
    print(client_addr)


    while True:  # 通信循环
        try:
            data=conn.recv(1024)
            print('这是客户端的数据：',data.decode('utf8'))
            conn.send(data.upper())
        except ConnectionError:
            break
    conn.close()


s.close()


