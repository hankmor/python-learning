"""
高阶函数
"""


# 函数与变量
print(abs)  # abs是一个函数，<built-in function abs>
print(abs(-10))  # 调用abs函数获得绝对值，10
f = abs(-10)
print(f)  # f是abs执行的结果, 10
f = abs
print(f)  # f 是 abs 函数的别名, <built-in function abs>
print(f(-10))  # 执行函数 f 的结果， 10

# abs = 10 # 变量 abs 替换了内建函数 abs
# abs(-10) # 无法执行 abs，被替换了


# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)


def square(x):
    return x**2


r = add(-10, -2, abs)
print(r)  # 12
r = add(2, 3, square)
print(r)  # 13
