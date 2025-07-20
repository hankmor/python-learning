from typing import Generic, TypeVar


class Animal:
    def speak(self) -> str:
        return "Generic sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


T = TypeVar("T", bound=Animal, contravariant=True)


class Feeder(Generic[T]):
    def feed(self, item: T) -> None:  # 仅写入
        print(f"Feeding {item.speak()}")


def process_feeder(feeder: Feeder[Dog]) -> None:
    feeder.feed(Dog())


# 使用
animal_feeder = Feeder[Animal]()
process_feeder(animal_feeder)  # 有效：Feeder[Animal] 可替代 Feeder[Dog]
