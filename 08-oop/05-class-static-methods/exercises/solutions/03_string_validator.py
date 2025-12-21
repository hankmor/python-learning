"""
练习3：字符串验证工具类
包含各种字符串验证的静态方法
"""

import re

class StringValidator:
    """字符串验证工具类"""
    
    @staticmethod
    def is_email(email):
        """
        验证邮箱格式（静态方法）
        - 简单验证：包含@和.
        - 不需要访问类或实例状态
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_phone(phone):
        """
        验证手机号（中国）
        格式：1开头的11位数字
        """
        pattern = r'^1[3-9]\d{9}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def is_strong_password(password):
        """
        验证强密码
        要求：至少8位，包含大小写字母、数字和特殊字符
        """
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
        
        return all([has_upper, has_lower, has_digit, has_special])
    
    @staticmethod
    def is_palindrome(s):
        """
        判断是否为回文
        忽略空格和大小写
        """
        s = s.replace(' ', '').lower()
        return s == s[::-1]
    
    @staticmethod
    def is_numeric(s):
        """判断是否为数字"""
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def is_url(url):
        """验证URL格式"""
        pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        return re.match(pattern, url) is not None


# 测试
if __name__ == "__main__":
    print("=== 邮箱验证 ===")
    emails = [
        "test@example.com",
        "invalid.email",
        "user@domain.co.uk"
    ]
    for email in emails:
        result = "✓" if StringValidator.is_email(email) else "✗"
        print(f"{result} {email}")
    
    print("\n=== 手机号验证 ===")
    phones = [
        "13812345678",
        "12345678901",
        "18600001111"
    ]
    for phone in phones:
        result = "✓" if StringValidator.is_phone(phone) else "✗"
        print(f"{result} {phone}")
    
    print("\n=== 强密码验证 ===")
    passwords = [
        "weak",
        "Weak123",
        "Strong@123"
    ]
    for pwd in passwords:
        result = "✓" if StringValidator.is_strong_password(pwd) else "✗"
        print(f"{result} {pwd}")
    
    print("\n=== 回文验证 ===")
    strings = [
        "A man a plan a canal Panama",
        "racecar",
        "hello"
    ]
    for s in strings:
        result = "✓" if StringValidator.is_palindrome(s) else "✗"
        print(f"{result} {s}")
    
    print("\n=== 数字验证 ===")
    numbers = [
        "123",
        "3.14",
        "abc"
    ]
    for num in numbers:
        result = "✓" if StringValidator.is_numeric(num) else "✗"
        print(f"{result} {num}")
    
    print("\n=== URL验证 ===")
    urls = [
        "https://www.example.com",
        "http://example.com/path",
        "not_a_url"
    ]
    for url in urls:
        result = "✓" if StringValidator.is_url(url) else "✗"
        print(f"{result} {url}")
