"""
使用 BytesIO 读写字节
"""
from io import BytesIO

# 使用 BytesIO 写入内容
f = BytesIO()
# 将中文字符串编码为 utf-8 字节再写入
f.write("这是一行中文".encode('utf-8'))
# 打印内容
print(f.getvalue())
# b'\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe8\xa1\x8c\xe4\xb8\xad\xe6\x96\x87'

# 使用 BytesIO 读取内容
f = BytesIO(b'\xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\x80\xe8\xa1\x8c\xe4\xb8\xad\xe6\x96\x87')
s = f.read()
# 将读取的字节解码为 utf-8
print(s.decode(encoding="utf-8"))
# 这是一行中文
