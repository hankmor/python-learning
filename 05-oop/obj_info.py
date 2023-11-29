"""
获取对象的信息
"""

# 判断对象的类型，用 type() 方法
import types


print(type(1))  # <class 'int'>
print(type("1"))  # <class 'str'>
print(type(abs))  # <class 'builtin_function_or_method'>


def fn():
    pass


# 判断类型是否相同，可以用 ==
print(type(1) == type(2))  # True
# 但是如果需要判断一个类型是否是函数，则需要使用 types 包
print(type(abs) == types.BuiltinFunctionType)  # True, 判断是否是内建函数
print(type(fn) == types.FunctionType)  # True, 判断是否是函数
print(type(lambda x: x * x) == types.LambdaType)  # True, 判断是否是 lambda 匿名函数
print(type((x * x for x in range(10))) ==
      types.GeneratorType)  # True, 判断是否是生成器


"""
如果需要判断对象是否是类的实例，需要使用 isinstance() 函数
"""


class User():
    pass


class Student(User):
    pass


zhangsan = Student()
print(isinstance(zhangsan, Student))  # True, zhangsan 是 Student 的实例
print(isinstance(zhangsan, User))  # True, 由于继承关系，zhangsan 仍然是 User 的实例
print(isinstance(1, int))  # True
print(isinstance("1", str))  # True
# isinstance 还可以判断是否是其中的一种类型实例
print(isinstance([1, 2, 3], (list, tuple)))  # True
print(isinstance((1, 2, 3), (list, tuple)))  # True


"""
想要获取对象的所有属性和方法，可以使用 dir() 函数
"""

print(dir(types.FunctionType))
print(dir(Student))


class Programer(User):
    def __init__(self, name, skills) -> None:
        super().__init__()
        self.name = name
        self.skills = skills


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
hank = Programer("hank", "java, go, python")
print(hasattr(hank, "name"))  # True
print(hasattr(hank, "skills"))  # True
setattr(hank, "name", "HANK")
print(hank.name)  # HANK
print(getattr(hank, "name"))  # HANK
# 不能访问不存在的属性
# age = getattr(hank, "age") # AttributeError: 'Programer' object has no attribute 'age'
# 但是可以定义默认值，不存在就返回默认值而不报错
age = getattr(hank, "age", 18)
print(age)  # 18
