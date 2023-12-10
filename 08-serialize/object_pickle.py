"""
对象序列化，python 使用 pickle 包
"""
import pickle

#  创建一个 dict
d = dict(a=1, b=3.1415, c="hello")
# 序列化 d 到文件中
with open("dict.serialized", "wb") as f:
    # 将实例 d 序列化到文件 f
    pickle.dump(d, f)

# 反序列化
with open("dict.serialized", "rb") as f:
    # load 方法反序列化文件到对象
    d = pickle.load(f)
    print(type(d))  # <class 'dict'>
    print(d)  # {'a': 1, 'b': 3.1415, 'c': 'hello'}
    print(d['a'])
