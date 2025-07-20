from typing import TypeVar, Generic, Dict, List

T = TypeVar("T")  # 定义类型变量 T


def identity(value: T) -> T:
    return value


# 使用
x: int = identity(42)  # T 被推断为 int
y: str = identity("hello")  # T 被推断为 str
print(x, y)


Number = TypeVar("Number", int, float)  # 限制为 int 或 float


def add(a: Number, b: Number) -> Number:
    return a + b


print(add(1, 2))  # 有效：int
print(add(1.5, 2.5))  # 有效：float
# print(add("a", "b"))  # Mypy 报错：类型不匹配


class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item


# 使用
int_box = Box[int](42)  # Box 存储 int
str_box = Box[str]("hello")  # Box 存储 str

print(int_box.get_item())  # 输出: 42
print(str_box.get_item())  # 输出: hello


K = TypeVar("K")
V = TypeVar("V")


def create_mapping(keys: List[K], values: List[V]) -> Dict[K, V]:
    return dict(zip(keys, values))


# 使用
result = create_mapping([1, 2], ["a", "b"])  # Dict[int, str]
print(result)  # 输出: {1: 'a', 2: 'b'}


class Animal:
    def speak(self) -> str:
        return "Generic animal sound"


class Container(Generic[T]):
    def __init__(self, content: T):
        self.content = content


class AnimalContainer(Container[Animal]):
    def make_sound(self) -> str:
        return self.content.speak()


# 使用
animal = Animal()
container = AnimalContainer(animal)
print(container.make_sound())  # 输出: Generic animal sound
