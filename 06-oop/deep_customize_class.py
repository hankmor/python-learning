"""
使用 python 特定的方法定制类, 如 __slots__ 属性, __len__() 方法等等
"""

# __str__，定义实例的打印字符串


from typing import Any


class User:
    def __init__(self, name) -> None:
        self.name = name

    # 与 java 的 toString(), golang 的 String() 方法作用相同
    def __str__(self) -> str:
        return "User(name = %s)" % self.name


# 没有定义 __str__ 打印的是对象的地址
u = User("zhangsan")
# print(u) # <__main__.User object at 0x108f40e10>
# 添加 __str__ 后打印该方法返回的字符串
print(u)  # User(name = zhangsan)


# __str__() 与 __repr__() 的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的


# __iter__，定义对象被 for in 语句迭代时的逻辑，循环时下一个值需要从方法 __next__ 中获取


class Fib:
    def __init__(self) -> None:
        self.a, self.b = 0, 1  # 定义两个变量，初始值为 0, 1

    # 迭代时的对象为其自身
    def __iter__(self):
        return self

    # 迭代时如何获取下一个值，直到遇到 StopIteration 错误才停止
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration("max returns 100")
        return self.a  # 返回下一个值


# 创建实例
f = Fib()
# 迭代实例
for n in f:
    print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89


# __getitem__ 可以按序号获取元素


# 虽然 Fib 可以迭代，但是还不能像 list 那样根据元素下标获取其中的元素
# print(f[0]) # TypeError: 'Fib' object is not subscriptable
# __getitem__ 方法就可以实现这个功能

print()


class SubscriptableFib(Fib):
    # 重新计算并获取第 index 个元素
    def __getitem__(self, index):
        a, b = 0, 1
        for x in range(index):
            a, b = b, a + b
        return a


# 现在，可以循环，也可以直接获取第 x 个元素了
sf = SubscriptableFib()
for x in sf:
    print(x)
print()
for x in range(10, 15):
    print(sf[x])


# 55
# 89
# 144
# 233
# 377


# 但是，现在的 SubscriptableFib 仍然不能获取切片，因为我们实现的 __getitem__ 的只是获取了下标，如果要获取切片，需要判断其参数类型
# print(sf[0:5]) # TypeError: 'slice' object cannot be interpreted as an integer


class SliceFib(Fib):
    # 第二个参数可能是 int，按下标获取，也可能是切片，这样就可以获取切片
    def __getitem__(self, x):
        a, b = 0, 1
        if isinstance(x, int):
            for _ in range(x):
                a, b = b, a + b
            return a
        elif isinstance(x, slice):
            start = x.start  # 开始位置
            end = x.stop  # 结束位置
            step = x.step  # 步长
            if start == None:
                start = 0
            if step == None:
                step = 1
            ret = []
            for idx in range(end):
                a, b = b, a + b
                # 处理步长
                # 0, 1, 2, 3, 4
                if idx >= start and idx < end and idx % step == 0:  # 不包含结束位置
                    ret.append(a)
            return ret


sf = SliceFib()
print(sf[:8])  # [1, 1, 2, 3, 5, 8, 13, 21]
print(sf[2:8])  # [2, 3, 5, 8, 13, 21]
print(sf[2:8:2])  # [2, 5, 13]

# 除了 __getitem__外, 还有以下2个同时使用方法
# __setitem__(), 把对象视作list或dict来对集合赋值
# __delitem__(), 用于删除某个元素
# 通过上面方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别


print()


class UintList(object):
    def __init__(self, len) -> None:
        self._data = []
        # map(lambda x: self._data.append(x), range(len))
        for x in range(len):
            self._data.append(x)

    def __getitem__(self, x):
        if isinstance(x, int):
            return self._data[x]
        elif isinstance(x, slice):
            start = x.start
            step = x.step
            end = x.stop
            if start == None:
                start = 0
            if step == None:
                step = 1
            if end == None:
                end = len(self._data)
            return self._data[start:end:step]

    def __setitem__(self, x, y):
        self._data[x] = y

    def __delitem__(self, x):
        self._data.remove(x)

    def __str__(self):
        return self._data.__str__()


ul = UintList(10)
print(ul)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 实现了 __setitem__ 就可以赋值了
ul[0] = 100
print(ul)  # [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 实现了 __delitem__ 可以删除元素
# ul.__delitem__(100)
del ul[100]  # TODO 为什么只能当作 dict 来删除？不能直接调用 remove 或 pop
# ul.remove(100)# AttributeError: 'UintList' object has no attribute 'remove'
# ul.pop(1) # AttributeError: 'UintList' object has no attribute 'pop'
print(ul)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# __getattr__ 方法动态返回不存在的属性


# 如果属性不存在，调用属性会抛出 AttributeError 异常, 此时如果定义了 __getattr__() 则会执行该方法


class Attr:
    def __getattr__(self, attr):
        if attr == "score":
            return 100
        elif attr != "name":
            raise AttributeError("no attr %s" % attr)


a = Attr()
print(a.score)  # 100
# 由于定义了 __getattr__ 方法，所有的属性都会调用，不存在的属性会返回 None
print(a.name)  # None


# 如果不需要返回 None，需要抛出 AttributeError
# print(a.age)  # AttributeError: no attr age


class Chain(object):
    def __init__(self, path=""):
        self._path = path

    # 返回 Chain 实例获得链式调用的能力
    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


s = Chain().status.user.timeline.list
print(s)  # /status/user/timeline/list


# __call__ 方法可以允许直接调用实例，而不是调用实例下的方法


class Call:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return "call invoked"


c = Call()
# 直接调用实例，其实就是将实例当作普通方法来调用，仍然可以传递参数
print(c())  # call invoked
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(c))  # True
print(callable(1))  # False
print(callable([1, 2]))  # False
