# ==========
# 基本数据类型：int，str，float，bool
# ==========

a = 1
b = 1.0
c = "1"
d = True
e = False
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

# 数据类型转换
# print(a + c) # 异常，数据类型不兼容
print(str(a) + c)  # 转换类型
print(a + int(c))  # str转int

# ==========
# 类型运算
# ==========

# bool True可以看成1，False可以看成0，然后进行运算
print(a + d)  # 结果为2
print(a + e)  # 结果为1

aInt = 10
bInt = 3
ret = aInt / bInt
print(ret, type(ret))  # 除法运算，结果为float
# 整除，需要使用 //
ret = aInt // bInt
print(ret, type(ret))  # 这样结果为int
# 取模
ret = aInt % bInt
print(ret)

# 负数运算
cInt = -3
print(aInt / cInt)  # -3.3333333333333335
print(aInt % cInt)  # -2
print(cInt / -2)  # 1.5
print(aInt * bInt)  # 30
# python中的乘方运算，使用 **
print(aInt ** 2)  # 100