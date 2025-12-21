#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题01答案：除法运算对比
"""

a = 9
b = 2

print("除法运算对比:")
print("="*40)

# 除法 /
result1 = a / b
print(f"{a} / {b} = {result1}")
print(f"类型: {type(result1)}")
print(f"说明: 除法运算，结果是浮点数")

print()

# 整除 //
result2 = a // b
print(f"{a} // {b} = {result2}")
print(f"类型: {type(result2)}")
print(f"说明: 整除运算，结果是整数（向下取整）")

print()

# 取模 %
result3 = a % b
print(f"{a} % {b} = {result3}")
print(f"类型: {type(result3)}")
print(f"说明: 取模运算，结果是余数")

print("="*40)

# 验证关系：a = b * (a // b) + (a % b)
print(f"\n验证: {a} = {b} × {result2} + {result3} = {b * result2 + result3}")
