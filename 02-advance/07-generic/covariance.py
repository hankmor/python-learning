from typing import Generic, TypeVar

# covariance 允许子类型的容器替代父类型的容器, 称为协变类型
# 协变不允许作为输入参数，允许子类型的容器替代父类型的容器，作为输入参数可能导致类型非预期
T = TypeVar("T", covariant=True)


class Animal:
    def speak(self) -> str:
        return "Generic sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:  # 仅读取
        return self.item


def process_container(container: Container[Animal]) -> None:
    print(container.get_item().speak())


# 使用
dog_container = Container[Dog](Dog())
process_container(dog_container)  # 有效：Container[Dog] 可替代 Container[Animal]
