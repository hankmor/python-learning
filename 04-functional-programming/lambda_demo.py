"""
Lambda函数与高阶函数示例
对应文章：Python教程18：Lambda函数与高阶函数
"""

# -----------------------------------------------------------------------------
# 1. Lambda基础
# -----------------------------------------------------------------------------

# 普通函数 vs Lambda
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(f"Normal function: {square(5)}")         # 25
print(f"Lambda function: {square_lambda(5)}")  # 25

# 多参数
add = lambda x, y: x + y
print(f"Add: {add(3, 5)}")  # 8

# 无参数
greet = lambda: "Hello!"
print(f"Greet: {greet()}")  # Hello!

# 默认参数
power = lambda x, n=2: x ** n
print(f"Power (default): {power(3)}")     # 9
print(f"Power (custom): {power(3, 3)}")   # 27


# -----------------------------------------------------------------------------
# 2. 实际应用
# -----------------------------------------------------------------------------

# 列表排序
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]
# 按分数降序排列
students.sort(key=lambda x: x[1], reverse=True)
print(f"Sorted students: {students}")
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 字典排序
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted scores: {sorted_scores}")

# 条件判断 (三元表达式)
max_val = lambda a, b: a if a > b else b
print(f"Max(10, 20): {max_val(10, 20)}")  # 20


# -----------------------------------------------------------------------------
# 3. 高阶函数配合 (map, filter)
# -----------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# map: 平方
squares = list(map(lambda x: x**2, numbers))
print(f"Squares (map): {squares}")

# filter: 偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens (filter): {evens}")

# reduce: 累积求和
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(f"Total (reduce): {total}")


# -----------------------------------------------------------------------------
# 4. Lambda vs 列表推导式
# -----------------------------------------------------------------------------

# map vs list comprehension
squares_lc = [x**2 for x in numbers]
print(f"Squares (LC): {squares_lc}")

# filter vs list comprehension
evens_lc = [x for x in numbers if x % 2 == 0]
print(f"Evens (LC): {evens_lc}")
