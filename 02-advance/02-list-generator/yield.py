# 定义斐波那契数列函数
def fib(max):
    n = 0
    a, b = 0, 1
    while (n < max):
        print(b)  # 打印
        a, b = b, a+b
        n = n + 1
    return "done"


fib(5)

print("====")


# yield关键字表明该函数不再是一个普通函数，而是一个generator函数，它将返回一个generator
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print("====")


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


o = odd()
print(next(o))  # step 1, 1
print(next(o))  # step 2, 2
print(next(o))  # step 3, 3
# next(o)  # StopIteration

print("====")

# 调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
# 每次调用odd都会生成一个新的generator，每次调用遇到yield才会返回，所以都会返回1
print(next(odd()))  # 1, step 1
print(next(odd()))  # 1, step 1
print(next(odd()))  # 1, step 1

print("====")


# 改造斐波那契函数为generator
def fib_g(max):
    n = 0
    a, b = 0, 1
    while n < max:
        yield b  # 生成器调用next才会返回
        a, b = b, a+b
        n = n + 1
    return 'done'


f = fib_g(6)
print(f)  # <generator object fib_g at 0x1071dc660>
print(next(f))  # 1
print(next(f))  # 1
print(next(f))  # 3
for v in f:
    print(v)
# 5
# 8

# 上述代码虽然执行正确，但是不能获取函数的返回值，因为 next 执行后 yield 返回，最终无法到达 return 语句
# 除非 next 抛出 StopIteration 并被捕获
f = fib_g(10)
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print("f's return value: ", e.value)
        break
# 1
# 1
# 2
# 3
# 5
# 8
# f's return value:  done


print("====")


# 使用list 生成器打印杨辉三角
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
def yanghui_triangle(max):
    n, a, b = 0, [1], []
    while n < max:
        yield a
        for v in range(0, len(a)+1):  # b 中的元素数量比当前 a 中的多一个
            if v == 0 or v == len(a):
                b.append(a[0])  # 第一个和最后一个位置的元素取 a 的第一个元素
            else:
                # b 中当前位置元素 = a 中当前位置前一个元素 + a 中当前位置的元素
                b.append(a[v-1] + a[v])
        a, b = b, []  # b 需要重置
        n = n + 1


f = yanghui_triangle(10)
for x in f:
    print(x)
