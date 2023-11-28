"""
继承和多态
"""


class User():
    def __init__(self, name) -> None:
        self.__name = name

    # 定义问好的方法
    def say_hi(self):
        print("hello, i am %s" % self.__name)

    # 定义走路方法
    def walk(self):
        print(f"{self.__name} is walking")


# 定义Student继承了User类
class Student(User):
    # 重写府类User的walk方法
    def walk(self):
        # super()返回父类，先调用父类的 walk 方法
        super().walk()
        print("actually, i don't like walking")


# 创建 User 类的实例对象
zhangsan = User("zhangsan")
zhangsan.say_hi()  # hello, i am zhangsan
zhangsan.walk()  # zhangsan is walking
# 创建 Student 的实例
lisi = Student("lisi")
# 调用继承自父类的方法
lisi.say_hi()  # hello, i am lisi
# 调用自身复写的方法
lisi.walk()
# output:
# lisi is walking
# actually, i don't like walking


"""
python中的鸭子模型，这与 golang 类似
如果一个对象看起来像鸭子，那么它就是鸭子
"""


# 增加一个方法，接收一个 user 参数
def greeting(user):
    user.say_hi()


# user或者其子类都继承了 say_hi() 方法，可以传入 greeting
greeting(zhangsan)  # hello, i am zhangsan
greeting(lisi)  # hello, i am lisi


# 定义一个 Cat 类，虽然它没有继承 User，但是它具有 say_hi 方法，同样可以传入 greeting
class Cat():
    def say_hi(self):
        print("喵，喵~")


# 在 python 这类动态与中，没有强类型，所以只要类具有 say_hi 方法，都可以传入给 greeting
greeting(Cat())  # 喵，喵~
