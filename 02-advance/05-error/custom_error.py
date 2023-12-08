"""
自定义异常类
"""


# err_raise.py
class FooError(ValueError):
    """ 自定义一个异常类，继承自 ValueError，内部其实什么事都没干 """
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
