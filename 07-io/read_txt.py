"""
读取文本文件

python open 函数文档: https://docs.python.org/3/library/functions.html#open
打开文件的模式：
1、'r': 只读打开（默认）
2、'w': 以写入的方式打开，文件已经存在则会清空并重新写入
3、'x': 以独占创建的方式打开文件，存在则出错
4、'a': 以追加写入的方式打开，存在则追加
5、'b': 打开二进制文件
6、't': 文本文件模式(默认)
7、'+': 以更新的方式打开(读和写都支持)
默认情况下，r 等同于 rt，w+和w+b都会清空已有文件, r+和r+b则不会清空已有文件
"""

# with 语句简化了文件流的打开和关闭，自动调用 f.close()，相当于 try except finally
with open('demo.txt', 'r') as f:
    s = f.read()  # 读取文件中的所有内容，返回一个字符串
    print(s)

# r.readlines()一次读取所有内容并按行返回，读取配置文件的时候非常有用
with open('demo.txt', 'r') as f:
    ls = f.readlines()
    for line in ls:
        # 由于文本文件每一行末尾有换行符 '\n'，所以需要去掉它
        print("line:", line.strip())

# 读取文本文件时可以指定字符串编码, 不指定默认为系统编码，按照 gbk 编码来编解码文件
# 如果编码不匹配，抛出 UnicodeDecodeError
# with open('demo.txt', 'r', encoding='gbk') as f:
# errors参数为一个字符串，指定当出现编码错误时如何处理错误，包括 'strict' 严格抛出 ValueError 及其子类, ‘ignore’ 忽略错误
with open('demo.txt', 'r', encoding='gbk', errors='ignore') as f:
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0x87 in position 37: incomplete multibyte sequence
    # s = f.read()
    # 文本文件为 utf8 编码，按照 gbk 来读取时编码不匹配，如果忽略错误则打印乱码
    s = f.read()
    print(s)
    # 鏉ヤ竴鐐逛腑鏂
