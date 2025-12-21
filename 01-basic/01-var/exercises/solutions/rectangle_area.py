#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题03答案：长方形面积计算
"""

# 获取用户输入
length = float(input("请输入长方形的长："))
width = float(input("请输入长方形的宽："))

# 计算面积
area = length * width

# 输出结果
print(f"长方形的面积是：{area}")

# 更详细的版本
print("\n" + "="*40)
print("长方形面积计算")
print("="*40)
print(f"长：{length}")
print(f"宽：{width}")
print(f"面积：{area}")
print("="*40)

# 扩展：计算周长
perimeter = 2 * (length + width)
print(f"周长：{perimeter}")
