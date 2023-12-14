"""
内置的 datetime 包用法示例
官方文档地址: https://docs.python.org/zh-cn/3/library/datetime.html
时区文档: https://docs.python.org/zh-cn/3/library/zoneinfo.html
"""
import re
# 注意这里的包为 datetime, 类也为 datetime
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# ================================================
# 获取当前时间
# ================================================

# 获取当前时间，调用类方法，时区为系统时区+08:00
now = datetime.now()
print(now)  # 2023-12-13 17:11:33.255865
# 获取当前 utc 时间
utcnow = datetime.utcnow()
print(utcnow)  # 2023-12-13 09:11:33.255955
# 指定时区，tz参数为一个 ZoneInfo 时区对象,美国洛杉矶西八区，-08:00
tznow = datetime.now(tz=ZoneInfo("America/Los_Angeles"))
print(tznow)  # 2023-12-13 01:11:33.956169-08:00

# ================================================
# 指定具体年月日时分秒创建 datetime 对象
# ================================================

# 指定时间
dt = datetime(year=2023, month=1, day=1, hour=23, minute=59, second=59)
print(dt)  # 2023-01-01 23:59:59
# 必须指定 year, month, day 参数
dt = datetime(2023, 1, 1)
print(dt)  # 2023-01-01 00:00:00

# ================================================
# datetime 与 timestamp 的相互转换
# ================================================

# datetime 转为 timestamp
now = datetime.now()
print(now)  # 2023-12-13 17:20:25.300688
# 转为 timestamp，它是一个浮点数整数部分表示秒
print(now.timestamp())  # 1702459259.859633

# timestamp 转为 datetime
ts = 1702459259.859633
dt = datetime.fromtimestamp(ts)
print(dt)  # 2023-12-13 17:20:59.859633
# 转为 utc 时间
dt = datetime.utcfromtimestamp(ts)
print(dt)  # 2023-12-13 09:20:59.859633

# ================================================
# str 与 datetime 的相互转换
# ================================================

# str 转为 datetime
s = '2023-12-13 17:20:59.859633'
# f 表示微秒
dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
print(dt)  # 2023-12-13 17:20:59.859633
s = '2023-12-13 17:20:59'
dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(dt)  # 2023-12-13 17:20:59

# datetime 转为 str
s = '2023-12-13 17:20:59'
dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
dts = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
print(dts)  # 2023-12-13 17:20:59
print(dts == s)  # True

# ================================================
# datetime加减
#
# 需要用到 timedelta 类，该类表示两个 date 对象或 time
# 对象，或者 datetime 对象之间的时间间隔，精确到微秒。类似
# Go 中的 During
# ================================================

# 创建 timedelta，3天1秒，半分钟，半小时
threedays = timedelta(days=3, seconds=1, minutes=0.5, hours=0.5)
print(threedays)  # 3 days, 0:30:31
print(threedays.days)  # 天数, 3
print(threedays.seconds)  # 时分秒表示的秒数, 1831
print(threedays.total_seconds())  # 这个时间间隔表示的总秒数(包括days), 261031.0
print(threedays.microseconds)  # 微秒, 0

dt = datetime.now()
print(dt)
# 计算当前时间3天以后的时刻
after3days = dt + timedelta(days=3)  # 2023-12-13 19:25:12.521336
print(after3days)  # 2023-12-16 19:25:12.521336
# 三天前的时刻
before3days = dt - timedelta(days=3)
print(before3days)  # 2023-12-10 19:41:36.838127

# 使用 timedelta 构建时区

# 获取当前时间传递 ZoneInfo 时区对象
# 美国位于西八区，比中国时间早 16 个小时
tznow = datetime.now(tz=ZoneInfo("America/Los_Angeles"))
print(tznow)  # 2023-12-13 03:47:46.742426-08:00
# 获取当前时间下指定时区的时间, 除了可以使用 ZoneInfo 对象外，还可以用 timedelta 创建 timezone
# 使用 timezone
tznow = datetime.now(tz=timezone(timedelta(hours=-8)))
print(tznow)  # 2023-12-13 03:47:46.742455-08:00

# ================================================
# 时区转换
# ================================================

# 如果能够获取到 utc0 的时间，就可以将其转为任意时区的时间，而不用考虑获取时间时的时区了
# 获取 utc 的当前时间，并设置时区为0，时间会带上 +00:00
utcnow = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utcnow)  # 2023-12-14 11:59:35.684088+00:00
# 转换时间到东八区
print(utcnow.astimezone(tz=timezone(timedelta(hours=8))))  # 2023-12-14 19:59:35.684088+08:00
# 转换时间到西八区
print(utcnow.astimezone(tz=timezone(timedelta(hours=-8))))  # 2023-12-14 03:59:35.684088-08:00

# ================================================
# 练习，输入时间 2015-6-1 08:10:30， UTC+7:00 两个字符串
# ================================================


# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

tz_regex = re.compile(r'^UTC([+\-]0?\d):00$')


def to_timestamp(dt_str, tz_str=None):
    # 按照正则匹配输入的时区
    m = tz_regex.match(tz_str)
    if not m:
        raise ValueError('invalid timezone, a valid input is like "UTC+08:00"')
    hours = int(m.group(1))
    # 将时间字符串转为 datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 这里的处理方式有多种
    # 1、给 datetime 指定时区，使用 replace 函数
    # dt_tz = dt.replace(tzinfo=timezone(timedelta(hours=hours)))
    # 2、减去给定的小时数就是 utc0 时间
    dt_tz = (dt - timedelta(hours=hours)).replace(tzinfo=timezone.utc)
    return dt_tz.timestamp()


# 指定的时区时间，如2015-6-1 08:10:30 UTC+7:00，utc 对应时间就是减去 7 个小时后的时间
# dt = datetime(2015, 6, 1, 1, 10, 30, tzinfo=timezone.utc)
# print(dt.timestamp()) # 1433121030.0

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
