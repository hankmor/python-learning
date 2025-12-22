# 嵌套条件
age = 20
has_id = True

print("--- 嵌套条件示例 ---")
if age >= 18:
    if has_id:
        print("验证通过，可以进入")
    else:
        print("请出示身份证")
else:
    print("未成年，不能进入")

# 条件表达式的真假值
print("\n--- 真假值示例 ---")
name = "张三"
if name:  # 非空字符串为True
    print(f"你好，{name}")

numbers = []
if not numbers:  # 空列表为False，not后变为True
    print("列表为空")

count = 0
if count:  # 0为False
    print("有数据")
else:
    print("没有数据")

# 逻辑组合
print("\n--- 逻辑组合示例 ---")
age = 25
has_license = True

# and：都为True
if age >= 18 and has_license:
    print("可以开车")

# or：有一个为True
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("可以休息")

# not：取反
is_raining = False
if not is_raining:
    print("可以出门")

# 复杂组合
score = 85
attendance = 0.9
if score >= 60 and (attendance >= 0.8 or score >= 90):
    print("通过考试")
