"""
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传
入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
"""


# 定义一个 kw 参数表示关键字参数(前边有两个 "**")，该函数除了保证能够接受name、age两个参数外，
# 还可以接受调用者传入的其他更多参数，这样就 # 扩展了函数的能力
def person(name, age, **kw):
    # print(type(kw)) # <class 'dict'>
    print(f'name = {name}, age = {age}, other = {kw}')


# 然后，就可以通过 [关键字=参数] 的形式传递，这将是一个dict
# name = 章三, age = 20, other = ({'hobby': 'program', 'dept': 'dev'},)
person('章三', 20, hobby='program', dept='dev')
# 可以直接传入dict，**d 表示将参数d这个dict作为关键字参数传入person函数
d = {'hobby': 'program', 'dept': 'dev'}
person('章三', 20, **d)


"""
命名关键字参数
用于限制关键字参数的名称，也就是说只接受特定名称的关键字参数，其他的不接收
"""

# 虽然可以通过 in 来判断 kw的dict中是否有对应的key，但是无法限制调用者传递其他更多参数，此时需要用到命名关键字参数


def person(name, age, **kw):
    if 'hobby' in kw:
        print("has hobby:", kw['hobby'])
    if 'dept' in kw:
        print("has dept")


person('章三', 20, hobby='program')  # has hobby: program
person('章三', 20, hobby='program', haha='not used')  # 传递其他无效的参数


# 定义命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, hobby, dept):
    print(f'name={name}, age={age}, hobby={hobby}, dept={dept}')


# 命名关键字参数必须传入参数名称，否则报错
# person('章三', 20, hobby='program') # TypeError: person() missing 1 required keyword-only argument: 'dept'
person('章三', 20, hobby='program', dept='dev')
# 现在，其他无用的参数不能再传入了
# person('章三', 20, hobby='program', dept='dev', haha='unused') # TypeError: person() got an unexpected keyword argument 'haha'


# 但是关键字参数必须传入的话，与普通参数就没什么区别了，如果实现选择行传入呢，可以使用参数默认值
def person(name, age, *, hobby, dept='none'):
    print(f'name={name}, age={age}, hobby={hobby}, dept={dept}')


# 现在，不需要再传入dept了，会使用默认值
person('章三', 20, hobby='program')  # name=章三, age=20, hobby=program, dept=none


# 如果参数列表定义了可变参数，此时不需要 “*” 来定义命名关键字参数了
def person(name, age, *other, hobby, dept='none'):
    print(f'name={name}, age={age}, other={other} hobby={hobby}, dept={dept}')


# name=章三, age=20, other=('haha', 'xixi') hobby=program, dept=none
person('章三', 20, "haha", "xixi", hobby='program')
