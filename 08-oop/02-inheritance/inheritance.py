class Animal:
    """动物类（父类）"""
    
    def __init__(self, name, age):
        """初始化动物"""
        self.name = name
        self.age = age
    
    def eat(self):
        """吃东西（所有动物都会吃）"""
        return f"{self.name} is eating"
    
    def sleep(self):
        """睡觉"""
        return f"{self.name} is sleeping"

class Dog(Animal):
    """狗类（子类）- 继承Animal"""
    
    def bark(self):
        """狗叫（狗特有的方法）"""
        return f"{self.name} says: Woof!"

class Cat(Animal):
    """猫类（子类）- 继承Animal"""
    
    def meow(self):
        """猫叫（猫特有的方法）"""
        return f"{self.name} says: Meow!"

if __name__ == "__main__":
    # 使用
    dog = Dog("Buddy", 3)
    print(dog.eat())   # 继承自Animal：Buddy is eating
    print(dog.bark())  # Dog自己的方法：Buddy says: Woof!

    cat = Cat("Whiskers", 2)
    print(cat.eat())   # 继承自Animal：Whiskers is eating
    print(cat.meow())  # Cat自己的方法：Whiskers says: Meow!
