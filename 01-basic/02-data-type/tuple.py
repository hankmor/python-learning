# 元组类似于list，但是不能重复赋值，相当于只读列表

tuple = ('string', 1, 1.23)
tinytuple = (123, 'haha')

print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第四个（不包含）的元素
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
# python支持使用乘法来做同样的操作
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)   # 打印组合的元组

# output:
# ('string', 1, 1.23)
# string
# (1, 1.23)
# (1.23,)
# (123, 'haha', 123, 'haha')
# ('string', 1, 1.23, 123, 'haha')

# 元组中的元素无法更改
# tinytuple[0] = 1 # TypeError: 'tuple' object does not support item assignment

# int与tuple的歧义, 元组中只有一个元素时，定义的是int，所以python规定在元素后需要追加一个逗号才能定义为元组
x = (1)
print(type(x)) # <class 'int'>
x = (1,)
print(type(x)) # <class 'tuple'>