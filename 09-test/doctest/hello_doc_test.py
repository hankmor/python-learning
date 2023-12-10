"""
文档测试: 编写在文档注释中的代码，python 可以通过 doctest 直接提取并测试。
doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
"""
import doctest


def abs(n):
    """
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n >= 0 else (-n)


# 上述 abs 方法文档中存在交互式命令行代码，doctest 可以直接提取并严格验证他们的结果

if __name__ == '__main__':
    # 倒入文档测试包
    import doctest

    # 开启文档测试
    doctest.testmod()

# 命令行执行 python3 hello_doc_test.py，没有任何输出说明文档测试通过
# 如果将 abs(0) 改为 abs(1) 则会输出异常, 告诉我们哪儿未测试通过，期望值和得到的值都是什么，异常如下：
# **********************************************************************
# File "/Users/hank/workspace/mine/python-projects/python-learning/09-test/doctest/hello_doc_test.py", line 18, in __main__.abs
# Failed example:
#     abs(1)
# Expected:
#     0
# Got:
#     1
# **********************************************************************
# 1 items had failures:
#    1 of   3 in __main__.abs
# ***Test Failed*** 1 failures.
