#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
注释示例
演示单行注释和多行注释的使用
"""

# ==========
# 单行注释
# ==========

# 这是一个单行注释
print("Hello")  # 这也是注释，可以放在代码后面

# 计算圆的面积
# 使用简化的π值，精确度够用且计算更快
radius = 5
area = 3.14 * radius ** 2
print("圆的面积:", area)

# ==========
# 多行注释
# ==========

"""
这是一个多行注释
可以写很多行
通常用于写文档字符串（docstring）
"""

'''
单引号也可以
但更推荐用双引号
'''

def calculate_area(radius):
    """
    计算圆的面积
    
    参数:
        radius: 圆的半径
    
    返回:
        圆的面积
    """
    return 3.14 * radius ** 2

# 调用函数
result = calculate_area(10)
print("半径为10的圆的面积:", result)
