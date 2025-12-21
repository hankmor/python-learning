class Date:
    """日期类"""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """
        替代构造函数（工厂方法）
        - cls是Date类本身
        - 可以创建实例
        - 解析字符串创建对象
        """
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)  # 调用__init__
    
    @classmethod
    def today(cls):
        """
        获取今天的日期
        - 类方法可以有多个
        - 提供不同的实例化方式
        """
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def is_prime(n):
        """
        判断质数
        - 不需要访问类或实例属性
        - 纯工具函数
        - 放在类里是为了组织代码
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

if __name__ == "__main__":
    # 使用Date
    date1 = Date(2024, 1, 15)           # 普通构造
    date2 = Date.from_string("2024-01-15")  # 类方法构造
    date3 = Date.today()                # 类方法构造
    
    print(date1)
    print(date2)
    print(date3)

    # 使用MathUtils
    print(MathUtils.is_prime(17))  # True
    print(MathUtils.factorial(5))  # 120
