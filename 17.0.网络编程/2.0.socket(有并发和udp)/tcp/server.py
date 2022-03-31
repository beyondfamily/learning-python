import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.97.58',8888))
server_socket.listen()
client_socket,client_info=server_socket.accept()
while True:
    # 接收客户端消息
    recv_data=client_socket.recv(1024)
    print('客户端说：',recv_data.decode('gbk'))
    # 发送信息
    msg=input('>>>')
    client_socket.send(msg.encode('gbk'))







