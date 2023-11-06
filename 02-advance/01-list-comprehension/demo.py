"""
列表生成式
python提供了强大的生成列表的方法
"""

# 使用range生成list
l = list(range(1, 11))  # 1 - 10的列表
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？可以使用循环
l1 = []
for v in l:
    l1.append(v * v)
print(l1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 不使用循环，而改为列表生成式, 一行代码就可以生成列表
l2 = [x*x for x in range(1, 11)]
print(l2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 还可以使用if语句为生成的每一个元素添加筛选条件
# 筛选出偶数
l3 = [x*x for x in range(1, 11) if x % 2 == 0]
print(l3)  # [4, 16, 36, 64, 100]

# 使用两层循环生成所有的排列
l4 = [a + b for a in 'abc' for b in 'def']
print(l4)  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# 拼接字符串
d = {'x': 'A', 'y': 'B', 'z': 'C'}
l5 = [k + '=' + v for k, v in d.items()]
print(l5)  # ['x=A', 'y=B', 'z=C']

# 调用函数
L = ['Hello', 'World', 'IBM', 'Apple']
l6 = [s.lower() for s in L]
print(l6)  # ['hello', 'world', 'ibm', 'apple']
