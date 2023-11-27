#!/usr/bin/env python3

"""
用于测试 python 模块
"""

import sys


# 定义 __author__ 变量指定作者
__author__ = "hank"


def test():
    args = sys.argv  # 获取命令行传入的参数，第一个参数始终是当前 python 脚本文件名称
    if len(args) == 1:
        print("hello, python!")
    elif len(args) == 2:
        print("hello, %s" % args[1])
    else:
        print("too many arguments")


# 命令行执行脚本时，自动将变量 __name__ 设置为 __main__，通过这里开始执行
if __name__ == '__main__':
    test()


# 执行脚本：
# 1、在控制台授权: chmod +x hello.py
# 2、执行: ./hello.py
# 3、传递参数： ./hello.py hank
# ➜  python-learning git:(main) ✗ cd 04-module
# 示例如下：
# ➜  04-module git:(main) ✗ chmod +x hello.py
# ➜  04-module git:(main) ✗ ./hello.py
# hello, python!
# ➜  04-module git:(main) ✗ ./hello.py hank
# hello, hank
# ➜  04-module git:(main) ✗ ./hello.py hank other
# too many arguments
#
