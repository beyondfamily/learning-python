import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('192.168.97.58',8888))

while True:
    # 客户端发送消息
    msg=input('>>>')
    client_socket.send(msg.encode('gbk'))
    # 客户端接收消息
    recv_data=client_socket.recv(1024)
    print('服务器端说：',recv_data.decode('gbk'))





