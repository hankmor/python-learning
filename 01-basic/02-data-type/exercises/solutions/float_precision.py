#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题02答案：浮点数精度问题
"""

print("浮点数精度问题演示:")
print("="*40)

# 问题演示
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"是否等于0.3? {result == 0.3}")

print()

# 解决方案1：使用round()函数
rounded = round(result, 1)
print(f"使用round()函数: {rounded}")
print(f"现在等于0.3? {rounded == 0.3}")

print()

# 解决方案2：使用decimal模块（精确计算）
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
result_decimal = a + b
print(f"使用Decimal: {result_decimal}")
print(f"等于0.3? {result_decimal == Decimal('0.3')}")

print("="*40)

# 为什么会出现精度问题？
print("\n原因:")
print("计算机用二进制存储数字")
print("某些十进制小数无法用二进制精确表示")
print("就像1/3无法用十进制精确表示（0.333...）")
