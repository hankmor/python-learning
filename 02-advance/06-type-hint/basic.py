def greet(name: str) -> str:
    """给方法参数加上类型提示，这样静态工具mypy等可以检查并给出错误"""
    return f"Hello, {name}"


greet("Alice")
# greet(123)  # mypy will raise an error here

# mypy --strict type-hint.py
