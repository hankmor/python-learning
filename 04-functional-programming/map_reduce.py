"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""


from functools import reduce


def f(x):
    return x*x


r = map(f, [1, 2, 3, 4])  # 列表中的每个元素都作为f的参数执行，结果返回一个Iterator
print(type(r))  # <class 'map'>
print(list(r))  # list函数把整个序列计算出来并返回list，结果为：[1, 4, 9, 16]


# 将列表中的元素都转为str，并打印
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""


# 定义一个两个数求和运算的func
def add(x, y):
    return x + y


# 使用reduce函数依次累加list中的元素
print(reduce(add, [1, 2, 3, 4]))  # 10
# 效果同sum函数
print(sum([1, 2, 3, 4]))  # 10


# 将list中的整数连接起来，元素必须小于10
def concat(x, y):
    return x*10 + y


print(reduce(concat, [1, 2, 3, 4]))  # 1234


# 字符串转为整数的map reduce写法
def char_to_num(c):
    ds = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return ds[c]


print(reduce(concat, map(char_to_num, '123456')))  # 123456
