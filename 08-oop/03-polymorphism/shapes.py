from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """图形抽象基类"""
    
    @abstractmethod
    def area(self):
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass
    
    def describe(self):
        """描述图形"""
        return f"{self.__class__.__name__}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

class Circle(Shape):
    """圆形"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """矩形"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """三角形"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # 海伦公式
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

def print_shape_info(shape: Shape):
    """
    打印图形信息
    - 统一接口
    - 多态：不同图形有不同的计算方式
    """
    print(shape.describe())

if __name__ == "__main__":
    # 使用
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print_shape_info(shape)
