"""
python中没有switch，但可以使用match。
match可以将一个值与多个值进行比较，类似java的Switch语句，但是case匹配不再执行其他case语句，不要break
"""
import sys


def http_status(status):
    match status:
        case 200:
            print('Ok')
        case 400:
            print('Bad Request')
        case 404:
            print('Not Found')
        case 500:
            print('Server Error')
        case _:  # 其他任何情况
            print('Unkown Error')


def http_status2(status):
    match status:
        case 200:
            print('Ok')
        case 400 | 404:  # 可以使用 | 组合多个值
            print('Client Error')
        case 500:
            print('Server Error')
        case _:
            print('Unkown Error')


http_status(200)
http_status(400)
http_status(404)
http_status(500)
http_status(401)

http_status2(400)
http_status2(500)


# 匹配tuple
def check_point(point):
    match point:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f'Y={y}')
        case (x, 0):
            print(f'X={x}')
        case (x, y):
            print(f'X={x}, Y={y}')
        case _:
            raise ValueError('Not a point')


check_point((0, 0))
check_point((0, 45))
check_point((45, 0))
check_point((45, 45))
check_point((45, 45))
try:
    check_point(20)
except ValueError as v:
    print('Error: ', v)
    print(sys.exc_info())

# 复杂匹配
age = 15
match age:
    case x if x < 10:  # 匹配满足条件
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

# 匹配列表

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']
match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

