import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定一个本机端口
s.bind(('192.168.97.58',8989)) # 绑定的是本机 端口号是8989
# 接收信息
recv_msg=s.recvfrom(1024)
print('接收到%s的消息是:%s'%(recv_msg[1],recv_msg[0].decode('gbk')))

s.close()




