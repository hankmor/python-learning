"""
递归函数
"""


# 基本的递归写法，不断调用函数会导致栈溢出
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
print(fact(5))  # 120


"""
优化递归造成的栈溢出问题：使用尾递归，基本思想就是使用循环代替递归
"""


def fact_1(n):
    return fact_item(n, 1)


# n为基数，r为计算的结果
def fact_item(n, r):
    if n == 1:
        return r
    return fact_item(n - 1, n * r)  # 相当于循环调用


# fact_1(5)
# fact_item(5, 1)
# fact_item(4, 5)
# fact_item(3, 20)
# fact_item(2, 60)
# fact_item(1, 120)
# 120
print(fact_1(5))  # 120
