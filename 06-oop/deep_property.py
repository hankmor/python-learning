"""
使用 python 的 property 装饰器定义方法属性
"""


# javaer 都知道，类属性需要定义 getter 和 setter 才能对属性进行取值和设值，python 面向对象编程也可以这样编码
class Student:
    def get_score(self):
        return self._score

    # 限制 score 的合法范围
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("invalid score")
        self._score = score


# 调用实例上的 getter 和 setter 方法
s = Student()
s.set_score(60)
print(s.get_score())  # 60
# s.set_score(200) # ValueError: invalid score


# 这样其实与 java 差不多了，python 其实有更简单的方式，那就是使用 @property 来定义属性方法
class Student1:
    # 装饰器，为 getter 方法 score 增加 score 属性，同时自己还创造 @score.setter 装饰器，
    # 可以用在 setter 上
    @property
    def score(self):
        return self._score

    # 由上边的 @property 创建的装饰器，用来给 score 赋值
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError("invalid score")
        self._score = score

    # 只加上 @property ，那么该属性就是只读的，无法设置值
    @property
    def readonly_field(self):
        return "readonly"


# 现在，score 就可以当成属性来操作了，而不是调用方法
s1 = Student1()
# setter
s1.score = 60
# getter
print(s1.score)  # 60
# s1.score = 200  # ValueError: invalid score
# 无法为只读属性赋值
# s1.readonly_field = "haha" # AttributeError: property 'readonly_field' of 'Student1' object has no setter
print(s1.readonly_field)  # readonly
