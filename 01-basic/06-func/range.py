# range函数生成一个数字序列，一个参数时从0开始，步长为1
r = range(3)
print(r, type(r))  # range(0, 3) <class 'range'>

# 可以不从0开始生成序列
r = range(5, 9)
print(list(r))  # 用range生成的序列创建list，方便查看：[5, 6, 7, 8]

# 可以为range指定步长
r = range(10, 20, 2)
print(list(r))  # [10, 12, 14, 16, 18]

# 循环
for i in range(10):
    print(i, end=" ")

print()
# range返回的是一个可迭代的对象：iterable，比如list、string、dict、tuple都是可迭代对象
# 通过直接传递可迭代对象，可以创建list、set等对象
print(set(range(10)))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(tuple(range(10)))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum(range(10)))  # 45，使用sum行数将可迭代的range对象累加
