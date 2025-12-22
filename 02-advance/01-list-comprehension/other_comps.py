# 其他推导式 (Other Comprehensions)

print("--- 字典推导式 (Dictionary Comprehension) ---")
# 创建字典
numbers = range(1, 6)
squares_dict = {n: n ** 2 for n in numbers}
print(f"Squares dict: {squares_dict}")

# 交换字典键值
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped:  {swapped}")

# 筛选字典
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
passed = {name: score for name, score in scores.items() if score >= 80}
print(f"Passed:   {passed}")


print("\n--- 集合推导式 (Set Comprehension) ---")
# 去重并转换
numbers = [1, 1, 2, 2, 3, 3]
unique_squares = {n ** 2 for n in numbers}
print(f"Unique squares: {unique_squares}")

# 提取首字母
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
first_letters = {w[0] for w in words}
print(f"First letters:  {first_letters}")


print("\n--- 生成器表达式 (Generator Expression) ---")
# 列表推导式：立即生成所有元素
squares_list = [i ** 2 for i in range(5)]
print(f"List type: {type(squares_list)}")
print(f"List data: {squares_list}")

# 生成器表达式：惰性计算（使用圆括号）
squares_gen = (i ** 2 for i in range(5))
print(f"Gen type:  {type(squares_gen)}")
print("Iterating gen:", end=" ")
for sq in squares_gen:
    print(sq, end=" ")
print()
