words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
else: # 循环结束后执行else
    print("bye")

"""
遍历集合时修改集合的内容，会很容易生成错误的结果。因此不能直接进行循环，而是应遍历该集合的副本或创建新的集合
"""

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(users)

# 赋值然后修改集合的元素
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

# 创建新的集合
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(users)
print(active_users)