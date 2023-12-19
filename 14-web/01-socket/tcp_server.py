import socket

p = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口
s.bind(('127.0.0.1', p))
# 开启监听，客户端可以连接，参数为最大的客户端连接数量
s.listen(5)
print("server started on port: %d" % p)
while True:
    # 等待客户端连接, conn 表示当前建立的 tcp 连接通道， addr 为客户端地址
    conn, addr = s.accept()
    print("client connected from %s:%s " % (addr[0], addr[1]))
    # 发送欢迎消息
    conn.send(("welcome, %s:%s" % (addr[0], addr[1])).encode('utf-8'))
    # 接收客户端数据
    while True:
        data = conn.recv(1024)
        # 没有数据或者发送 exit 退出循环，不再接收数据
        if not data or data.decode('utf-8') == 'exit':
            break
        else:
            conn.send(("hello, %s" % data.decode('utf-8')).encode('utf-8'))
    # 关闭连接
    conn.close()
    print("connection closed from %s:%s" % (addr[0], addr[1]))
