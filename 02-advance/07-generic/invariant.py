from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):  # 默认不变性
    def __init__(self, item: T):
        self.item = item

    def set_item(self, item: T) -> None:
        self.item = item

    def get_item(self) -> T:
        return self.item


class Animal:
    pass


class Dog(Animal):
    pass


# 使用
dog_box = Box[Dog](Dog())
animal_box = Box[Animal](Animal())


# 不变性：Box[Dog] 和 Box[Animal] 互不兼容
def process_box(box: Box[Animal]) -> None:
    pass


# process_box(dog_box)  # Mypy 报错：Box[Dog] 不能替代 Box[Animal], 可以通过协变来接受子类型
process_box(animal_box)  # 没有问题
