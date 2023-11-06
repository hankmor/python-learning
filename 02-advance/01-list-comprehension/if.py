"""
列表生成式中if...else的用法
"""

# 筛选偶数
l = [x for x in range(1, 11) if x % 2 == 0]
print(l)  # [2, 4, 6, 8, 10]

# 注意上边的筛选不能使用else，否则无法筛选并抛出异常
# l = [x for x in range(1, 11) if x % 2 == 0 else 0]
# print(l) # SyntaxError: invalid syntax

# 将筛选条件放在前边时，必须加上else
# l = [x if x % 2 == 0 for x in range(1, 11)] # SyntaxError: expected 'else' after 'if' expression
l = [x if x % 2 == 0 else 0 for x in range(1, 11)]
print(l)  # [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]

# 注意两者的区别：
# 1、在循环之后添加 if 时增加了筛选条件，不能加else，否则不知道如何筛选
# 2、在前边加上if是在循环得到元素x后再作处理，此时必须加上else，否则必匹配if后无法成功得到一个元素
