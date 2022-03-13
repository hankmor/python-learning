# ==========
# 列表，也就是动态数组，支持动态添加、修改、删除元素，支持切片操作
#
# 特点：
# 1、元素存储按照顺序存放
# 2、每一个索引对应一个数据
# 3、数据可以重复
# 4、可以混合存储任何数据类型
# ==========

print("====创建列表====")
lst1 = []
lst2 = list()
print(lst2 == lst1)  # True

print("====获取元素====")
lst = [1, 2, 3, 4, 4, 5, 5, 6, 6]
print(lst)
print(lst[0])  # 按照下标获取元素
print(len(lst))  # 元素个数
print(lst[-1], lst[-2])  # 负数从最后的位置开始获取元素：6 6
# 如果指定的索引位置元素不存在，抛出IndexError
# print(lst[100]  # IndexError: list index out of range

print("====索引操作====")
# 用index函数获取指定元素才list中的索引
# 1、如果存在多个相同元素，只返回第一元素的索引
# 2、如果元素不存在，则抛出ValueError
# 3、可以指定start、stop查找范围内的元素
print("4 index: ", lst.index(4))
print("5 index: ", lst.index(5))
# print(lst.index(7))  # ValueError: 7 is not in list
print(lst.index(5, 4, 6))  # 查找元素5，范围从下标4到6内找，找到第一个5: 5
print(lst.index(5, 6, 8))  # 查找元素5，范围从下标6到8内找，找到第二个5: 6

# 可以混合存储多个数据类型
lst = ["a", 1, 1.0, [1, "a"]]
print(lst)
print(len(lst))
for item in lst:
    print(item, type(item))

# 列表的切片
print("====切片操作====")
lst = [0, 1, 2, 3, 4, 5, 6, 7]
print(lst, id(lst))  # 内存地址
lst2 = lst[2:4]  # 从第2到第4个（不包括）下标位置开始切片，创建新的列表，原列表不变
print(lst2, id(lst2))
print(lst)
# 切片可以设定步长，表示每多少个元素切一次，默认为1
print(lst[::2])  # 省略start，默认为0，省略stop默认为列表长度: 0,2,4,6
print(lst[:6:2])  # 省略start，默认为0，切片到第5个下标: 0,2,4
print("切片步长为负数")
'''
如果切片步长为负数，则从后往前切片
'''
print(lst[::-2])  # 从最后的一个元素往前没2个元素切一次片: 7 5 3 1
print(lst[-1:-5:-2])  # 从最后一个元素到倒数第4个元素切片，每2个元素切一次: [7 5]
print(lst[::-1])  # 效果即使列表反序: [7, 6, 5, 4, 3, 2, 1, 0]
print(lst[7::-1])  # 同样是反序
print(lst[7:3:-1])  # [7, 6, 5, 4]

'''
判断元素是否存在
'''
print("判断列表元素是否存在")
# in 可以判断字符串
print("p" in "python")  # True
print("p" not in "python")  # False
# 同样可以判断集合
lst = [10, 20, 30]
print(10 in lst)  # True
print(40 in lst)  # False

'''
列表的遍历
'''
# 使用 for in语句可以遍历列表中的元素
for item in lst:
    print(item)

'''
列表的元素添加、修改、删除，包括 append、extend、insert、remove、clear、pop、切片、del等方法
'''
print("添加元素")
lst = [1, 2, 3]
print("原列表：", lst, id(lst))
# 通过append向列表添加元素，不会创建新的列表
lst.append(4)
print("新列表: ", lst, id(lst))

lst2 = [5, 6]
lst.append(lst2)
print(lst)  # [1, 2, 3, 4, [5, 6]] 可以看到在列表加了一个元素，该元素是一个列表

# 通过extend可以将元素添加到列表，而不是列表本身
lst.extend(lst2)
print(lst)  # [1, 2, 3, 4, [5, 6], 5, 6]

# 通过切片来赋值
lst3 = [True, False]
lst[1:] = lst3  # 从第一个元素开始，切掉后边的所有元素，换成lst3中的元素
print(lst)  # [1, True, False]

print("元素修改")
lst = [1, 2, 3, 4]
# 给下标赋值来修改元素
lst[1] = 100
print(lst)  # [1, 100, 3, 4]
# 使用切片并赋值来修改
lst[1:3] = [10, 20]
print(lst)  # [1, 10, 20, 4]

print("元素删除")
lst = [1, 2, 3, 4, 5, 6, 2, 3]
lst.remove(2)  # 删除第一个出现的元素
print(lst)  # [1, 3, 4, 5, 6, 2, 3]
# lst.remove(7)  # 不存在的元素，删除抛出ValueError

# 可以使用pop删除指定下标的元素，不指定索引，删除最后一个元素
lst.pop()
print(lst)  # [1, 3, 4, 5, 6, 2]
lst.pop(0)
print(lst)  # [3, 4, 5, 6, 2]
# lst.pop(100)  # 下标不存在元素，抛出IndexError

# 切片操作至少删除一个元素，并且产生一个新的列表对象
lst4 = lst[2:]
print(lst4)  # [5, 6, 2]
print(lst)  # [3, 4, 5, 6, 2]
# 如果不想生成新的列表，可以给切片赋空值
lst[2:] = []  # 将第2个下标位置以后的元素全部删除
print(lst)  # [3, 4]

# 使用clear清除列表中的所有元素
lst.clear()
print(lst)
# 使用del会删除lst列表并将列表引用从内存中删除
del lst
# print(lst)  # NameError: 找不到lst变量了

'''
列表的排序：
1、通过sort排序，不产生新的列表
2、通过sorted排序，会产生新的列表，原列表不影响
'''

lst = [10, 8, 5, 9, 14]
print("排序前：", lst)  # 排序前： [10, 8, 5, 9, 14]
# 使用sort排序，默认为升序
lst.sort()
print("排序后：", lst)  # 排序后： [5, 8, 9, 10, 14]
# 传递reverse为True可以实现降序排序
lst.sort(reverse=True)
print("降序排序：", lst)  # 降序排序： [14, 10, 9, 8, 5]

lst = [10, 8, 5, 9, 14]
# 通过内置方法sorted排序，产生新的列表，默认为升序排序
sortedList = sorted(lst)
print(sortedList)  # [5, 8, 9, 10, 14]
# sorted降序
sortedList = sorted(lst, reverse=True)
print(sortedList)  # [14, 10, 9, 8, 5]
print(lst)  # [10, 8, 5, 9, 14]

'''
列表生成公式
'''
print("列表生成式")
lst = [item for item in range(10)]  # 根据range函数产生的列表创建新的列表
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [item ** 2 for item in range(10)]  # 创建的列表中的每个元素为range列表中的每个元素的二次方
print(lst)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成一个列表，元素为小于等于10的偶数
lst = [i * 2 for i in range(6)]
print(lst)  # [0, 2, 4, 6, 8, 10]
