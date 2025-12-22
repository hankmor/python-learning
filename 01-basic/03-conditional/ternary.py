# 三元表达式 (Conditional Expressions)

age = 20

# 传统写法
if age >= 18:
    status = "成年"
else:
    status = "未成年"
print(f"传统写法状态: {status}")

# 三元表达式写法
# 语法：值1 if 条件 else 值2
status = "成年" if age >= 18 else "未成年"
print(f"三元表达式状态: {status}")

# 更多示例
score = 85
result = "及格" if score >= 60 else "不及格"
print(f"考试结果: {result}")

x = 10
y = 20
max_value = x if x > y else y  # 获取最大值
print(f"最大值: {max_value}")

# 嵌套三元表达式（不推荐，难读）
# grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
