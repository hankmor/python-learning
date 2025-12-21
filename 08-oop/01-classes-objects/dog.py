class Dog:
    """
    狗类
    - 定义狗的属性和行为
    - 这是一个简单的示例类
    """
    
    # 类属性（所有实例共享）
    species = "Canis familiaris"  # 物种
    
    def __init__(self, name, age):
        """
        初始化方法（构造函数）
        - self代表实例本身
        - name和age是实例属性
        
        Args:
            name: 狗的名字
            age: 狗的年龄
        """
        self.name = name  # 实例属性
        self.age = age
    
    def bark(self):
        """
        狗叫的方法
        - 实例方法的第一个参数必须是self
        """
        return f"{self.name} says: Woof!"
    
    def get_info(self):
        """获取狗的信息"""
        return f"{self.name} is {self.age} years old"

if __name__ == "__main__":
    # 创建对象（实例化）
    buddy = Dog("Buddy", 3)
    print(buddy.name)      # Buddy
    print(buddy.bark())    # Buddy says: Woof!
    print(buddy.get_info())  # Buddy is 3 years old
