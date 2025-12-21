#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题04答案：短路求值应用
"""

def safe_divide(a, b):
    """
    安全的除法函数，利用短路求值避免除零错误
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        除法结果，如果除数为0则返回None
    """
    # 利用and的短路特性：
    # 如果b != 0为False，不会执行后面的除法
    if b != 0 and a / b > 0:
        return a / b
    elif b != 0:
        return a / b
    else:
        return None

# 测试
print("安全除法函数测试")
print("="*50)

print(f"\nsafe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
print(f"safe_divide(-10, 2) = {safe_divide(-10, 2)}")

# 另一种写法
def safe_divide_v2(a, b):
    """使用or的短路特性"""
    return b != 0 and a / b or "除数不能为0"

print(f"\nsafe_divide_v2(10, 2) = {safe_divide_v2(10, 2)}")
print(f"safe_divide_v2(10, 0) = {safe_divide_v2(10, 0)}")

# 演示短路求值的威力
print("\n【短路求值演示】")
print("如果不使用短路，会发生什么？")

# 错误示例（不要运行）
# result = (10 / 0) or print("除零错误")  # 会抛出异常

# 正确示例
denominator = 0
result = denominator != 0 and 10 / denominator or "除数为0"
print(f"结果：{result}")

# 更多短路应用
print("\n【实用应用】")

# 应用1：安全访问列表元素
my_list = [1, 2, 3]
index = 5
value = len(my_list) > index and my_list[index] or "索引越界"
print(f"安全访问列表[{index}]：{value}")

# 应用2：设置默认值
user_input = ""  # 假设用户没有输入
name = user_input or "匿名用户"
print(f"用户名：{name}")
