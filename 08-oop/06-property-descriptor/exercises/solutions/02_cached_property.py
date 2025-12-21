"""
练习2：cached_property描述符
实现一个懒加载并缓存结果的属性描述符
"""

class cached_property:
    """
    缓存属性描述符
    - 第一次访问时计算值
    - 后续访问返回缓存值
    - 类似functools.cached_property
    """
    
    def __init__(self, func):
        """
        初始化
        Args:
            func: 计算属性值的函数
        """
        self.func = func
        self.attrname = None
        self.__doc__ = func.__doc__
    
    def __set_name__(self, owner, name):
        """
        Python 3.6+特性
        - 自动获取属性名
        """
        self.attrname = name
    
    def __get__(self, instance, owner):
        """
        获取属性值
        - 第一次：计算并缓存
        - 后续：返回缓存
        """
        if instance is None:
            return self
        
        # 检查是否已缓存
        if self.attrname is None:
            raise TypeError(
                "Cannot use cached_property instance without "
                "calling __set_name__ on it.")
        
        # 尝试从实例字典获取缓存值
        cache = instance.__dict__
        try:
            return cache[self.attrname]
        except KeyError:
            pass
        
        # 首次访问：计算并缓存
        print(f"计算 {self.attrname}...")
        value = self.func(instance)
        cache[self.attrname] = value
        return value


class DataAnalyzer:
    """
    数据分析器
    - 使用cached_property缓存计算结果
    """
    
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def sum(self):
        """总和（缓存）"""
        return sum(self.data)
    
    @cached_property
    def mean(self):
        """平均值（缓存）"""
        return self.sum / len(self.data)
    
    @cached_property
    def variance(self):
        """方差（缓存）"""
        mean = self.mean
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)
    
    @cached_property  
    def std_dev(self):
        """标准差（缓存）"""
        return self.variance ** 0.5


# 测试
if __name__ == "__main__":
    data = list(range(1, 101))  # 1到100
    analyzer = DataAnalyzer(data)
    
    print("=== 首次访问（会计算） ===")
    print(f"总和：{analyzer.sum}")
    print(f"平均值：{analyzer.mean}")
    print(f"方差：{analyzer.variance}")
    print(f"标准差：{analyzer.std_dev}")
    
    print("\n=== 再次访问（使用缓存） ===")
    print(f"总和：{analyzer.sum}")
    print(f"平均值：{analyzer.mean}")
    print(f"方差：{analyzer.variance}")
    print(f"标准差：{analyzer.std_dev}")
    
    print("\n=== 验证缓存 ===")
    print(f"实例字典：{list(analyzer.__dict__.keys())}")
