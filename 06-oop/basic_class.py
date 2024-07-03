"""
python中，oop编程使用 class 关键字定义类
"""


# 定义User类，包含 name、age 两个属性
class User:
    # __init__就是构造器，创建 User 实例时必须指定 nage 和 age 两个参数，第一个参数 self 表明创建的实例本身，
    # python 解释器会自动添加
    def __init__(self, name, age):
        # 设置实例的name和age
        self.name = name
        # 将 age 标记为私有，如果前边有两个下划线，则表明该属性是私有的，不允许外部访问
        self.__age = age


# 创建 User 实例
zhangsan = User("zhangsan", 20)
# type 为 class
print(type(zhangsan))  # <class '__main__.User'>
# 实例，oxxxx 表示实例的内存地址
print(zhangsan)  # <__main__.User object at 0x103ed1610>
# 如果不指定构造参数，则会报错
# lisi = User() # TypeError: User.__init__() missing 2 required positional arguments: 'name' and 'age'
# 访问类实例的属性
print(zhangsan.name)  # zhangsan
# 如果访问私有属性会报错
# print(zhangsan.__age)  # AttributeError: 'User' object has no attribute '__age'
# 报错是因为 python 解释器将 __age改了个名字，变成了 _User__age 了，所以仍然可以被访问
print(zhangsan._User__age)  # 20
# 修改属性值
zhangsan.name = "张三"
print(zhangsan.name)  # 张三
# 如果试图去修改私有属性，其实并不会生效，看似修改成功了，但是实际上只是给实例 zhangsan 多加了一个 __age 属性
# 而真正的 __age 属性已经变成了 _User__age，其实它并没有被修改
zhangsan.__age = 21
print(zhangsan.__age)  # 21
print(zhangsan._User__age)  # 20
