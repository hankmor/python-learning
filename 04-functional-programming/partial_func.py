"""
使用 functools 包定义偏函数
"""


# int 函数将字符串转换为整数，默认按照十进制转换
import functools


x = int('12345')
print(x)
# 可以指定 base 参数设置给定参数的进制
x = int('1101', base=2)
print(x)  # 13
x = int('12345', base=8)
print(x)  # 5349
x = int('12345', base=16)
print(x)  # 74565


# 如果有大量的二进制字符串需要转换为 int，每次设置 base=2 会很麻烦，可以自定义一个函数 int2，指定默认的 base 参数为 2
def int2(s, base=2):
    return int(s, base)


print(int2('1'))  # 1
print(int2('10'))  # 2
print(int2('11'))  # 3
print(int2('100'))  # 4
print(int2('101'))  # 5
print(int2('110'))  # 6


# 其实，functools 包下的 partial 方法已经为我们做了这件事情，它接收一个函数作为参数，并可以指定该函数的参数列表并为其指定默认值
int2 = functools.partial(int, base=2)
print(int2('1'))  # 1
print(int2('10'))  # 2
print(int2('11'))  # 3
print(int2('100'))  # 4
print(int2('101'))  # 5
print(int2('110'))  # 6
