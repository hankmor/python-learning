from typing import List, Sequence

Num = int | float

ns: List[Num] = [1, 2, 4]


def print_list(lst: List[Num]):
    for x in lst:
        print(x)
    lst.append(
        5.1
    )  # 可以修改列表, 增加了风险，应为Num可以是int或float类型，可能会导致类型不一致的情况


print_list(ns)
"""
是否可以处理List[int]？

运行时没有问题，但是mypy会检测是出错：
list.py:19: error: Argument 1 to "print_list" has incompatible type "list[int]"; expected "list[int | float]"  [arg-type]
list.py:19: note: "list" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
list.py:19: note: Consider using "Sequence" instead, which is covariant
Found 1 error in 1 file (checked 1 source file)

此时可以使用 Sequence 来替代 List，这样就可以处理 List[int] 了

Sequence 无法使用append函数来修改list。
"""

# ints: List[int] = [1, 2, 3]
# print_list(ints) # 无法通过mypy的检查


def print_list2(lst: Sequence[Num | int]):
    for x in lst:
        print(x)
    # lst.append(
    #     1.1
    # )  # mypy会检查出问题: list.py:38: error: "Sequence[int | float | int]" has no attribute "append"  [attr-defined]


ints: List[int] = [1, 2, 3]
print_list2(ints)  # 现在可以通过mypy的检查了
