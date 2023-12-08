"""
python 的异常机制与 java 类似，也定义了 try except finally 语句来捕获异常
except 语句块捕获到对应的异常会执行，而且跟异常继承体系有关，多个 except 语句块时越低级的异常要写在最前边，否则会被上级异常捕获
finally 语句块无论是否捕获异常都会执行

python的异常机制体系如下: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
可以看到所有的异常都继承自 BaseException
"""

try:
    x = 10 / 0
    print("result: ", x)
except ArithmeticError as e:  # 由于 ZeroDivisionError 继承自 ArithmeticError，所以前边的 ArithmeticError 会被执行
    print("arith exception: ", e)
except ZeroDivisionError as e:  # 这里不会被执行
    print("zero division exception: ", e)
finally:
    print("finally")

# arith exception:  division by zero
# finally
