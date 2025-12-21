class SingletonMeta(type):
    """单例元类"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """
        调用类创建实例时触发
        - 检查是否已有实例
        - 有则返回，无则创建
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string

class UpperAttrMeta(type):
    """
    元类：将所有属性名转为大写
    """
    def __new__(cls, name, bases, attrs):
        # 转换属性名为大写
        uppercase_attrs = {
            (key.upper() if not key.startswith('__') else key): value
            for key, value in attrs.items()
        }
        return super().__new__(cls, name, bases, uppercase_attrs)

class MyClass(metaclass=UpperAttrMeta):
    x = 10
    y = 20
    
    def hello(self):
        return "Hello"

if __name__ == "__main__":
    # 单例测试
    db1 = Database("localhost")
    db2 = Database("otherhost")  # 参数被忽略
    print(f"db1 is db2: {db1 is db2}")
    
    # 属性大写测试
    obj = MyClass()
    print(f"X: {obj.X}")
    print(f"HELLO: {obj.HELLO()}")
