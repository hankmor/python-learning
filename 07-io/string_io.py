"""
stringio 读写字符串
"""
from io import StringIO

f = StringIO()
f.write("hello ")
f.write("python\n")
f.writelines("这是一行中文")

# 获取写入后的值
print(f.getvalue())

# 从 StringIO 读取内容
# 初始化
f = StringIO("哈哈, \n hello world!")
# 读取全部内容
s = f.read()
print(s)

# 前边的 StringIO 已经被读取过了，重新在创建一个
f = StringIO("哈哈, \n hello world!")
# 也可以逐行读取
while True:
    s = f.readline()
    if s == '':
        break
    print("line:", s)
