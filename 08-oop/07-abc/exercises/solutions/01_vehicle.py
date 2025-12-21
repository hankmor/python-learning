"""
练习1：Vehicle抽象基类
定义交通工具的基本接口
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    交通工具抽象基类
    - 定义所有交通工具的通用接口
    """
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False
    
    @abstractmethod
    def start(self):
        """启动（抽象方法）"""
        pass
    
    @abstractmethod
    def stop(self):
        """停止（抽象方法）"""
        pass
    
    @abstractmethod
    def drive(self, distance):
        """行驶指定距离（抽象方法）"""
        pass
    
    def get_info(self):
        """获取车辆信息（具体方法）"""
        status = "运行中" if self.is_running else "停止"
        return f"{self.brand} {self.model} ({status})"


class Car(Vehicle):
    """汽车类"""
    
    def __init__(self, brand, model, fuel_type="汽油"):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.fuel_level = 100  # 油量百分比
    
    def start(self):
        """启动汽车"""
        if self.fuel_level > 0:
            self.is_running = True
            return f"{self.brand} {self.model}发动机启动"
        return "油箱空了，无法启动"
    
    def stop(self):
        """停止汽车"""
        self.is_running = False
        return f"{self.brand} {self.model}发动机关闭"
    
    def drive(self, distance):
        """驾驶汽车"""
        if not self.is_running:
            return "请先启动车辆"
        
        fuel_needed = distance * 0.1  # 每公里消耗0.1%油量
        if fuel_needed > self.fuel_level:
            return f"油量不足，无法行驶{distance}公里"
        
        self.fuel_level -= fuel_needed
        return f"行驶{distance}公里，剩余油量{self.fuel_level:.1f}%"
    
    def refuel(self, amount):
        """加油"""
        self.fuel_level = min(100, self.fuel_level + amount)
        return f"加油后油量：{self.fuel_level:.1f}%"


class Bicycle(Vehicle):
    """自行车类"""
    
    def __init__(self, brand, model, gear_count=1):
        super().__init__(brand, model)
        self.gear_count = gear_count
        self.current_gear = 1
    
    def start(self):
        """开始骑行"""
        self.is_running = True
        return f"开始骑{self.brand} {self.model}"
    
    def stop(self):
        """停止骑行"""
        self.is_running = False
        return f"停止骑行{self.brand} {self.model}"
    
    def drive(self, distance):
        """骑行"""
        if not self.is_running:
            return "请先开始骑行"
        return f"骑行{distance}公里（档位：{self.current_gear}/{self.gear_count}）"
    
    def shift_gear(self, gear):
        """换挡"""
        if 1 <= gear <= self.gear_count:
            self.current_gear = gear
            return f"切换到{gear}挡"
        return f"无效的挡位（有效范围：1-{self.gear_count}）"


# 测试
if __name__ == "__main__":
    print("=== 汽车测试 ===")
    car = Car("Toyota", "Camry")
    print(car.get_info())
    print(car.start())
    print(car.drive(100))
    print(car.drive(900))
    print(car.drive(100))  # 油量不足
    print(car.refuel(50))
    print(car.drive(100))
    print(car.stop())
    
    print("\n=== 自行车测试 ===")
    bike = Bicycle("Giant", "TCR", gear_count=21)
    print(bike.get_info())
    print(bike.start())
    print(bike.shift_gear(5))
    print(bike.drive(10))
    print(bike.shift_gear(15))
    print(bike.drive(20))
    print(bike.stop())
