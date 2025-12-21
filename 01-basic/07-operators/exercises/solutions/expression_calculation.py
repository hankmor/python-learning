#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题01答案：表达式计算
"""

print("表达式：10 + 5 * 2 ** 2 - 8 // 3")
print("="*50)

# 计算过程
step1 = 2 ** 2
print(f"步骤1：2 ** 2 = {step1}")

step2 = 5 * step1
print(f"步骤2：5 * {step1} = {step2}")

step3 = 8 // 3
print(f"步骤3：8 // 3 = {step3}")

step4 = 10 + step2
print(f"步骤4：10 + {step2} = {step4}")

result = step4 - step3
print(f"步骤5：{step4} - {step3} = {result}")

print(f"\n最终结果：{result}")

# 验证
actual_result = 10 + 5 * 2 ** 2 - 8 // 3
print(f"直接计算：{actual_result}")

print("\n运算符优先级（从高到低）：")
print("1. ** (乘方)")
print("2. *, /, //, % (乘、除、整除、取模)")
print("3. +, - (加、减)")
