def func(x):
    if x < 0:
        print('x is Negative')
    elif x == 0:
        print('x is 0')
    elif x == 1:
        print('x is Single')
    else:
        print('x is More')


func(-1)
func(0)
func(1)
func(100)

# python中没有switch

var = 100
if var == 100:
    print("变量 var 的值为100")
print("Good bye!")
