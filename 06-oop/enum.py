"""
定义枚举类
"""
from enum import Enum

# 使用枚举，需要定义枚举类
MONTH = Enum("MONTH", "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC")
# 值
print(MONTH.JAN)  # MONTH.JAN
# 下标，默认从 1 开始
print(MONTH.JAN.value)  # 1

# 遍历枚举
for name, v in MONTH.__members__.items():
    print(name, "->", v, v.value)


# JAN -> MONTH.JAN 1
# FEB -> MONTH.FEB 2
# MAR -> MONTH.MAR 3
# APR -> MONTH.APR 4
# MAY -> MONTH.MAY 5
# JUN -> MONTH.JUN 6
# JUL -> MONTH.JUL 7
# AUG -> MONTH.AUG 8
# SEP -> MONTH.SEP 9
# OCT -> MONTH.OCT 10
# NOV -> MONTH.NOV 11
# DEC -> MONTH.DEC 12


# 想要自定义枚举，可以继承

class Month(Enum):
    # 自定义一月从 0 开始
    JAN = 0
    FEB = 1
    MAR = 2
    APR = 3
    MAY = 4
    JUN = 5
    JUL = 6
    AUG = 7
    SEP = 8
    OCT = 9
    NOV = 10
    DEC = 11


jan = Month.JAN
print(jan)  # Month.JAN
print(jan.value)  # 0
print(Month['JAN'])  # Month.JAN
print(jan == Month.JAN)  # True
print(Month(0))  # Month.JAN
# 超过出抛出异常
# print(Month(12)) # ValueError: 12 is not a valid Month
