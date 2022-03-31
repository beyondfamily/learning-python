import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.97.58',8888))
# 监听
server_socket.listen(5)
# 接收client的连接
client_socket,client_info=server_socket.accept()
# 接收client发送的消息
recv_data=client_socket.recv(1024)

print('接收到%s的小时：%s',client_info,recv_data.decode('gbk'))

client_socket.close()
server_socket.close()

