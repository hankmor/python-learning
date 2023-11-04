# 可以给函数定义别名
print(abs(-10)) # 10
abs1 = abs # 相当于给abs函数定义了一个别名abs1，此时abs和abs1的功能完全相同
print(abs(-10)) # 10
print(abs1(-10)) # 10