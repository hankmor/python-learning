"""
列表基础练习题答案
"""

print("====练习1：偶数列表反转====")
# 1. 创建一个列表存储1-10的偶数，然后反转这个列表
evens = [i for i in range(1, 11) if i % 2 == 0]
print(f"原列表: {evens}")
evens.reverse()
print(f"反转后: {evens}")

print("\n====练习2：去重保持顺序====")


# 2. 写一个函数，去除列表中的重复元素并保持顺序
def remove_duplicates(lst):
    """
    去除列表重复元素并保持顺序
    方法：利用set去重，但set无序
    """
    if not lst:
        return []

    # 方法1：循环判断（适合保留顺序）
    result = []
    seen = set()  # 用set辅助判断，O(1)查找
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def remove_duplicates1(lst):
    """
    去除列表重复元素并保持顺序
    方法：新建列表判断
    """
    if not lst:
        return []

    # 方法2：新建列表
    result = []
    newlist = []
    for item in lst:
        if item not in newlist:
            result.append(item)
            newlist.append(item)
    return result


test_list = [1, 2, 3, 2, 1, 4, 5, 5]
print(f"原列表: {test_list}")
print(f"去重后: {remove_duplicates(test_list)}")
print(f"去重后: {remove_duplicates1(test_list)}")

print("\n====练习3：Flatten展平列表====")


# 3. 实现列表的flatten功能（把嵌套列表展平成一维列表）
def flatten(nested_list):
    """
    展平二维列表
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))  # 递归处理多层嵌套，否则直接extend到列表末尾
        else:
            result.append(item)
    return result


# 简单二维版本（如果不考虑递归）
def flatten_2d(nested_list):
    result = []
    for row in nested_list:
        if isinstance(row, list):
            result.extend(row)
        else:
            result.append(row)
    return result


nested = [[1, 2], [3, 4], [5], 6]  # 混合
print(f"原嵌套列表: {nested}")
print(f"展平后: {flatten(nested)}")

nested_simple = [[1, 2], [3, 4], [5, 6]]
print(f"二维列表: {nested_simple}")
print(f"展平后: {flatten_2d(nested_simple)}")

nested_simple = [
    [
        [1, 2],
        [11, 12],
    ],
    [[3, 4], [33, 44]],
    [5, 6],
]
print(f"二维列表: {nested_simple}")
print(f"展平后: {flatten(nested_simple)}")
