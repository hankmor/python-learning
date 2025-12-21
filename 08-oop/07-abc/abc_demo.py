from abc import ABC, abstractmethod

class Shape(ABC):
    """抽象形状类"""
    
    @abstractmethod
    def area(self):
        """计算面积（抽象方法）"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长（抽象方法）"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Payment(ABC):
    """支付抽象基类"""
    
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def process_payment(self):
        """处理支付（抽象）"""
        pass
    
    def validate_amount(self):
        """验证金额（具体方法）"""
        if self.amount <= 0:
            raise ValueError("金额必须大于0")
        return True

class CreditCardPayment(Payment):
    """信用卡支付"""
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def process_payment(self):
        self.validate_amount()
        return f"用信用卡{self.card_number}支付${self.amount}"

if __name__ == "__main__":
    c = Circle(5)
    print(f"Area: {c.area():.2f}, Perimeter: {c.perimeter():.2f}")
    
    payment = CreditCardPayment(100, "1234-5678")
    print(payment.process_payment())
