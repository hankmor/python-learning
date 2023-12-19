import socket

# 创建 socket，使用 ipv4 和 udp 协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8080))
print("udp server started on port 8080")
while True:
    # 返回数据和客户端的地址与端口, 后边可以直接调用 sendto 方法发送数据
    data, addr = s.recvfrom(1024)
    print('received data from client %s: %s' %(addr, data.decode('utf-8')))
    # sendto 发送消息给客户端，不保证客户端能够成功收到
    s.sendto(b'hello %s' % data, addr)
