"""
装饰器
"""


import functools
import time


def fn():
    return "haha"


# 函数也是一个对象，可以赋值给变量
f = fn
print(fn())  # haha
print(f())  # haha
print(fn.__name__)  # 打印函数的名称，输出：fn
print(f.__name__)  # fn
print()


"""
装饰器是一种模式，可以动态增强函数的功能
"""


# 定义打印日志的函数，它接收和返回一个函数
def log(func):
    def wrapper(*args, **kw):  # 定义了可变参数，关键字参数，这样就可以接受任意参数
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 形式类似java的注解
# 把@log放到now()函数的定义处，执行函数就相当于执行了语句：fn = log(fn)
@log
def fn(name):
    return "hello, %s!" % name


print(fn("hank"))
print(log(fn)("hank"))
# output:
# call fn():
# hello, hank!
# 上边的代码，相当于执行了 log(fn)("hank"), 但是函数名称却不一样：
print(log(fn)("hank"))
# call wrapper()
# call fn()
# hello, hank!
# 打印函数的名称，返回的是wrapper
print(fn.__name__)  # wrapper

print()


def fn1(name):
    return "hello, %s!" % name


# 函数名称的变化
# 由于log返回的是wrapper函数，所以f的名称变成了wrapper
f = log(fn1)
print(f.__name__)  # wrapper


# 如果需要f名称仍然不变，则可以使用functools包
def log(func):
    @functools.wraps(func)  # 使用functools包，使得func被包装后返回的wrapper函数名称为func
    def wrapper(*args, **kw):
        print("call %s") % func.__name__
        return func(*args, **kw)
    return wrapper


f = log(fn1)
print(fn1.__name__)  # 未被@log标记名称仍然未 fn1
print(f.__name__)  # fn1


print()


# 带参数的decorator
# 要定义参数的装饰器，则需要再加一个装饰函数，对wrapper再次包装
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def fn2():
    return "fn2"


f = fn2
print(fn2.__name__)  # fn2
print(f.__name__)  # fn2


# 编写一个装饰器，打印函数的执行时间
def exec_time(fn):
    start = time.time()

    def wrapper(*args, **kw):
        ret = fn(*args, **kw)
        end = time.time()
        print("execute %s spend %s ms" % (fn.__name__, (end - start) * 1000))
        return ret
    return wrapper


@exec_time
def fn3(a, b):
    return a + b


@exec_time
def fn4(s1, s2):
    time.sleep(2)
    return s1 + s2, len(s1+s2)


print(fn3(1, 2))
# execute fn3 spend 0.0019073486328125 ms
# 3
print(fn4("hello", "hank"))
# execute fn4 spend 2001.924753189087 ms
# ('hellohank', 9)
