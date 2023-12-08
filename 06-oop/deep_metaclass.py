"""
元类
"""


class Hello():
    def hello(self, name="world"):
        print("Hello, {}!".format(name))


h = Hello()
h.hello()  # Hello, world!
# 实例的类型是 Hello class
print(type(h))  # <class '__main__.Hello'>
# class 类型其实是 type
print(type(Hello))  # <class 'type'>


# ================================================
# 动态创建 class
# type 不仅仅可以查看类信息，还可以动态创建类
# ================================================

# 定义一个方法
def hello(self, name="world"):
    print(f"Hello, {name}!")


# 开始动态创建 Hello class
# type 创建类时包含三个参数，第一个为类名称，第二个未继承 tuple，第三个未绑定的属性和方法 dict
# 返回创建的 class
# 通过下边的方法动态创建了一个名为 DynamicHello 的 class，继承自 object, 具有 hello 方法
DynamicHello = type("DynamicHello", (object,), {"hello": hello})
dh = DynamicHello()
print(type(DynamicHello))  # <class 'type'>
print(type(dh))  # <class '__main__.DynamicHello'>
# 调用其方法
dh.hello()  # Hello, world!


# ================================================
# 元类, metaclass，定义它可以动态创建class
# ================================================

# 除了通过 type 方法动态的创建 class， 还可以使用 metaclass 来创建 class
# class 可以看作是 metaclass 的实例，或者说 metaclass 是 class 的模板
# 这一点与 java 的反射机制有点类似

# 定义 metaclass，相当于定义了类模板，它必须继承自 type
class MyListMetaclass(type):

    # 创建 class 是通过 __new__ 来创建，支持三个参数：
    # 1、cls: 当前创建的类对象
    # 2、name: 创建的类名称
    # 3、bases: 继承的类的集合
    # 4、attrs: 类的方法集合
    def __new__(cls, name, bases, attrs):
        # 给创建的类增加一个名称为 add 的方法, 该方法接收一个 value 参数,
        # self 是下边使用该 metaclass 的具体 class，这里必须是一个 list，所以直接调用了其 append 方法
        attrs["add"] = lambda self, value: self.append(value)
        # 返回新建的 class
        return type.__new__(cls, name, bases, attrs)


# 有了模板，现在我们可以根据模板来定义 class
# 1、class 继承自 list
# 2、指定 metaclass 为上边定义的模板，这样就告诉 python 解释器，通过该 metaclass 来创建 MyList
class MyList(list, metaclass=MyListMetaclass):
    pass


# 创建一个自定义的 list，它是一个 list，并且具有自定义的 add 方法
ml = MyList()
ml.append(1)
ml.add(2)
print(ml)  # [1, 2]
