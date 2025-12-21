# Python教程09：Python编码规范(PEP 8)
# 这个文件演示了一些PEP 8的规范

import os
import sys

# 常量命名：全大写
MAX_SIZE = 100

# 类名：PascalCase
class UserManager:
    def __init__(self, name):
        # 变量名：snake_case
        self.user_name = name
        # 私有变量
        self._internal_id = 123
    
    def get_name(self):
        # 4个空格缩进
        return self.user_name

# 函数名：snake_case
def calculate_area(radius):
    """
    文档字符串演示
    计算圆的面积
    """
    return 3.14159 * radius ** 2

# 顶层函数间空2行
def main():
    user = UserManager("Alice")
    print(f"User: {user.get_name()}")
    
    # 操作符周围加空格
    x = 10 + 20
    
    # 列表定义
    items = [
        1, 2, 3,
        4, 5, 6,
    ]
    
    # 比较
    if x is not None:
        print("x is not None")

if __name__ == "__main__":
    main()
