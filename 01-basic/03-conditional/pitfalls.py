# 常见陷阱

print("--- 陷阱 1：赋值 vs 比较 ---")
x = 10

# 错误：赋值，不是比较
# if x = 10:  # SyntaxError: invalid syntax
#     print("x是10")

# 正确：比较
if x == 10:
    print("x是10")

print("\n--- 陷阱 2：浮点数比较 ---")
# 不要直接比较浮点数
val = 0.1 + 0.2
if val == 0.3:  # False！
    print("相等")
else:
    print(f"不相等: {val} != 0.3")

# 应该比较差值的绝对值
if abs(val - 0.3) < 0.0001:
    print("近似相等")

print("\n--- 陷阱 3：空列表的判断 ---")
my_list = []

# 不推荐
if len(my_list) == 0:
    print("列表为空(不推荐写法)")

# 推荐（Pythonic）
if not my_list:
    print("列表为空(推荐写法)")
