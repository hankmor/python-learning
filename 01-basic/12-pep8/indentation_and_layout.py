# 缩进与布局 (Indentation and Layout)

# 1. 缩进：使用4个空格
def hello():
    print("Hello")
    if True:
        print("World")

# 2. 续行对齐
# 方法1：对齐左括号
def some_function(a, b, c, d):
    pass

result = some_function(1, 2,
                       3, 4)

# 方法2：悬挂缩进
result = some_function(
    1, 2,
    3, 4
)

# 3. 列表、字典的续行
my_list = [
    1, 2, 3,
    4, 5, 6,
]  # 末尾逗号是好习惯

# 4. 空行规则
# 顶层函数和类之间空2行
def func1():
    pass


def func2():
    pass


class MyClass:
    # 类中的方法之间空1行
    def method1(self):
        pass

    def method2(self):
        pass
