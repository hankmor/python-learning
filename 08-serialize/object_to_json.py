"""
将对象序列化为 json，python json 包
"""
import json

# ================================================
# 将 dict 序列化为 json
# ================================================

#  创建一个 dict
d = dict(a=1, b=3.1415, c="hello")
# dumps 方法将对象序列化为 json
s = json.dumps(d)
print(s)  # {"a": 1, "b": 3.1415, "c": "hello"}

# 反序列化
d = json.loads(s)
print(type(d))  # <class 'dict'>
print(d)  # {'a': 1, 'b': 3.1415, 'c': 'hello'}


# ================================================
# 将 class 序列化为 json
# ================================================

class User():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


# 创建 User 对象实例
u = User("zhangsan", 1, 20)


# 直接序列化会抛异常, 因为 python 不知道如何去序列化 User 对象
# s = json.dumps(u) # TypeError: Object of type User is not JSON serializable


# 我们可以专门写两个序列化和反序列化函数
def user_to_json(user):
    """ 定义如何将 user 转换为可序列化的 dict """
    return {"name": user.name, "gender": user.gender, "age": user.age}


def json_to_user(json_dict):
    """ 定义如何将 json 反序列化 user """
    return User(json_dict["name"], json_dict["gender"], json_dict["age"])


# 然后，序列化和反序列化时使用这两个函数
# default 参数定义如何将对象转换为可序列化的对象，比如这里转换为 dict
s = json.dumps(u, default=user_to_json)
print(s)  # {"name": "zhangsan", "gender": 1, "age": 20}
# object_hook 函数用于反序列化 json 为对象
u = json.loads(s, object_hook=json_to_user)
print(type(u))  # <class '__main__.User'>
print(u)  # <__main__.User object at 0x107028be0>

# 如果每一个对象我们都这么定义两个函数还是有点麻烦
# 其实，每个对象(除了定义了 __slots__ 属性的 class)都有一个 __dict__ 属性，它就是一个 dict，用来存储实例
# 可以直接使用它来序列化
s = json.dumps(u, default=lambda x: x.__dict__)
print(s)
# 但是在反序列化时，还是需要编写方法来告诉 python 如何反序列化
