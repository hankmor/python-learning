# 循环中的 else: 如果循环执行完成没有break，则继续执行else，如果break则else不再执行
for i in range(2, 10):
    if i < 2 or i > 10:
        break  # 循环break后，不会执行else
else:  # 属于for循环的else，而不是if语句
    print("i >= 2 and i < 10")

print("===========")

# 判断是否是素数：只能被1和其自身整除的数
for n in range(2, 10):
    # print("n = ", n)
    for x in range(2, n):  # 范围为2到 n - 1的数中，如果n能被整除，则不是素数
        # print("x = ", x)
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break  # 跳出循环，不执行 else
    else:  # 否则，是素数
        print(n, 'is a prime number')

print("===========")

# continue语句与java类似
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
