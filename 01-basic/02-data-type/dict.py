"""
字段数据类型：key=value的键值对，对象用{}表示，列表用的是[]
1、字典是无序的，通过hash计算内存存储位置
2、字典的key必须是不可变序列，即不能进行增删改，如字符串，可变的如列表
"""
# 相当于JSON中的对象，Java中的Map

# 创建空字典
dict1 = {}
dict2 = dict()
print(dict1, id(dict1), type(dict1))
print(dict2, id(dict2), type(dict2))

# 创建字典: key: value的格式
dict1 = {"name": '张三', "age": 10, "from": 'china'}
print(dict1)

# 获取元素的值
print(dict1['name'])  # 如果key不存在，会抛出异常
print(dict1.get("name"))  # 如果key不存在，返回none
print(dict1.get("name1"))  # 如果key不存在，返回None,第二个参数为指定的值
print(dict1.get("name1", "unknown-user"))  # unknown-user
# 删除元素，使用pop方法
dict1.pop("name") # {'age': 10, 'from': 'china'}
print(dict1)

# 遍历字典
for key in dict1:
    print(key, ": ", dict1[key])


# 获取字典的key或value
print(dict1.keys())
print(dict1.values())
# output:
# dict_keys(['name', 'age', 'from'])
# dict_values(['张三', 10, 'china'])
