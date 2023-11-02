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

# 字符串是不可变的，即不可修改
str1 = 'string'
print(str1[0])  # s
# str[0] = 'S'  # TypeError: 'str' object does not support item assignment

# ==========
# 字符串支持切片操作
# ==========

'''
 +---+---+---+---+---+---+---+---+---+---+---+---+
 | h | e | l | l | o | , | p | y | t | h | o | n |
 +---+---+---+---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   9   10  11  12
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3   -2  -1  0
'''
print('---------- string 切片 ----------')
# 切片长度为后边的位置减前边的位置
str2 = "hello,python"
print(str2[2:3])  # 从位置2开始切到为位置3，长度为1
print(str2[:])  # 切整个字符串
print(str2[0:6])  # 从第1个字符开始，切到第5个字符（不包含第5个），hello
print(str2[6:12])  # 切取python
print(str2[-6:12])  # 从-6的位置开始切取python
print(str2[-6:])  # 效果同上
print(str2[-12:-7])  # 从右向左，-7的位置排除，此时是逗号','

# 获取字符串中的字符，如果下标越界则抛出异常
# print(str[13])  # IndexError: string index out of range
# 但是切片是可以自动处理越界
print(str2[0:15])  # hello,python

'''
字符串存储在字符串池中，只要池中有该字符，则直接获取，所以id相同
'''
# 切片后字符串的id
str1 = 'string'
print(str1, id(str1))
# 下标两个语句id相同
print(str1, id(str1[0:3]))
print(str1, id(str1[0:3]))

# unicode
ch = "【演唱会】2000-拉阔音乐会"
u = ch.encode("unicode_escape")  # 输出unicode编码后的字节
print(u)
print(type(u))  # <class 'bytes'>
s = u.decode("utf-8")
print(type(s))  # <class 'str'>
print(s)  # \u3010\u6f14\u5531\u4f1a\u30112000-\u62c9\u9614\u97f3\u4e50\u4f1a
# 先编码为latin-1，然后再加码为unicode，输出为中文：【演唱会】2000-拉阔音乐会
print(s.encode("latin-1").decode("unicode_escape"))
s = "\u3010\u6f14\u5531\u4f1a\u30112000-\u62c9\u9614\u97f3\u4e50\u4f1a"
print(s)  # 【演唱会】2000-拉阔音乐会
# 使用r或者R可以原样使用字符串
s = r"\u3010\u6f14\u5531\u4f1a\u30112000-\u62c9\u9614\u97f3\u4e50\u4f1a"
print(s)


# 格式化输出
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# python 格式化与C类似，用 format % (参数列表) 的形式格式化输出字符串，如果只有一个参数可以省略括号
s = "hello, %s" % "python"
print(s)  # hello, python
s = "you spend $%.2f, price: %.2f, number: %d" % (3.14, 3.14, 9)
print(s)  # you spend $3.14, price: 3.14, number: 9
fmt = "%-10s %-10s"
title = fmt % ("format", "desc")
print(title)
print(fmt % ("%d", "整数"))
print(fmt % ("%f", "浮点数"))
print(fmt % ("%s", "字符串"))
print(fmt % ("%x", "十六进制整数"))
# format     desc
# %d         整数
# %f         浮点数
# %s         字符串
# %x         十六进制整数
print("%x" % 10)  # 十六进制，a
print("%o" % 10)  # 八进制，12
# 使用format函数格式化字符串，使用{num}占位
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format(
    '小明', 17.125))  # Hello, 小明, 成绩提升了 17.1%
# 使用f开头的字符串格式化，通过{}引入变量的值并进行格式化
r = 2.5
s = 3.14 * r ** 2
# The area of a circle with radius 2.5 is 19.62
print(f'The area of a circle with radius {r} is {s:.2f}')
