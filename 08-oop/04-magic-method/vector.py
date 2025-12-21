class Vector:
    """二维向量"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """加法: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """减法: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """乘法: v * 3"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """除法: v / 2"""
        return Vector(self.x / scalar, self.y / scalar)
    
    def __neg__(self):
        """取负: -v"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """绝对值/模: abs(v)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    # 使用
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(v1 + v2)  # Vector(4, 6)
    print(v1 - v2)  # Vector(-2, -2)
    print(v1 * 3)   # Vector(3, 6)
    print(v1 / 2)   # Vector(0.5, 1.0)
    print(-v1)      # Vector(-1, -2)
    print(abs(v1))  # 2.23606...
