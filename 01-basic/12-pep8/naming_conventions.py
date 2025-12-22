# 命名约定 (Naming Conventions)

# 1. 变量和函数：snake_case
user_name = "Alice"
total_count = 100

def calculate_sum(numbers):
    return sum(numbers)

# 2. 常量：UPPER_CASE
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159

# 3. 类名：PascalCase
class UserManager:
    pass

class HTTPConnection:
    pass

# 4. 私有变量和方法
class MyClass:
    def __init__(self):
        self.public_var = "公开"
        self._protected_var = "受保护" # 单下划线
        self.__private_var = "私有"   # 双下划线

    def public_method(self):
        pass

    def _protected_method(self):
        pass

    def __private_method(self):
        pass
