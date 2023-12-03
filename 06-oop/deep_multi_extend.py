"""
python 支持使用多重继承
"""


# 具名的
class Nameable:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 动物
class Animal(Nameable):
    def call(self):
        print(f"{self.name} is calling")


# 可飞行的
class Flyable:
    def fly(self):
        print(f"{self.name} is flying")


class Bird(Animal, Flyable):
    pass


swift = Bird()
swift.name = "swift"
swift.call()  # swift is calling
swift.fly()  # swift is flying
