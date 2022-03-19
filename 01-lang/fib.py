'''
斐波那契数列
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''


# 给定一个数，求它之前的斐波那契数列
def fib(num):
    a, b, result = 0, 1, ''
    while a <= num:
        result += "{0}, ".format(a)
        a, b = b, a + b  # b变为a+b的和，a变为b
    return result


# 求斐波那契数列中第idx索引位置的数字
def fib2(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    else:
        # 递归，前边两个数相加
        return fib2(idx - 2) + fib2(idx - 1)


print(fib(100))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
print('\n')
print(fib2(0))  # 0
print(fib2(1))  # 1
print(fib2(3))  # 2
print(fib2(11))  # 89
