# 不规范代码示例 (Bad Style Examples)
# 仅供参考，请勿模仿

# 1. 错误的缩进
def wrong_indent():
  print("Bad indent") # 2个空格

# 2. 错误的空格使用
x=10 # 缺少空格
y =20 # 空格不对称
def func( a,b ): # 多余的空格
    pass

# 3. 错误比较单例
if x == None: # 应该用 is None
    pass
if x == True: # 应该直接用 if x:
    pass

# 4. 导入不规范
import os, sys # 应该分行导入
from math import * # 避免通配符导入

# 5. 命名不规范
a = 10 # 名字无意义
def MyFunction(): # 函数名应该是snake_case
    pass
