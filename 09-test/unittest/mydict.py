"""
编写一个 MyDict 类，功能与 dict 一样，支持通过属性来赋值和取值
"""


# 默认的 dict 无法通过 dict.key 的方式来获取 key 对应的值
# x = {"a": 1, "b": 2}
# print(x["a"])
# print(x.a)


class MyDict(dict):
    """ 自定义一个 dict，从 dict 继承，但是支持通过 dict.key 的方式来设置值和取值 """

    def __init__(self, **kw):
        super().__init__(**kw)

    def __setattr__(self, key, value):
        """ 设置值的方法 """
        self[key] = value

    def __getattr__(self, item):
        """ 取值方法，如果 key 不存在则抛出异常 """
        try:
            return self[item]
        except KeyError as e:
            # 不存在属性则抛出 AttributeError 异常
            raise AttributeError("no key '%s' found" % item)
