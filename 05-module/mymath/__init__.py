# mymath/__init__.py
"""
mymath包：提供数学运算功能
"""

VERSION = "1.0.0"

from .basic import add, subtract
from .advanced import power, sqrt

__all__ = ['add', 'subtract', 'power', 'sqrt', 'VERSION']

print(f"mymath包已加载，版本：{VERSION}")
