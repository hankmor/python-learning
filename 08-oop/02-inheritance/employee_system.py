class Employee:
    """员工基类"""
    
    # 类属性：员工ID计数器
    _id_counter = 1000
    
    def __init__(self, name, department):
        """初始化员工"""
        self.name = name
        self.department = department
        self.employee_id = Employee._id_counter
        Employee._id_counter += 1
    
    def get_info(self):
        """获取员工信息"""
        return f"ID: {self.employee_id}, Name: {self.name}, Dept: {self.department}"
    
    def calculate_salary(self):
        """计算工资（子类需要实现）"""
        raise NotImplementedError("子类必须实现calculate_salary方法")

class FullTimeEmployee(Employee):
    """全职员工"""
    
    def __init__(self, name, department, monthly_salary):
        super().__init__(name, department)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        """计算月薪"""
        return self.monthly_salary
    
    def get_info(self):
        """重写get_info"""
        base_info = super().get_info()
        return f"{base_info}, Type: Full-time, Salary: ¥{self.monthly_salary}"

class PartTimeEmployee(Employee):
    """兼职员工"""
    
    def __init__(self, name, department, hourly_rate):
        super().__init__(name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
    
    def log_hours(self, hours):
        """记录工作小时"""
        self.hours_worked += hours
    
    def calculate_salary(self):
        """计算兼职工资"""
        return self.hourly_rate * self.hours_worked
    
    def get_info(self):
        """重写get_info"""
        base_info = super().get_info()
        salary = self.calculate_salary()
        return f"{base_info}, Type: Part-time, Earned: ¥{salary}"

if __name__ == "__main__":
    # 使用
    full_time = FullTimeEmployee("张三", "技术部", 10000)
    part_time = PartTimeEmployee("李四", "市场部", 100)
    part_time.log_hours(40)

    employees = [full_time, part_time]
    for emp in employees:
        print(emp.get_info())
        print(f"  本月工资：¥{emp.calculate_salary()}\n")
