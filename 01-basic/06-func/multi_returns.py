import math

# 一个函数可以返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # 151.96152422706632 70.0

# 看起来返回了多个值，其实只是一个语法糖，底层返回是元组并给返回的变量依次赋值
r = move(100, 100, 60, math.pi / 6)
print(r)  # (151.96152422706632, 70.0)
