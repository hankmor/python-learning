"""
Python没有专门处理字节的数据类型,但由于 b'str' 可以表示字节，所以，字节数组＝二进制str。
而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
"""
import struct

# 把一个32位无符号整数变成字节，也就是4个长度的bytes

# ================================================
# 字节运算法
# ================================================

n = 10240099
# 取高8位为第一个字节(8位)，高 8 位为1，其他位为 0, 11111111 00000000 00000000 00000000
b1 = (n & 0xff000000) >> 24
# 取次高位的一个字节(8位), 11111111 00000000 00000000
b2 = (n & 0xff0000) >> 16
# 取次地位的一个字节(8位), 11111111 00000000
b3 = (n & 0xff00) >> 8
# 取低位的一个字节(8位), 11111111
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)  # 字节的字符串表示: b'\x00\x9c@c'

# ================================================
# 使用 int.to_bytes 方法
# ================================================

# 也可以使用 int.to_bytes 方法直接转换为字节, length 为字节长度, byteorder 为字节顺序: big 为大端序， little 为小端序
print(int.to_bytes(n, length=4, byteorder='big', signed=True))  # b'\x00\x9c@c'
print(int.from_bytes(b'\x00\x9c@c', byteorder='big', signed=True))  # 10240099
print(int.to_bytes(n, length=4, byteorder='little', signed=True))  # b'c@\x9c\x00'
print(int.from_bytes(b'c@\x9c\x00', byteorder='little', signed=True))  # 10240099

# ================================================
# Python 还提供了一个 struct 模块来解决bytes和其他二进制数据类型的转换
# ================================================

# pack的第一个参数是处理指令:
# '>': 大端序（网络序）
# '<': 小端序
# 'I': 表示4字节无符号整数
b = struct.pack('>I', 10240099)  # b'\x00\x9c@c'
print(b)
i = struct.unpack('>I', b'\x00\x9c@c')
print(i)  # (10240099,)
# IH 的含义为: 转换时后面的bytes依次变为I：4字节无符号整数 和 H：2字节无符号整数。
i = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(i)  # (4042322160, 32896)
