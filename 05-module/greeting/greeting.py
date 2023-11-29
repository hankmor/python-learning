
__author__ = 'hank'


import sys


def _sayHello(name):
    print("hello, %s" % name)


def _introduce(name):
    print("my name is %s, nice to meet you, %s" % ('hank', name))


def greeting(name):
    _sayHello(name)
    _introduce(name)


# 测试模块
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        greeting("zhangsan")
    elif len(args) == 2:
        greeting(args[1])
    else:
        print("too many arguments")
