#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
运算符示例
演示Python各类运算符的使用
"""

print("="*50)
print("1. 算术运算符")
print("="*50)

a = 10
b = 3

print(f"\n基本运算：")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# 负数取模
print(f"\n负数取模：")
print(f"10 % 3 = {10 % 3}")
print(f"10 % -3 = {10 % -3}")
print(f"-10 % 3 = {-10 % 3}")
print(f"-10 % -3 = {-10 % -3}")

print("\n" + "="*50)
print("2. 比较运算符")
print("="*50)

x = 10
y = 20

print(f"\n{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# 链式比较
age = 25
print(f"\n链式比较：18 <= {age} <= 65: {18 <= age <= 65}")

print("\n" + "="*50)
print("3. 逻辑运算符")
print("="*50)

print(f"\nTrue and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# 短路求值演示
print(f"\n短路求值：")
print(f"False and print('不执行') = ", end="")
result = False and print("不执行")
print(result)

print("\n" + "="*50)
print("4. 位运算符")
print("="*50)

a = 5  # 二进制: 0101
b = 3  # 二进制: 0011

print(f"\na = {a} (二进制: {bin(a)})")
print(f"b = {b} (二进制: {bin(b)})")
print(f"{a} & {b} = {a & b} (二进制: {bin(a & b)})")
print(f"{a} | {b} = {a | b} (二进制: {bin(a | b)})")
print(f"{a} ^ {b} = {a ^ b} (二进制: {bin(a ^ b)})")
print(f"~{a} = {~a}")
print(f"{a} << 1 = {a << 1}")
print(f"{a} >> 1 = {a >> 1}")

print("\n" + "="*50)
print("5. 成员运算符")
print("="*50)

text = "Python"
numbers = [1, 2, 3, 4, 5]

print(f"\n'P' in '{text}': {'P' in text}")
print(f"'J' in '{text}': {'J' in text}")
print(f"3 in {numbers}: {3 in numbers}")
print(f"10 not in {numbers}: {10 not in numbers}")

print("\n" + "="*50)
print("6. 身份运算符")
print("="*50)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\na = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"a == b: {a == b} (值相等)")
print(f"a is b: {a is b} (不是同一对象)")
print(f"a is c: {a is c} (是同一对象)")
print(f"id(a) = {id(a)}, id(b) = {id(b)}, id(c) = {id(c)}")

print("\n" + "="*50)
print("7. 运算符优先级")
print("="*50)

result = 10 + 5 * 2 ** 2 - 8 // 3
print(f"\n10 + 5 * 2 ** 2 - 8 // 3 = {result}")
print("计算顺序：2**2=4, 5*4=20, 8//3=2, 10+20-2=28")

result = (10 + 5) * 2 ** 2 - 8 // 3
print(f"\n(10 + 5) * 2 ** 2 - 8 // 3 = {result}")
print("使用括号改变优先级")
