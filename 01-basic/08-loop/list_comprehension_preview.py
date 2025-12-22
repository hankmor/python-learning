# 列表推导式预告

print("--- 传统方法 ---")
# 传统方法：生成1-10的平方
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)

print("\n--- 列表推导式 ---")
# 列表推导式：一行搞定
squares = [i ** 2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, ..., 100]
