# bin 输出二进制字符串
x = bin(10)
print(type(x))  # <class 'str'>
print(x)  # 0b1010

# int(x [,base]) 将x转为整数，x必须为整数或者字符串，如果提供了进制，
# 则x为字符串，且字符串必须与之对应，否则可能报错
print(int("11", 2))  # 3
print(int("11", 10))  # 11
print(int("11", 8))  # 9
print(int("11", 16))  # 17
print(int("11"))  # 11，不给定进制，默认为10进制
print(int(11.11))  # 11，float转为int
# print(int(0x11, 16))  # TypeError: int() can't convert non-string with explicit base

# float(x) 将x转换到一个浮点数
print(float(3.14))  # 3.14
print(float(3))  # 3.0
print(float("3.14"))  # 3.14
print(float("3"))  # 3.0
# print(float("0x11"))  # ValueError: could not convert string to float: '0x11'

# complex(real [,imag]) 创建一个复数
print(complex(3.14))   # (3.14+0j)
print(complex(3, 0.14))  # (3+0.14j)

# str(x) 将对象 x 转换为字符串
print(str(3))  # 3
print(str(3.14))  # 3.14
print(str(0x11))  # 17
m = {"a": 1, "b": 0}
sm = str(m)
print(type(m), type(sm))  # <class 'dict'> <class 'str'>

# repr(x) 将对象 x 转换为表达式字符串
sm = repr(m)
print(type(sm))  # <class 'str'>
print(type(repr(1)))  # <class 'str'>

# eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
s = "1+2"
print(eval(s))  # 3

# tuple(s) 将序列 s 转换为一个元组
l = [1, "a", 2, "b"]
t = tuple(l)
print(type(t))  # <class 'tuple'>

# list(s) 将序列 s 转换为一个列表
print(type(list(t)))  # <class 'list'>

# set(s) 转换为集合，元素不重复，可以进行并、交、差、补集
s1 = set("hello")
s2 = set("python")
print(type(s1), type(s2))  # <class 'set'> <class 'set'>
# s1[0] = 'x' # set 不允许修改，TypeError: 'set' object does not support item assignment
print(s1, s2)  # {'l', 'h', 'e', 'o'} {'y', 't', 'o', 'h', 'p', 'n'}
print(s1 & s2)  # 求交集, {'o', 'h'}
print(s1 | s2)  # 求并集, {'l', 'e', 'n', 'o', 'h', 'p', 'y', 't'}
# print(s1 + s2)  # 集合不能相加, TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s1 - s2)  # 求差集, {'l', 'e'}
print(s1 ^ s2)  # 求补集，返回两个集合中都没有的元素，{'p', 'l', 'e', 'y', 'n', 't'}

# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
# 使用关键字参数构建dict
dict1 = dict(x=1, y="a", z=3.14)
print(dict1)  # {'x': 1, 'y': 'a', 'z': 3.14}
# 使用可迭代对象创建dict
dict2 = dict([("a", 1), ("b", "x")])
print(dict2)  # {'a': 1, 'b': 'x'}
# 使用映射创建字典，组合关键字参数
# print(dict({"a": 1, "b":"x"}, ("c", 3.14))) # TypeError: dict expected at most 1 argument, got 2
print(dict({"a": 1, "b": "x"}, c=3.14))  # {'a': 1, 'b': 'x', 'c': 3.14}
# 映射函数方式来构造字典
# {'one': 1, 'two': 2, 'three': 3}
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))

# frozenset(s) 转换为不可变集合，set同样不可变
s1 = frozenset(range(5))
print(s1)  # frozenset({0, 1, 2, 3, 4})
# s1[0] = 100 # TypeError: 'frozenset' object does not support item assignment
# s1 = set(range(5))
# s1[0] = 100 # TypeError: 'set' object does not support item assignment
s1 = list(range(5))
s1[0] = 100
print(s1)  # [100, 1, 2, 3, 4]

# chr(x) 将一个整数转换为一个字符
print(chr(0x30), chr(0x31), chr(0x61))   # 十六进制
# 0 1 a
print(chr(48), chr(49), chr(97))         # 十进制
# 0 1 a
print(",", chr(0), ",")  # , ,
print(chr(255))  # ÿ
print(chr(256))  # Ā
print(chr(257))  # ā

# unichr(x) 将一个整数转换为Unicode字符，python3已经移除，改为chr

# ord(x) 将一个字符转换为它的整数值
print(ord("a"))  # 97
print(ord("z"))  # 122
print(ord("A"))  # 65
print(ord("Z"))  # 90
print(ord("哈"))  # 21704

# hex(x) 将一个整数转换为一个十六进制字符串
print(hex(10))  # 0xa
print(hex(11))  # 0xb
print(hex(12))  # 0xc

# oct(x) 将一个整数转换为一个八进制字符串
print(oct(7))  # 0o7
print(oct(8))  # 0o10
print(oct(9))  # 0o11
