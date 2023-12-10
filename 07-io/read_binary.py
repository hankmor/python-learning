"""
读取二进制文件
"""

# 读取二进制文件, 'rb' 为读取二进制文件模式
with open('avatar.gif', "rb") as f:
    s = f.read()
    print(type(s))  # <class 'bytes'>
    print(s)
# 输出字节的字符串形式: b'GIF89a\x87\x00...
