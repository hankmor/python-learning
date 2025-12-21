class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner, balance=0):
        """初始化账户"""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """
        存款（实例方法）
        - 第一个参数是self
        - 可以访问和修改实例属性
        """
        if amount > 0:
            self.balance += amount
            return f"存入{amount}元，余额{self.balance}元"
        return "金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if amount > self.balance:
            return "余额不足"
        self.balance -= amount
        return f"取出{amount}元，余额{self.balance}元"
    
    def get_balance(self):
        """查询余额"""
        return f"{self.owner}的余额：{self.balance}元"

if __name__ == "__main__":
    # 使用
    account = BankAccount("张三", 1000)
    print(account.deposit(500))    # 存入500元，余额1500元
    print(account.withdraw(200))   # 取出200元，余额1300元
    print(account.get_balance())   # 张三的余额：1300元
