"""
python 内置的 base64 编解码
"""
import base64

s = base64.b64encode(b'binary\x00string')
print(s)  # b'YmluYXJ5AHN0cmluZw=='
d = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(d)  # b'binary\x00string'

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

s = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s)  # b'abcd++//'
s = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s)  # b'abcd--__'
d = base64.urlsafe_b64decode('abcd--__')
print(d)  # b'i\xb7\x1d\xfb\xef\xff'


# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
# 'abcd' -> 'YWJjZA=='
# 自动去掉=:
# 'abcd' -> 'YWJjZA'
# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

def safe_base64_decode(s):
    # 不足4的倍数，用 = 补齐，缺几个补几个
    s += '===='[len(s) % 4:]
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
