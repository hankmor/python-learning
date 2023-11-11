"""
如果list可以通过算法计算出来，而不需要创建完整的list而浪费内存，那么可以通过generator一边计算一边生成
列表生成式与列表生成器：
1、生成式是简化列表的创建，得到的是已经创建了元素的列表
2、生成器不会生成列表元素，而需要循环或者通过next获取元素
"""

# 把一个列表生成式的[]改成()，就创建了一个generator
l = [x * x for x in range(1, 11)]
# 得到的是一个list
print(l)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
g = (x * x for x in range(1, 11))
# 得到一个生成器实例
print(g)  # <generator object <genexpr> at 0x10239d970>

# 可以通过next获取generator生成的下一个的值，如果下一个值无法计算，则或抛出异常
print(next(g))  # 1
print(next(g))  # 4
print()
# 循环获取列表，generator上一个可迭代对象，由于上边next已经获取了两个元素，所以下边的循环将会从元素9开始打印
for v in g:
    print(v)
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

# 如果没有元素了，next将报错：
# next(g) # StopIteration
