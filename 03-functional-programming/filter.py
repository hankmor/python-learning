"""
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list。
"""


def is_odd(n):
    return n % 2 == 1


# 过滤偶数，只留下奇数
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 判断字符s是否是空字符串
def not_empty(s):
    return s and s.strip()


# ['A', 'B', 'C']
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


"""
筛选素数（也叫质数，是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数）

首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, \, 5, \, 7, \, 9, \, 11, \, 13, \, 15, \, 17, \, 19, \, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 7, 11, 13, 17, 19, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 11, 13, 17, 19, ...
不断筛下去，就可以得到所有的素数。
"""


# 一般写法
def filter_prime_normal(n):
    l = []
    for x in range(2, n+1):
        is_prime = True
        # 从2开始到x-1，均不能整除为素数
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            l.append(x)
    return l


print(filter_prime_normal(20))  # [2, 3, 5, 7, 11, 13, 17, 19]


# 利用filter函数和list generator的高级写法

# 一个生成奇数的生成器，这是一个无限序列
def odd_gen():
    n = 1
    while True:
        n += 2
        yield n


# 返回一个匿名函数，该函数接受一个参数x，返回 x 能否被 n 整除
def not_divisable(n):
    return lambda x: x % n > 0
    # 上边的lambda，等同于下边的代码
    # def div_fn(x):
        # return x % n > 0
    # return div_fn

# 返回一个生成素数的生成器，这是一个无限序列
def filter_prime_master():
    yield 2  # 第一个素数直接返回2
    g = odd_gen()  # 生成一个基数序列，因为除了2之外的素数都是基数
    while True:
        n = next(g)  # 下一个基数
        yield n  # 第一个是素数3，取下一个素数则执行下一行
        # 正确的写法：not_divisable返回的函数中，每次过滤时参数n不变，将g序列的元素依次与n求模，判断其是否能被n整除。返回一个新序列
        # print("n =", n)
        g = filter(not_divisable(n), g)
        # 错误的写法，注意两者的区别，函数传入的参数值不同，打印出来 n 和 x 的值就可以看出差别
        # g = filter(lambda x: x % n > 0, g)
        # 上边错误的写法代码等同于这样
        # g = filter(err_code, g)


def err_code(x):
    print("x =", x)
    return lambda n: x % n > 0


# 求1000以内所有的素数，可以通过filter_prime_master()无限序列打印所有的素数
for i in filter_prime_master():
    if i > 20:  # 无限序列，需要给出退出条件
        break
    print(i)


g = (a for a in range(1, 10))


def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, g)))
print(lambda x: x % n > 0)
print(is_even)
