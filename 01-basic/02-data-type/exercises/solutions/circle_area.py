#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题03答案：圆的面积计算
"""

# 获取用户输入
radius = float(input("请输入圆的半径："))

# 定义π（简化值）
PI = 3.14

# 计算面积
area = PI * radius ** 2

# 输出结果
print(f"半径为 {radius} 的圆的面积是：{area}")

# 更详细的版本
print("\n" + "="*40)
print("圆的面积计算")
print("="*40)
print(f"半径 r = {radius}")
print(f"π = {PI}")
print(f"面积 = π × r² = {PI} × {radius}² = {area}")
print("="*40)

# 扩展：计算周长
circumference = 2 * PI * radius
print(f"周长 = 2πr = {circumference}")

# 使用更精确的π值
import math
area_precise = math.pi * radius ** 2
print(f"\n使用math.pi计算的面积：{area_precise}")
