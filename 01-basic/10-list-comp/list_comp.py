# Python教程08：列表推导式入门

# 1. 基本语法
# [表达式 for 变量 in 序列]
squares = [i ** 2 for i in range(1, 11)]
print(f"Squares: {squares}")

# 2. 带条件
# [表达式 for 变量 in 序列 if 条件]
numbers = range(1, 11)
evens = [n for n in numbers if n % 2 == 0]
print(f"Evens: {evens}")

# 过滤并转换
words = ['apple', 'banana', 'cherry', 'date']
long_words = [w.upper() for w in words if len(w) > 5]
print(f"Long words: {long_words}")

# 3. 带if-else
# [表达式1 if 条件 else 表达式2 for 变量 in 序列]
numbers = range(1, 11)
result = [n ** 2 if n % 2 == 1 else n for n in numbers]
print(f"If-else result: {result}")

# 4. 嵌套列表推导式
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# 九九乘法表
table = [f"{i}×{j}={i*j}" for i in range(1, 10) for j in range(1, i+1)]
print("Multiplication table (first 5):", table[:5])

# 5. 字典推导式
squares_dict = {n: n ** 2 for n in range(1, 6)}
print(f"Dict comp: {squares_dict}")

# 6. 集合推导式
unique_squares = {n ** 2 for n in [1, 1, 2, 2, 3, 3]}
print(f"Set comp: {unique_squares}")

# 7. 生成器表达式
squares_gen = (i ** 2 for i in range(10))
print("Generator output:", end=" ")
for sq in squares_gen:
    print(sq, end=" ")
print()
