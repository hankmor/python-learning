# 1. 单例模式
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. 工厂模式
class Circle:
    def draw(self): return "Circle"
class Rectangle:
    def draw(self): return "Rectangle"

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Unknown shape type")

# 3. 观察者模式
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")

if __name__ == "__main__":
    # Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(f"Singleton: {s1 is s2}")
    
    # Factory
    shape = ShapeFactory.create_shape("circle")
    print(shape.draw())
    
    # Observer
    sub = Subject()
    sub.attach(Observer("Obs1"))
    sub.attach(Observer("Obs2"))
    sub.notify("Hello Observers")
