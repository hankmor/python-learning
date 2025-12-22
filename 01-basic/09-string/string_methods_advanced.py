# 字符串方法进阶

s = "Hello World"
print("--- 大小写转换 ---")
print(f"Original: {s}")
print(f"Capitalize: {s.capitalize()}")  # 首字母大写
print(f"Title: {s.title()}")           # 每个单词首字母大写
print(f"Swapcase: {s.swapcase()}")     # 大小写互换

print("\n--- 查找 ---")
text = "Python is awesome, Python is easy"
print(f"Text: {text}")
print(f"Find 'Python': {text.find('Python')}")      # 0
print(f"Find 'Java': {text.find('Java')}")        # -1
print(f"Count 'Python': {text.count('Python')}")     # 2

print("\n--- 这里是分割和分行 ---")
# 分行
multiline = "Line1\nLine2\nLine3"
print(f"Splitlines: {multiline.splitlines()}")

print("\n--- 去除空白 ---")
ws_str = "  Hello World  \n"
print(f"Lstrip: |{ws_str.lstrip()}|")  # 去除左侧
print(f"Rstrip: |{ws_str.rstrip()}|")  # 去除右侧

print("\n--- 判断方法 ---")
check_str = "Python123"
print(f"String: {check_str}")
print(f"Startswith 'Py': {check_str.startswith('Py')}")
print(f"Endswith '123': {check_str.endswith('123')}")
print(f"Isalpha: {check_str.isalpha()}")
print(f"Isalnum: {check_str.isalnum()}")
print(f"Digit check: {'123'.isdigit()}")
