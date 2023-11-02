count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1

print("Good bye!")

# continue 用于跳过该次循环，break 则是用于退出循环
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

# while、for都可以支持else，当循环退出时会执行else

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")


# 求2到100之间的素数：只能被1和他自身整除的数
i = 2
while (i < 100):
    j = 2
    while (j <= (i/j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i/j):
        print(i, " 是素数")
    i = i + 1

print("Good bye!")
