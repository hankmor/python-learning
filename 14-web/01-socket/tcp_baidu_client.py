"""
tcp 请求新浪服务器
"""
import socket

# 创建socket, AF_INET 表示 ipv4, SOCK_STREAM 表示用 tcp 连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))
# 发送数据，这里使用 http协议请求头发送 GET 请求,
# 注意:
# 1、请求头和 body 之间有一个空行，发送的是字节
# 2、要设置Content-Type请求头，编码为 utf-8，否则返回的数据可能乱码
s.send(b'''GET / HTTP/1.1
Host: www.baidu.com
Connection: close
Content-Type: text/html;charset=UTF-8
Accept: text/html,application/xhtml+xml


''')
# 接收服务器返回的数据
buff = []
while True:
    # 最次最多接收 1k 数据
    d = s.recv(1024)
    if d:
        buff.append(d)
    else:  # 接收完成x
        break
data = b''.join(buff)
print(str(data))
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('baidu.html', 'wb') as f:
    f.write(html)
# 关闭socket
s.close()
