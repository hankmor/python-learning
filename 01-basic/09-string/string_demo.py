# Python教程07：字符串深入
# 1. 字符串的创建
s1 = 'Hello'
s2 = "World"
s3 = """这是一个
多行
字符串"""
s4 = '''也可以用
单引号'''
path = r"C:\Users\name\documents"  # 原始字符串
full = s1 + " " + s2

print(f"s1: {s1}")
print(f"path: {path}")

# 2. 字符串格式化
name = "张三"
age = 25
print("我叫%s，今年%d岁" % (name, age))

# format()
print("{}+{}={}".format(1, 2, 3))
print("{name}今年{age}岁".format(name="李四", age=30))
print("{:.2f}".format(3.14159))

# f-string (推荐)
name = "王五"
age = 28
city = "北京"
print(f"{name}今年{age}岁，来自{city}")
print(f"明年我{age + 1}岁")
pi = 3.14159
print(f"π ≈ {pi:.2f}")

# 3. 索引和切片
text = "Python"
print(f"text[0]: {text[0]}")
print(f"text[-1]: {text[-1]}")
print(f"text[0:3]: {text[0:3]}")
print(f"text[::-1]: {text[::-1]}")  # 反转

# 4. 常用方法
s = "Hello World"
print(s.upper())
print(s.lower())

s = "Python is awesome, Python is easy"
print(s.replace("Python", "Go"))
print(s.split(","))

fruits = ["apple", "banana", "orange"]
print(",".join(fruits))

s = "  Hello World  \n"
print(f"|{s.strip()}|")

# 5. 编码
s = "你好"
b = s.encode("utf-8")
print(f"Encoded: {b}")
print(f"Decoded: {b.decode('utf-8')}")
