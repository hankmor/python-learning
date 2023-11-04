"""
可变参数
python的可变参数定义格式为 [*param_name], java 和 go 都用 [...] 表示可变参数
"""


# 参数 *nums表示可以传递多个值
def add(*nums):
    r = 0
    for x in nums:
        r = r + x
    return r


print(add())  # 0
print(add(1))  # 1
print(add(1, 2))  # 3
print(add(1, 2, 3))  # 6


# 如果传递一个list、tuple会怎样，直接传递是不行的，会抛出异常
# print(add((1,2,3))) # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
# print(add([1,2,3])) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
# 此时需要使用 * 号告诉解释器将tuple和list中的元素作为可变参数传入函数中
print(add(*(1, 2, 3)))  # 6
print(add(*[1, 2, 3]))  # 6


def add(*nums):
    print(type(nums))


print(add(1, 2, 3))  # <class 'tuple'>, 可见，可变参数其实是对 tuple 的一种封装
