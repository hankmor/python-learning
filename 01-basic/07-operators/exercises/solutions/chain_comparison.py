#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题02答案：链式比较
"""

# 获取用户输入
number = int(input("请输入一个数字："))

# 方法1：链式比较（Python特有的优雅写法）
if 10 <= number <= 100:
    print(f"{number} 在10到100之间")
else:
    print(f"{number} 不在10到100之间")

# 方法2：传统写法（对比）
if number >= 10 and number <= 100:
    print(f"{number} 在10到100之间（传统写法）")

# 更详细的判断
print("\n详细判断：")
if number < 10:
    print(f"{number} 小于10")
elif 10 <= number <= 100:
    print(f"{number} 在10到100之间（含边界）")
else:
    print(f"{number} 大于100")

# 演示链式比较的强大
age = 25
if 18 <= age < 65:
    print(f"\n年龄{age}在工作年龄段")

# 多重链式比较
x = 5
if 0 < x < 10 < 100:
    print(f"\n链式比较：0 < {x} < 10 < 100 = True")
