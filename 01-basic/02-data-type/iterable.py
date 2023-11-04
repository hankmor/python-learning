"""
可迭代对象
"""

from collections.abc import Iterable

# 判断是否可以迭代，需要引入 collections.abc 中的 Iterable
print(isinstance([1, 2], Iterable))  # True
print(isinstance((1, 2), Iterable))  # True
print(isinstance({"a": 1}, Iterable))  # True
print(isinstance({"a", "b"}, Iterable))  # True
print(isinstance(123, Iterable))  # False
print(isinstance("123", Iterable))  # True
