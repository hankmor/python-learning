"""
使用 os 模块获取系统信息
"""
import os

# ================================================
# 获取系统
# ================================================

print(os.name)  # 获取操作系统类型，posix，说明是 linux、macOS、unix 系统
print(os.uname())  # 系统详细信息
print(os.environ)  # 系统环境变量
for k, v in os.environ.items():
    print(k, ":", v)

# 获取某个变量的值
print(os.environ.get("GOPATH"))
print(os.environ.get("PATH"))

# ================================================
# 操作文件或目录
# ================================================

print(os.path.abspath("."))  # 获取当前目录的绝对路径
# 使用 os.path 的 join 方法，避免自己拼接字符串时考虑不同操作系统分隔符
s = os.path.join("/user/hank", "work")
print(s)
# 如果要分离 path 也是一样
p = os.path.split(s)  # /user/hank/work
print(p)  # ('/user/hank', 'work')
# 分离文件后缀
p = os.path.splitext("/user/hank/test.txt")
print(p)  # ('/user/hank/test', '.txt')

# 列出目录下的所有目录，只需要一行代码，使用列表生成式
d = [p for p in os.listdir("../../python-learning") if os.path.isdir(os.path.join("..", p))]
print(d)
# 列出所有的 .py 文件
d = [p for p in os.listdir(".") if os.path.isfile(p) and os.path.splitext(p)[1] == '.py']
print(d)
