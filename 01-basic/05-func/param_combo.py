"""
参数组合使用
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)  # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, 3)  # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'ext': 'none'}
f1(1, 2, 3, 'a', 'b', ext='none')

f2(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 可以通过tuple、dict传入参数，会依次匹配参数列表
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
