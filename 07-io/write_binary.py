"""
写二进制文件
"""

# 先打开二进制文件
with open('avatar.gif', 'rb') as r:
    s = r.read()
    print(type(s))  # <class 'bytes'>
    # 'wb' 写入二进制文件
    with open('avatar_copy.gif', 'wb') as f:
        f.write(s)
