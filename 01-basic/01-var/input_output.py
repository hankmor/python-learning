#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
输入输出示例
演示print()和input()的使用
"""

# ==========
# print() 基本用法
# ==========

print("=== print()基本用法 ===")
print("Hello, World!")

# 打印多个值
print("姓名:", "张三", "年龄:", 25)

# 指定分隔符
print("A", "B", "C", sep="-")  # 输出: A-B-C
print("A", "B", "C", sep="")   # 输出: ABC

# 指定结束符（不换行）
print("不换行", end=" ")
print("继续")

# 打印变量
name = "李四"
age = 30
print("姓名:", name, "年龄:", age)

# 格式化输出（f-string，Python 3.6+）
print(f"姓名: {name}, 年龄: {age}")

# ==========
# input() 基本用法
# ==========

print("\n=== input()基本用法 ===")

# 注意：input()返回的是字符串
user_input = input("请输入你的名字：")
print(f"你好，{user_input}!")
print(f"类型: {type(user_input)}")

# 转换类型
# age = int(input("请输入你的年龄："))
# print(f"十年后你 {age + 10} 岁")
# print(f"类型: {type(age)}")

# ==========
# 综合示例
# ==========

print("\n=== 综合示例（已注释，需要交互） ===")
# 下面的代码需要用户输入，取消注释即可运行

# name = input("请输入你的名字：")
# birth_year = int(input("请输入你的出生年份："))
# current_year = 2024
# age = current_year - birth_year
# print(f"你好，{name}！")
# print(f"你今年 {age} 岁")

# 如果需要运行交互式代码，请取消注释并执行
