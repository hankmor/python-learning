# 变量

# 变量赋值
a = 10
b = "10"
c = 10.2
d = [a,b,c]
e = (a,b,c)
e = (a,b)

print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
# a=10, b=10, c=10.2, d=[10, '10', 10.2], e=(10, '10')

# 打印变量的类型
print("type a:", type(a)) # type a: <class 'int'>

# 多个变量赋值，三个变量被分配到相同的内存空间上
a = b = c = 1
print(f'a={a}, b={b}, c={c}')
# a=1, b=1, c=1
del a,b,c # 可以使用 del 删除变量
# print(f'a={a}, b={b}, c={c}') # NameError: name 'a' is not defined