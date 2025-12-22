# 字符串实用技巧与不可变性
from string import Template

print("--- 技巧1：字符串模板 ---")
t = Template("$name今年$age岁")
result = t.substitute(name="赵六", age=32)
print(result)

print("\n--- 技巧2：多行字符串格式化 ---")
data = {
    "name": "Python",
    "version": "3.11",
    "year": 2023
}
info = f"""
编程语言：{data['name']}
版本：{data['version']}
发布年份：{data['year']}
"""
print(info.strip())

print("\n--- 技巧3：字符串对齐 ---")
s = "Hello"
print(f"Ljust: |{s.ljust(10, '*')}|")
print(f"Rjust: |{s.rjust(10, '*')}|")
print(f"Center: |{s.center(10, '*')}|")

print("\n--- 不可变性演示 ---")
immutable_s = "Python"
try:
    # 尝试修改会报错
    # immutable_s[0] = 'J'
    pass
except TypeError as e:
    print(f"Error: {e}")

# 正确做法：创建新字符串
new_s = 'J' + immutable_s[1:]
print(f"Old: {immutable_s}, New: {new_s}")
