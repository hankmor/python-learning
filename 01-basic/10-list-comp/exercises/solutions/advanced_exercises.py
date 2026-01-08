"""
列表进阶练习题答案
"""

import math

print("==== 练习1：两位数质数 ====")


# 用列表推导式生成所有两位数的质数
# 质数：只能被1和自身整除
def is_prime(n):
    if n < 2:
        return False
    # 判断是否能被 2 到 sqrt(n) 之间的数整除
    # all中的所有远都是True才会返回True，否则False
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


primes = [x for x in range(10, 100) if is_prime(x)]
print(primes)

# 纯推导式版本 (不推荐，可读性差，但作为练习)
# primes = [x for x in range(10, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]


print("\n==== 练习2：单位矩阵 ====")
# 创建一个5x5的单位矩阵
size = 5
identity_matrix = [[1 if r == c else 0 for c in range(size)] for r in range(size)]

for row in identity_matrix:
    print(row)


print("\n==== 练习3：99乘法表 ====")
# 使用嵌套列表推导式生成99乘法表
table = [[f"{j}x{i}={i * j}" for j in range(1, i + 1)] for i in range(1, 10)]

for row in table:
    print(f" ".join(row))
