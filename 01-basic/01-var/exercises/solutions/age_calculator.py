#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题01答案：年龄计算器
"""

# 获取用户输入
name = input("请输入你的姓名：")
birth_year = int(input("请输入你的出生年份："))

# 计算年龄（假设当前年份）
current_year = 2024
age = current_year - birth_year

# 输出结果
print(f"你好，{name}！")
print(f"你今年 {age} 岁")

# 更详细的版本
print("\n" + "="*40)
print(f"姓名：{name}")
print(f"出生年份：{birth_year}")
print(f"当前年份：{current_year}")
print(f"年龄：{age} 岁")
print("="*40)
