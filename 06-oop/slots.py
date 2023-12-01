"""
slots 是 python 的一只机制，用来限制给 class 动态添加的属性列表，只能添加 __slots__ 变量定义的属性
"""


from types import MethodType


class User():
    pass


# 动态给实例添加属性
u1 = User()
u1.name = "zhangsan"
print(u1.name)  # zhangsan
# 由于 name 只有 u1 实例有，所以 u2 并没有，访问报错
u2 = User()
# print(u2.name)  # AttributeError: 'User' object has no attribute 'name'


def set_age(self, age):
    self.age = age


# 动态给实例增加方法，需要用到 MethodType
u1.set_age = MethodType(set_age, u1)
u1.set_age(20)
print(u1.age)  # 20
# 同样，u2 并没有这个方法
# u2.set_age(21) # AttributeError: 'User' object has no attribute 'set_age'


# 如果给 class 动态添加方法就没有问题了，所有实例都可以调用
User.set_age = set_age
u2.set_age(21)
print(u2.age)  # 21
# 也可以给 class 添加属性
User.hobby = ""
print(u1.hobby)  # ""
print(u2.hobby)  # ""


# 如果不想调用者无限制的给 class 添加属性，可以使用 __slots__ 特殊属性

class Student():
    __slots__ = ("number", "score")  # 这个是一个 tuple，定义了可以支持的动态属性


hank = Student()
hank.number = "123"
print(hank.number)
# 如果定义了不支持的属性，会报错
# hank.hobby = "coding" # AttributeError: 'Student' object has no attribute 'hobby'


class PrimaryStudent(Student):
    pass


# 需要注意的是 __slots__ 不会子类起作用，子类需要单独定义
jason = PrimaryStudent()
# 可以定义 hobby 而不受父类限制
jason.hobby = "play"
print(jason.hobby)


class PreschoolChild(Student):
    __slots__ = ("age")


# 如果子类自定义了 __slots__，那么它可以定义的属性就是自身的 + 父类的
jimmy = PreschoolChild()
jimmy.number = 3
print(jimmy.number)
jimmy.age = 5  # 3
print(jimmy.age)  # 5
# 无法定义不支持的 hobby，报错：AttributeError: 'PreschoolChild' object has no attribute 'hobby'
# jimmy.hobby = "eat"
