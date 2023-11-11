# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象

from typing import Iterable, Iterator

# list
print(isinstance([1, 2], Iterable))  # True
# dict
print(isinstance({"a": 1}, Iterable))  # True
# string
print(isinstance("abc", Iterable))  # True
# tuple
print(isinstance((1, 2), Iterable))  # True
# set
print(isinstance({1, 2}, Iterable))  # True


# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# list
print(isinstance([1, 2], Iterator))  # False
# dict
print(isinstance({"a": 1}, Iterator))  # False
# string
print(isinstance("abc", Iterator))  # False
# tuple
print(isinstance((1, 2), Iterator))  # False
# set
print(isinstance({1, 2}, Iterator))  # False
# 列表生成式
print(isinstance([x for x in range(1, 10)], Iterator))  # False
# list generator
print(isinstance((x for x in range(1, 10)), Iterator))  # True
