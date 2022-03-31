import socket

# 创建UDP socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 创建接受信息地址
addr=('192.168.97.58',8888)
# 接收信息
msg=input('请输入数据:')
# 用sendto发送
s.sendto(msg.encode('gbk'),addr)

s.close()





