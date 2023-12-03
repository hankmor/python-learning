"类属性和实例属性"


class User():
    # 定义了类属性，所有的实例都可以访问它
    name = "user"
    pass


# 实例都可以访问类属性
zs = User()
print(zs.name)
ls = User()  # user
print(ls.name)  # user
# 如果修改类属性，相当于给实例赋值了一个 name 属性，访问时会优先于同名的类属性
zs.name = 'zhangsan'
print(zs.name)  # zhangsan
# 类属性不会被修改
print(ls.name)  # lisi
