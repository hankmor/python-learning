"""
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
        case _:
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