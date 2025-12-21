import json
import datetime

# 1. MRO 示例
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def method(self):
        print("D.method")
        super().method()

# 2. Mixin 示例
class LogMixin:
    """日志Mixin"""
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.__class__.__name__}: {message}")

class SerializeMixin:
    """序列化Mixin"""
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
    
    def to_json(self):
        return json.dumps(self.to_dict(), default=str)

class User:
    """用户基类"""
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def update_email(self, email):
        self.email = email

class EnhancedUser(User, LogMixin, SerializeMixin):
    """增强的用户类"""
    def update_email(self, email):
        old = self.email
        super().update_email(email)
        self.log(f"邮箱从{old}更新为{email}")

if __name__ == "__main__":
    # MRO 测试
    print("MRO:", D.__mro__)
    d = D()
    d.method()
    print("-" * 20)

    # Mixin 测试
    user = EnhancedUser("alice", "alice@old.com")
    user.log("用户创建")
    print(user.to_json())
    
    user.update_email("alice@new.com")
    print(user.to_json())
