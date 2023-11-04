# 通过isinstance判断是否是类型的实例
def my_abs(x):
    if not isinstance(x, (int, float)):  # 判断x是否是int或float的实例
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs('a') # TypeError: bad operand type
print(my_abs(-10))  # 10
