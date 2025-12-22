# 遍历字符串
print("--- 遍历字符串 ---")
for char in "Python":
    print(char)

# range()函数示例
print("\n--- range()函数示例 ---")

# range(stop)
print("range(5):")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop)
print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# range(start, stop, step)
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# 倒序
print("range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 ... 1
print()
