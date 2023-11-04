"""
基础参数定义
"""


# 返回参数x的平方
def power(x):
    return x*x


print(power(3))  # 9


# 返回参数x的n次方
def power(x, n):
    r = 1  # 每次乘后的结果
    while n > 0:
        r = r * x
        n = n - 1
    return r


print(power(3, 2))  # 9
print(power(3, 3))  # 27

"""
默认参数
"""


# 使用默认参数
# 默认让power始终计算平方，也就是可以不传递n
def power(x, n=2):
    r = 1
    while n > 0:
        r = r * x
        n = n - 1
    return r


print(power(4))  # 16，不传n默认就是2
print(power(4, 3))  # 64


# 使用默认参数的坑
# 默认参数为一个list
def list_add(l=[]):
    l.append('end')
    return l


# 看似正常
print(list_add([1, 2, 3]))  # [1, 2, 3, 'end']
print(list_add([4]))  # [4, 'end']
# 如果使用默认参数就不正常了，看起来每次调用时list都会在上一次的结果中继续增加元素
print(list_add())  # ['end']
print(list_add())  # ['end', 'end']
print(list_add())  # ['end', 'end', 'end']


# 原因：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 要改进这个问题，可以使用不可变类型None
def list_add(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


# 现在多次调用都是相同的结果
print(list_add())  # ['end']
print(list_add())  # ['end']
print(list_add())  # ['end']
