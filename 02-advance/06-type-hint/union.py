from typing import Optional, Union

"""
Union: 表示参数可以是多种类型中的一种
"""


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


print(add(1, 2))
print(add(1.5, 2.5))

"""
也可以使用类型别名来简化类型提示
"""
Num = int | float  # Type alias for int or float


def add2(a: Num, b: Num) -> Num:
    return a + b


print(add2(1, 2))
print(add2(1.5, 2.5))


"""
如果需要结果可以为None，则可以如下方式, 几种写法结果一致
- Optional是python提供的类型，可以表示一个值可以是某种类型或None
- Union与Num | None等价, 都是表示可以是Num类型或None
"""


# def add3(a: Num, b: Num) -> Union[Num, None]:
# def add3(a: Num, b: Num) -> Num | None:
def add3(a: Num, b: Num) -> Optional[Num]:
    if a < 0 and b < 0:
        return None
    return a + b


print(add3(1, 2))
print(add3(-1, -2))  # Returns None
