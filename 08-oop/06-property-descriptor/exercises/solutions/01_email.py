"""
练习1：Email类
用property验证邮箱格式
"""

import re

class Email:
    """
    邮箱类
    - 使用property验证邮箱格式
    - 提供domain只读属性
    """
    
    def __init__(self, address):
        """初始化邮箱"""
        self.address = address  # 触发setter验证
    
    @property
    def address(self):
        """获取邮箱地址"""
        return self._address
    
    @address.setter
    def address(self, value):
        """
        设置邮箱地址（带验证）
        验证规则：
        - 包含@
        - @前后都有内容
        - 包含.
        - 符合基本邮箱格式
        """
        if not isinstance(value, str):
            raise TypeError("邮箱地址必须是字符串")
        
        # 简单正则验证
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError(f"无效的邮箱格式：{value}")
        
        self._address = value
    
    @property
    def username(self):
        """获取用户名（只读）"""
        return self._address.split('@')[0]
    
    @property
    def domain(self):
        """获取域名（只读）"""
        return self._address.split('@')[1]
    
    def __str__(self):
        return self._address
    
    def __repr__(self):
        return f"Email('{self._address}')"


# 测试
if __name__ == "__main__":
    # 正常邮箱
    email = Email("user@example.com")
    print(f"邮箱：{email}")
    print(f"用户名：{email.username}")
    print(f"域名：{email.domain}")
    
    # 修改邮箱
    email.address = "newuser@example.org"
    print(f"\n新邮箱：{email}")
    print(f"用户名：{email.username}")
    print(f"域名：{email.domain}")
    
    # 测试验证
    try:
        invalid = Email("invalid.email")
    except ValueError as e:
        print(f"\n✓ 捕获错误：{e}")
    
    try:
        email.address = "no-at-sign"
    except ValueError as e:
        print(f"✓ 捕获错误：{e}")
    
    # 尝试设置只读属性
    try:
        email.domain = "newdomain.com"
    except AttributeError as e:
        print(f"✓ 域名是只读的：can't set attribute")
