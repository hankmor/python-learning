"""
定义枚举类
"""
from enum import Enum, unique

# 使用枚举，需要定义枚举类
# 传递 tuple
# MONTH = Enum("MONTH", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
# 传递字符串
MONTH = Enum("Month", "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
# 枚举中的元素可以直接按属性访问
print(MONTH.Jan)  # Month.Jan
# 名称
print(MONTH.Jan.name)  # Jan
# 值
print(MONTH.Jan.value)  # 1

# 遍历枚举
for name, v in MONTH.__members__.items():
    print(name, "->", v, v.value)


# Jan -> Month.Jan 1
# Feb -> Month.Feb 2
# Mar -> Month.Mar 3
# Apr -> Month.Apr 4
# May -> Month.May 5
# Jun -> Month.Jun 6
# Jul -> Month.Jul 7
# Aug -> Month.Aug 8
# Sep -> Month.Sep 9
# Oct -> Month.Oct 10
# Nov -> Month.Nov 11
# Dec -> Month.Dec 12


# 想要自定义枚举，可以继承

@unique  # unique装饰器表示枚举类的元素唯一
class Month(Enum):
    # 自定义一月从 0 开始
    Jan = 0
    Feb = 1
    Mar = 2
    Apr = 3
    May = 4
    Jun = 5
    Jul = 6
    Aug = 7
    Sep = 8
    Oct = 9
    Nov = 10
    Dec = 11


jan = Month.Jan
print(jan)  # Month.Jan
print(jan.value)  # 0
print(Month['Jan'])  # Month.Jan
print(jan == Month.Jan)  # True
print(Month(0))  # Month.Jan
# 超过出抛出异常
# print(Month(12)) # ValueError: 12 is not a valid Month
