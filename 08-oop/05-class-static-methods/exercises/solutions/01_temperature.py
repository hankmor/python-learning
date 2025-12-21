"""
练习1：Temperature类
实现摄氏度和华氏度的转换
"""

class Temperature:
    """温度类"""
    
    def __init__(self, celsius):
        """初始化（摄氏度）"""
        self.celsius = celsius
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """
        从华氏度创建（类方法）
        公式：C = (F - 32) * 5/9
        """
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)
    
    @classmethod
    def from_kelvin(cls, kelvin):
        """
        从开尔文创建（类方法）
        公式：C = K - 273.15
        """
        celsius = kelvin - 273.15
        return cls(celsius)
    
    def to_fahrenheit(self):
        """
        转换为华氏度
        公式：F = C * 9/5 + 32
        """
        return self.celsius * 9 / 5 + 32
    
    def to_kelvin(self):
        """
        转换为开尔文
        公式：K = C + 273.15
        """
        return self.celsius + 273.15
    
    def __str__(self):
        return f"{self.celsius}°C"


# 测试
if __name__ == "__main__":
    # 方式1：直接创建
    t1 = Temperature(25)
    print(f"温度：{t1}")
    print(f"华氏度：{t1.to_fahrenheit()}°F")
    print(f"开尔文：{t1.to_kelvin()}K")
    
    # 方式2：从华氏度创建
    t2 = Temperature.from_fahrenheit(77)
    print(f"\n从77°F创建：{t2}")
    
    # 方式3：从开尔文创建
    t3 = Temperature.from_kelvin(298.15)
    print(f"从298.15K创建：{t3}")
