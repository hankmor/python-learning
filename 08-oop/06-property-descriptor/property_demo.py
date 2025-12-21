class Temperature:
    """温度类"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """获取摄氏温度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏温度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """
        计算华氏温度
        - 只读属性（没有setter）
        - 根据celsius动态计算
        """
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """通过华氏温度设置"""
        self._celsius = (value - 32) * 5/9

class Person:
    """使用property的Person类"""
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("名字不能为空")
        self._name = value
    
    @name.deleter
    def name(self):
        print(f"删除名字：{self._name}")
        del self._name

if __name__ == "__main__":
    t = Temperature(25)
    print(f"摄氏度: {t.celsius}, 华氏度: {t.fahrenheit}")
    
    t.celsius = 30
    print(f"摄氏度: {t.celsius}, 华氏度: {t.fahrenheit}")
    
    p = Person("Alice")
    print(p.name)
    p.name = "Bob"
    # p.name = "" # ValueError
