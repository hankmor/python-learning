
import os


# 使用循环
l = []
for v in os.listdir("."):
    l.append(v)
print(l)

# 使用列表生成式一行代码列举当前目录下的所有文件和目录
f = [x for x in os.listdir(".")]
print(f)
