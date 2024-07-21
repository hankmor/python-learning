import random


def test_m():
    for i in range(10):
        # 判断json酷不酷
        r = random.random()
        finishHomework = r > 0.5
        if finishHomework:
            print("jason is cool")
        else:
            print("jason is not cool")


def guess_number():
    x = 5
    while True:
        i = int(input("请输入一个数字: "))
        if i > x:
            print("太大了")
        elif i < x:
            print("太小了")
        else:
            print("恭喜，猜对了！")
            break


# test_m()
guess_number()
