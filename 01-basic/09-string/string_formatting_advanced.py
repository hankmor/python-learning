# 字符串格式化进阶

print("--- format()方法进阶 ---")
# 索引和顺序
print("{0}+{1}={2}".format(1, 2, 3))
print("{2}+{1}={0}".format(3, 2, 1))

# 关键字参数
print("{name}今年{age}岁".format(name="李四", age=30))

# 填充与对齐
print("{:0>5}".format(42))      # 00042（左侧填充0，总宽度5）
print("{:*^10}".format("Hi"))   # ****Hi****（居中，宽度10，填充*）

print("\n--- f-string进阶 ---")
# 表达式
age = 28
print(f"明年我{age + 1}岁")
print(f"2的10次方是{2 ** 10}")

# 对齐和填充
num = 42
print(f"Fill 0: {num:0>5}")    # 00042
print(f"Center: {num:*^10}")   # ****42****

# 调试输出（Python 3.8+）
x = 10
print(f"Debug: {x=}")  # x=10
