import socket
import subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('192.168.97.58',8888))
s.listen(5)

print('starting...')
while True: # 链接循环
    conn,client_addr=s.accept()
    print(client_addr)


    while True:  # 通信循环
        try:
            # 1. 收到命令
            cmd=conn.recv(1024)
            print('这是客户端的数据：',cmd.decode('utf8'))

            # 2. 执行命令,拿到结果
            obj=subprocess.Popen(cmd.decode('utf-8'),
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE
                                 )
            stdout=obj.stdout.read()
            stderr=obj.stdout.read()
            # 3. 把命令的结果返回给客户端
            conn.send(stdout+stderr) # +是一个可以优化的点
        except ConnectionError:
            break
    conn.close()


s.close()


