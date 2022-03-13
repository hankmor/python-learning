s1 = "aaa"
s2 = "bbb"
print(s1 + s2)  # 字符串连接
# 字符串可以定义为单引号、双引号和三引号
s3 = 'hello'
s4 = 'world'
print(s3 + s4)
# 可以使用 乘法来多次重复字符串
print(s1 * 3)  # aaaaaaaaa

# 可以将相邻的两个字符串自动拼接
print('aaa '
      'bbb')  # aaa bbb

# 三引号可以多行，每一行自动加换行，如果不需要加换行，可以输入\
print("""hello
world,
hello, python
""")
print('''hello\
world,\
hello, python
''')  # helloworld,hello, python

# 字符串支持下标访问，负数下标则从右边开始访问
s5 = 'hello'
print(s5[0], s5[1], s5[2])  # h e l
print(s5[-1], s5[-2])  # o l

# ==========
# 转义字符
# ==========
# 制表符
print("aaa\tbbb")  # aaa bbb
# 换行符
print("aaa\nbbb")  # 换两行输出
# 回车符
print("aaa\rbbb")  # bbb
# 退格符
print("aaa\bbbb")  # aabbb
