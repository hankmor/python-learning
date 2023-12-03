"""
class 中的方法
"""


class User():
    # 定义了两个私有属性
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    # 暴露方法给外部访问，其实就是 java 的 getter， settter
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


zhangsan = User("zhangsan", 20)
print(zhangsan.get_name())  # zhangsan
print(zhangsan.get_age())  # 20
zhangsan.set_name("张三")
zhangsan.set_age(21)
print(zhangsan.get_name())  # 张三
print(zhangsan.get_age())  # 21
