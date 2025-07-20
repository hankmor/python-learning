def use_in_if():
    # 传统写法
    user_input = input("Enter something: ")
    if len(user_input) > 5:
        print(f"Input is long, length is: {len(user_input)}")

    # 使用海象运算符可以简化代码
    if (n := len(input("Enter something: "))) > 5:
        print(f"Input is long, length is {n}")


def use_in_while():
    # 普通方式逐行读取
    f = open("./walrus-operator.py", "r")
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

    # 使用海象运算符简化代码
    while line := f.readline():
        print(line.strip())


def list_comprehension():
    # 普通方式
    numbers = [1, 2, 3, 4, 5]
    squares = []
    for n in numbers:
        y = n * n
        if y > 10:
            squares.append(n * n)
    print(squares)

    # 使用海象运算符
    squares = [y for x in numbers if (y := x * x) > 10]
    print(squares)


def pattern_matching():
    import re

    text = "Hello, my email is example@email.com"
    if match := re.search(r"\w+@\w+\.\w+", text):
        print(f"Found email: {match.group()}")


# use_in_if()
# use_in_while()
# list_comprehension()
pattern_matching()
