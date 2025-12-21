"""
练习3：RangeValidator描述符
验证数值在指定范围内
"""

class RangeValidator:
    """
    范围验证描述符
    - 验证数值在min_value和max_value之间
    - 支持可选的最小值和最大值
    """
    
    def __init__(self, min_value=None, max_value=None, inclusive=True):
        """
        初始化
        Args:
            min_value: 最小值（None表示无限制）
            max_value: 最大值（None表示无限制）
            inclusive: 是否包含边界值
        """
        self.min_value = min_value
        self.max_value = max_value
        self.inclusive = inclusive
        self.name = None
    
    def __set_name__(self, owner, name):
        """自动获取属性名"""
        self.name = name
    
    def __get__(self, instance, owner):
        """获取属性值"""
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        """
        设置属性值（带验证）
        - 验证类型
        - 验证范围
        """
        # 类型检查
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name}必须是数字")
        
        # 范围检查
        if self.min_value is not None:
            if self.inclusive:
                if value < self.min_value:
                    raise ValueError(
                        f"{self.name}不能小于{self.min_value}，得到{value}"
                    )
            else:
                if value <= self.min_value:
                    raise ValueError(
                        f"{self.name}必须大于{self.min_value}，得到{value}"
                    )
        
        if self.max_value is not None:
            if self.inclusive:
                if value > self.max_value:
                    raise ValueError(
                        f"{self.name}不能大于{self.max_value}，得到{value}"
                    )
            else:
                if value >= self.max_value:
                    raise ValueError(
                        f"{self.name}必须小于{self.max_value}，得到{value}"
                    )
        
        # 通过验证，设置值
        instance.__dict__[self.name] = value


class Rectangle:
    """
    矩形类
    - 使用RangeValidator验证宽度和高度
    """
    width = RangeValidator(min_value=0, inclusive=False)  # 必须>0
    height = RangeValidator(min_value=0, inclusive=False)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        """面积"""
        return self.width * self.height
    
    @property
    def perimeter(self):
        """周长"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class Student:
    """
    学生类
    - 使用RangeValidator验证年龄和分数
    """
    age = RangeValidator(min_value=0, max_value=150)
    score = RangeValidator(min_value=0, max_value=100)
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, score={self.score})"


# 测试
if __name__ == "__main__":
    print("=== 测试Rectangle ===")
    r = Rectangle(5, 10)
    print(r)
    print(f"面积：{r.area}")
    print(f"周长：{r.perimeter}")
    
    # 修改尺寸
    r.width = 8
    print(f"\n修改后：{r}")
    print(f"面积：{r.area}")
    
    # 测试验证
    try:
        r.width = 0
    except ValueError as e:
        print(f"\n✓ 捕获错误：{e}")
    
    try:
        r.height = -5
    except ValueError as e:
        print(f"✓ 捕获错误：{e}")
    
    print("\n=== 测试Student ===")
    s = Student("Alice", 20, 85)
    print(s)
    
    # 测试范围验证
    test_cases = [
        ("age", -1, "年龄不能为负"),
        ("age", 200, "年龄超过150"),
        ("score", 101, "分数超过100"),
        ("score", -10, "分数为负")
    ]
    
    for attr, value, desc in test_cases:
        try:
            setattr(s, attr, value)
        except ValueError as e:
            print(f"✓ {desc}：{e}")
