"""
练习2：计数器类
跟踪总共创建了多少个实例
"""

class Counter:
    """计数器类"""
    
    # 类属性：总实例数
    _total_count = 0
    
    def __init__(self, name):
        """初始化实例"""
        self.name = name
        self.count = 0
        # 增加总计数
        Counter._total_count += 1
        self.instance_id = Counter._total_count
    
    def increment(self):
        """实例计数+1"""
        self.count += 1
    
    def get_count(self):
        """获取实例计数"""
        return self.count
    
    @classmethod
    def get_total_count(cls):
        """
        获取总实例数（类方法）
        - 访问类属性
        - 不需要创建实例即可调用
        """
        return cls._total_count
    
    @classmethod
    def reset_total_count(cls):
        """重置总计数（主要用于测试）"""
        cls._total_count = 0
    
    def __str__(self):
        return f"Counter '{self.name}' (ID: {self.instance_id}, Count: {self.count})"


# 测试
if __name__ == "__main__":
    print(f"初始总数：{Counter.get_total_count()}")
    
    # 创建多个实例
    c1 = Counter("Counter 1")
    c2 = Counter("Counter 2")
    c3 = Counter("Counter 3")
    
    print(f"\n创建3个实例后，总数：{Counter.get_total_count()}")
    
    # 每个实例独立计数
    c1.increment()
    c1.increment()
    c2.increment()
    
    print(f"\n{c1}")
    print(f"{c2}")
    print(f"{c3}")
    
    # 验证可以通过实例调用类方法
    print(f"\n通过实例调用：{c1.get_total_count()}")
    
    # 创建更多实例
    c4 = Counter("Counter 4")
    print(f"\n创建第4个实例后，总数：{Counter.get_total_count()}")
