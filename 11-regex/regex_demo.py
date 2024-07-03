"""
python 中的正则表达式

python 提供了 re 模块来操作正则表达式，并且支持 r'正则' 字符串格式来消除转义
"""

import re

# ================================================
# 正则表达式基本写法
# ================================================

# 字符串前边增加 r, 则字符串的正则可以不用转义，python 会自动处理
# 下边的正则匹配三个数字开头，然后跟 “-”，最后由 3 到 8（注意正则中是包括8） 个数字组成的字符串
m = re.match(r"^\d{3}-\d{3,8}$", "010-12345")
# 如果匹配成功，返回一个 re.Match 对象
print(m)  # <re.Match object; span=(0, 9), match='010-12345'>

m = re.match(r"^\d{3}-\d{3,8}$", "010-123456789")
# 匹配失败，返回一个 None
print(m)  # None

# ================================================
# 使用正则分割字符串
# ================================================

# 如果字符串包含多个空格，默认的字符串分割只能处理一个空格
print("a b c".split(" "))  # ['a', 'b', 'c']
print("a b  c".split(" "))  # ['a', 'b', '', 'c']
# 可以使用正则来处理多个连续空格
print(re.split(r"\s+", "a b  c"))  # ['a', 'b', 'c']
# 如果再加上逗号，表示按照空格或逗号进行分割
print(re.split(r"[\s,]+", "a,b, c  d"))  # ['a', 'b', 'c', 'd']
# 又加上分号
print(re.split(r"[\s,;]+", "a,b;; c  d"))  # ['a', 'b', 'c', 'd']

# ================================================
# 正则的分组功能
# 正则的分组用 () 提取，注意默认第0个组就是匹配的整个字符串
# ================================================

m = re.match(r"^(\d{3})-(\d{3,8})$", "010-12345")
# 查看匹配后的分组
print(m.groups())  # ('010', '12345')
# 使用 m.group(n) 获取某一个组
for x in range(0, len(m.groups()) + 1):
    print(m.group(x))
# 010-12345
# 010
# 12345

# ================================================
# 正则的贪婪和非贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 非贪婪匹配会尽可能匹配少的字符
# ================================================

# 匹配任意数字后边的0（0个或多个），但是由于 (\d+) 采用贪婪匹配，直接把后面的0全部匹配了，结果 (0*) 只能匹配空字符串了。
m = re.match(r"^(\d+)(0*)$", "102300")
print(m.groups())  # ('102300', '')
# 使用 ? 可以使得正则进行非贪婪匹配
m = re.match(r"^(\d+?)(0*)$", "102300")
print(m.groups())  # ('1023', '00')

# ================================================
# 预编译正则
# 多次使用的正则为了性能考虑，都应该进行预编译
# ================================================

# 预编译正则，得到一个 Pattern 对象
re_telephone = re.compile(r"^(\d{3})-(\d{3,8})$")
print(re_telephone.match("010-12345").groups())  # ('010', '12345')
print(re_telephone.match("010-8086").groups())  # ('010', '8086')

# ================================================
# 使用正则匹配合法邮箱地址，提取邮箱名
# ================================================

# 合法的邮箱名称通常包含 字母开头,中间可以为字母、数字、下划线、短横线和点，如 a123@a.com, a-123@a.com, a.123@a.com
# 这里只匹配了主域名，没有考虑子域名的情况
re_email = re.compile(r"^([a-zA-Z]+[.\-_]?\w+)@[a-zA-Z0-9]+\.[a-zA-Z]+$")
s = "someone@gmail.com,1someone@gmail.com,bill.gates@microsoft.com,test_123@abc.com,hello-world@90net.org,hello-world-1@90net.org,Hank_xxx@email09.me"
for email in s.split(","):
    m = re_email.match(email)
    if m:
        print("valid: %s, name: %s" % (email, m.group(1)))
    else:
        print("invalid: %s" % email)
# valid: someone@gmail.com, name: someone
# invalid: 1someone@gmail.com
# valid: bill.gates@microsoft.com, name: bill.gates
# valid: test_123@abc.com, name: test_123
# valid: hello-world@90net.org, name: hello-world
# invalid: hello-world-1@90net.org
# valid: Hank_xxx@email09.me, name: Hank_xxx
