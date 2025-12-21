#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
练习题03答案：==和is的区别
"""

print("== vs is 的区别")
print("="*50)

# 案例1：列表
print("\n【案例1：列表】")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"\na == b: {a == b} <-- 值相等")
print(f"a is b: {a is b} <-- 不是同一个对象")
print(f"a is c: {a is c} <-- 是同一个对象")
print(f"\n内存地址：")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")

# 案例2：小整数缓存
print("\n【案例2：小整数缓存】")
x = 256
y = 256
print(f"x = 256, y = 256")
print(f"x == y: {x == y}")
print(f"x is y: {x is y} <-- Python缓存了-5到256的整数")

z = 257
w = 257
print(f"\nz = 257, w = 257")
print(f"z == w: {z == w}")
print(f"z is w: {z is w} <-- 超出缓存范围")

# 案例3：None的比较
print("\n【案例3：None的比较】")
value = None
print(f"value = None")
print(f"value == None: {value == None} <-- 可以，但不推荐")
print(f"value is None: {value is None} <-- 推荐写法")

# 总结
print("\n【总结】")
print("1. == 比较值是否相等")
print("2. is 比较是否是同一个对象（内存地址相同）")
print("3. 比较None时应该用 is None")
print("4. 一般情况下用 ==")
print("5. 需要判断对象身份时用 is")
