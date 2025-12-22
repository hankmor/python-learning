# 正则表达式入门
import re

print("--- 查找 (search) ---")
text = "我的电话是13812345678，邮箱是test@example.com"
# 匹配手机号
phone = re.search(r"1\d{10}", text)
if phone:
    print(f"Found phone: {phone.group()}")

print("\n--- 查找所有 (findall) ---")
# 匹配邮箱
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"Found emails: {emails}")

print("\n--- 替换 (sub) ---")
date_text = "今天是2024-01-15"
# 替换日期格式
result = re.sub(r"\d{4}-\d{2}-\d{2}", "某年某月某日", date_text)
print(f"Original: {date_text}")
print(f"Replaced: {result}")

print("\n--- 分割 (split) ---")
data = "apple,banana;orange:grape"
# 匹配多个分隔符
parts = re.split(r"[,;:]", data)
print(f"Data: {data}")
print(f"Split parts: {parts}")
