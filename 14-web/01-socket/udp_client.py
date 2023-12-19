import socket

# 创建 udp socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for x in ['hank', 'jason', 'jimmy']:
    # 给服务端发送消息，不保证服务端能够成功收到
    s.sendto(x.encode('utf-8'), ('127.0.0.1', 8080))
    # 接收服务端返回的数据并打印
    print(s.recv(1024).decode('utf-8'))
# 关闭连接
s.close()
