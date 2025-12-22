# 注释与文档 (Comments and Docstrings)

# 1. 行注释
# 注释应该完整的句子，首字母大写
x = 5  # 这是一个解释性注释

# 2. 文档字符串 (Docstrings)
def calculate_area(radius):
    """
    计算圆的面积。

    Args:
        radius (float): 圆的半径

    Returns:
        float: 圆的面积

    Examples:
        >>> calculate_area(5)
        78.53975
    """
    return 3.14159 * radius ** 2


class Calculator:
    """
    简单的计算器类。

    提供基本的数学运算功能。
    """

    def add(self, a, b):
        """返回两数之和。"""
        return a + b
