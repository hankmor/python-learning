# 嵌套列表推导式 (Nested List Comprehension)

# 1. 二维列表展平
print("--- 二维列表展平 ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 方法1：列表推导式（先外层后内层）
flat = [num for row in matrix for num in row]
print(f"Flattened with list comp: {flat}")

# 方法2：等价的传统写法
flat_traditional = []
for row in matrix:
    for num in row:
        flat_traditional.append(num)
print(f"Flattened traditional:    {flat_traditional}")

# 2. 生成九九乘法表
print("\n--- 九九乘法表 ---")
# 列表推导式生成
table = [f"{i}×{j}={i*j}" for i in range(1, 10) for j in range(1, i+1)]

# 打印前5个看看
print(f"First 5 items: {table[:5]}")

# 格式化打印
print("Printing table:")
row_idx = 1
for item in table:
    print(item, end="\t")
    if item.startswith(f"{row_idx}×{row_idx}"):
        print()
        row_idx += 1
