"""
写入文本文件
"""

# 'w' 模式会清空原文件重新写入, 相当于删了重新创建
with open("write.txt", "w") as f:
    f.write("hello ")
    f.write("world\n")
    f.writelines("hello python!")
    f.write("\n")

# 如果想再文件后追加内容，可以使用 'a' 模式，a 表示 append
with open("write.txt", "a") as f:
    f.writelines("new content\n")

# 如果以不同的编码写入，可以指定 encoding 参数, 此时我的 mac 电脑文件时 utf8 编码，打开后可以看到乱码
with open("write.txt", "w", encoding='gbk') as f:
    f.write("写一行中文")

# 同样按照 gbk 读取，能够成功读取
with open("write.txt", "r", encoding='gbk') as f:
    s = f.read()
    print(s)
    # 写一行中文
