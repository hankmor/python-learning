"""
内置 collections 模块示例

collections是Python内建的一个集合模块，提供了许多有用的集合类。
"""
import argparse
import collections
import os

# ================================================
# namedtuple
# ================================================

# tuple 虽然表示不变集合，但是无法准确表达含义，如果又不想定义一个类，此时就可以直接使用方便的 namedtuple 函数来动态创建一个类。
#
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

# 创建一个 Point 类型，类型名称为 Point, 具有两个属性 x, y
Point = collections.namedtuple(typename='Point', field_names=['x', 'y'])
# 创建 Point 的实例
p = Point(1, 2)
print(type(p))  # <class '__main__.Point'>
print(isinstance(p, Point))  # True
print(isinstance(p, tuple))  # True
# 可以直接通过属性名称来访问
print(p.x, p.y)  # 1 2

# ================================================
# 双端队列 deque，支持双向插入、删除数据
# ================================================

# 创建 dequeue，传入可迭代数据，可以通过 maxlen 指定最大长度
d = collections.deque(['a', 'b'], maxlen=5)
# 尾部插入数据
d.append('c')
d.append('d')
# 从头部插入数据
d.appendleft('z')
d.appendleft('y')
d.appendleft('x')
# 可以看到里边只有5跳数据
print(d)  # deque(['x', 'y', 'z', 'a', 'b'], maxlen=5)
x = d.pop()  # 删除尾部的 b
print(x)  # b
x = d.popleft()  # 删除头部的 x
print(x)  # x
print(d)  # deque(['y', 'z', 'a'], maxlen=5)

# ================================================
# defaultdict
# 默认的 dict 如果 key 不存在时访问就会抛出 KeyError,
# 如果希望返回一个默认值而不是抛出异常，则可以使用 defaultdict
# ================================================

dc = collections.defaultdict(lambda: None)
dc['a'] = 1
dc['b'] = 2
print(dc)  # defaultdict(<function <lambda> at 0x10bf40a60>, {'a': 1, 'b': 2})
print(dc['a'])  # 1
print(dc['b'])  # 2
print(dc['c'])  # None

# ================================================
# OrderedDict
# 解决默认的 dict 没有顺序的问题
# ================================================

d = dict({'a': 1, 'b': 2, 'c': 3})
print(d)  # dict的Key是无序的
# OrderedDict的Key是有序的
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# ================================================
# ChainMap 可以把一组dict串起来并组成一个逻辑上的dict。
# ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
#
# 一个使用场景就是依次查找设置的参数，如命令行、环境变量、默认参数等
# ================================================

# 命令行参数解析
parser = argparse.ArgumentParser()
# 解析必须的两个参数
parser.add_argument('-u', '--user', help='enter user', required=False)
parser.add_argument('-p', '--password', help='enter password', required=False)
namespace = parser.parse_args()
print(namespace)  # Namespace(user='root', password='123')
# 组装成为 dict
cmd_line_args = {k: v for k, v in vars(namespace).items() if v}
print(type(cmd_line_args))  # <class 'dict'>

# 组合成ChainMap, 优先级 命令行 > 环境变量 > 默认参数
combined = collections.ChainMap(cmd_line_args, os.environ, {"user": "root", "password": "<PASSWORD>"})

# 获取参数，ChainMap 会按照优先级依次查找
print('user=%s' % combined['user'])  #
print('password=%s' % combined['password'])

# 不设置参数时打印：
# user=root
# password=<PASSWORD>
# 通过控制台传递参数： python3 collections_sample.py -uroot -p123
# user=root
# password=123


# ================================================
# Counter
# 计数器
# ================================================

ct = collections.Counter()
# 向 counter 写入数据，会自动统计字符出现的次数
for s in 'hello world':
    ct[s] = ct[s] + 1
print(ct)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(ct['l'])  # 3
# 更新计数器的内容，但是统计的次数会继续累加
ct.update('python')
print(ct)  # Counter({'l': 3, 'o': 3, 'h': 2, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, 'p': 1, 'y': 1, 't': 1, 'n': 1})
# 清除所有统计数据
ct.clear()
print(ct)
