"""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""
import itertools

# 创建一个自然序列的无限迭代器
natuals = itertools.count(1)
for n in natuals:
    if n < 10:
        print(n)
    else:
        break

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
print(next(cs))
print(next(cs))
print(next(cs))
print(next(cs))

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 3)
for x in ns:
    print(x)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
c = itertools.chain('abc', '123')
for x in c:
    print(x)  # 依次打印 a b c 1 2 3

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']

# 指定第二个参数，定义认定重复的key，这里忽略大小写
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']

# 计算圆周率可以根据公式：
# π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和
def pi(N):
    """ 计算pi的值 """
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.count(1, 2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    selodds = itertools.takewhile(lambda x: x <= 2 * N - 1, odds)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和
    # 求和用 sum 函数，后边的列表中，x 为 1,3,5...,用 //2 整除2后，得到 0，1，2...,在 (-1) ** (x//2) 就可以加上负号了
    return sum(4 / x * ((-1) ** (x // 2)) for x in selodds)


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
