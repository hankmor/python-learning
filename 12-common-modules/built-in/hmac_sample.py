"""
Hmac 算法: Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
"""
import hashlib
import hmac

message = 'Hello, Python'
key = 'mykey'

# 如果自己拼接 salt，方式有多种，比如后边拼接、前边拼接
print(hashlib.md5((message + key).encode('utf-8')).hexdigest())  # 61b948a44fcd924ad1fc9832959c4997

# 使用标准的 Hmac 算法混入 salt，标准化
# MD5
h = hmac.new(key.encode('utf-8'), message.encode('utf-8'), digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())  # 44b8ae19903596bc0ddae07b1ca38ecf

# SHA1
h = hmac.new(key.encode('utf-8'), message.encode('utf-8'), digestmod='SHA1')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())  # 03cf17fb9b0389b8ef139426c7fdb84d4a01ea2b

# SHA256
h = hmac.digest(key.encode('utf-8'), message.encode('utf-8'), digest='SHA256')
print(h.hex())  # d6b0058935f09a22e7a5dc5ee7002365581d13670f9f90cd2dfb1cc933d0a72f
