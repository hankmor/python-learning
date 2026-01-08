"""
列表进阶与推导式高级
Coverage:
1. 嵌套列表推导式
2. 性能对比
3. 字典和集合推导式
4. 生成器表达式
5. 高级操作 (zip, enumerate)
"""
import time

print("==== 1. 嵌套列表推导式 ====")
# 二维列表展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# 创建3x3矩阵 (推荐方式)
matrix_3x3 = [[0 for _ in range(3)] for _ in range(3)]
print(f"3x3 Matrix: {matrix_3x3}")

# 笛卡尔积
colors = ['Red', 'Blue']
sizes = ['S', 'M']
products = [f"{c}-{s}" for c in colors for s in sizes]
print(f"Products: {products}")


print("\n==== 2. 性能对比 ====")
# 列表推导式 vs 循环
N = 100000
start = time.time()
res_loop = []
for i in range(N):
    res_loop.append(i**2)
time_loop = time.time() - start

start = time.time()
res_comp = [i**2 for i in range(N)]
time_comp = time.time() - start

print(f"Loop time: {time_loop:.4f}s")
print(f"Comp time: {time_comp:.4f}s")
print(f"Faster by: {(time_loop - time_comp) / time_loop * 100:.2f}%")


print("\n==== 3. 字典和集合推导式 ====")
# 字典推导式: 字符统计
text = "hello world"
char_count = {char: text.count(char) for char in set(text) if char != ' '}
print(f"Char count: {char_count}")

# 集合推导式: 绝对值去重
nums = [1, -2, 2, -1, 3]
abs_set = {abs(x) for x in nums}
print(f"Abs unique: {abs_set}")


print("\n==== 4. 生成器表达式 ====")
# 节省内存
gen = (x**2 for x in range(10))
print(f"Generator: {gen}")
print(f"Sum from gen: {sum(gen)}")


print("\n==== 5. 高级操作 ====")
# zip并行遍历
names = ["Alice", "Bob"]
scores = [85, 92]
mapped = {name: score for name, score in zip(names, scores)}
print(f"Zip result: {mapped}")

# 矩阵转置 (实战)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Original: {matrix}")
print(f"Transposed: {transposed}")
