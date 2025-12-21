#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题01答案：个性化问候程序
"""

# 打印姓名和喜欢的诗词
print("我叫张三")
print("海内存知己，天涯若比邻。")

# 或者使用变量
name = "李四"
poem = "长风破浪会有时，直挂云帆济沧海。"
print(f"我叫{name}")
print(poem)

# 更复杂的版本
print("\n" + "="*40)
print("个人信息")
print("="*40)
print(f"姓名：{name}")
print(f"座右铭：{poem}")
print("="*40)
