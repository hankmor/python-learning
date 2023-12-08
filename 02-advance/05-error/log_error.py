"""
通过日志记录错误信息
"""
import logging


def div(s):
    return 10 / int(s)


def power(s):
    return div(s) ** 2


def main():
    s = "0"
    try:
        power(s)
    except ZeroDivisionError as e:
        # 后边不加异常，则直接将当前异常向上抛出
        raise
        # 当前可以将其他异常转换为特定异常
        # raise ValueError("error value: %s" % s)


def main_logged():
    try:
        power("0")
    except ZeroDivisionError as e:
        # 使用 logging 包记录错误信息
        # exception 会打印堆栈信息
        # logging.exception(e)
        # 只打印错误信息, ERROR
        logging.error(e)
        # 打印警告信息，WARNING
        # logging.warning(e)


# main()
# 未捕获异常，程序终止，不会执行这里
# print("end")

main_logged()
# 使用 logging 记录了错误信息，程序不会有其他异常，可以执行到这里
print("end")
# ERROR:root:division by zero
# end
