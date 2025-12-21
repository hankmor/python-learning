# Python教程24：内置函数深入

# 1. 类型转换
print("=== 类型转换 ===")
print(int("123"))
print(float("3.14"))
print(bool("False"))
print(list("Python"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
print(dict([('a', 1), ('b', 2)]))

# 2. 数学函数
print("\n=== 数学函数 ===")
print(abs(-10))
print(round(3.14159, 2))
print(pow(2, 3))
print(sum([1, 2, 3]))
print(min(1, 2, 3))
print(max(1, 2, 3))
print(divmod(17, 5))

# 3. 序列操作
print("\n=== 序列操作 ===")
numbers = [1, 2, 3, 0]
print(all(numbers))  # False (0 is False)
print(any(numbers))  # True

words = ["python", "is", "awesome"]
print(sorted(words, key=len))

print(list(reversed(words)))

for i, word in enumerate(words, 1):
    print(f"{i}: {word}")

names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))

# 4. 高阶函数
print("\n=== 高阶函数 ===")
squares = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(squares))

evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(evens))

# 5. 对象属性
print("\n=== 对象属性 ===")
s = "hello"
print(isinstance(s, str))
print(hasattr(s, "upper"))
print(getattr(s, "upper")())
