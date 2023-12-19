import socket

# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务端
s.connect(('127.0.0.1', 8080))
# 接收欢迎消息
welcome = s.recv(1024)
# 打印欢迎消息
print(welcome.decode('utf-8'))
# 发送三条数据
for x in ['hank', 'jason', 'jimmy']:
    # 发送到服务端
    s.send(x.encode('utf-8'))
    # 接收服务端响应
    data = s.recv(1024)
    print("received data from server: %s" % data.decode('utf-8'))
# 发送退出消息
s.send(b'exit')
s.close()
