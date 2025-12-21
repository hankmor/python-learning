#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
缩进示例
演示Python缩进的重要性
"""

# 正确的缩进
print("=== 正确的缩进示例 ===")
if True:
    print("这行有缩进")
    print("这行也有缩进")
print("这行没有缩进，不属于if块")

# 嵌套缩进
print("\n=== 嵌套缩进示例 ===")
if True:
    print("第一层缩进")
    if True:
        print("第二层缩进（嵌套）")
        print("仍然是第二层")
    print("回到第一层")
print("没有缩进")

# 循环中的缩进
print("\n=== 循环中的缩进 ===")
for i in range(3):
    print(f"外层循环: {i}")
    for j in range(2):
        print(f"  内层循环: {j}")

# 函数中的缩进
print("\n=== 函数中的缩进 ===")
def greet(name):
    """问候函数"""
    if name:
        message = f"你好，{name}!"
        print(message)
    else:
        print("你好，陌生人!")

greet("张三")
greet("")
