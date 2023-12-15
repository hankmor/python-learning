"""
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
"""
import hashlib

s = 'hello, python'

# md5
md5 = hashlib.md5()
md5.update(s.encode('utf-8'))
print(md5.hexdigest())  # fb42758282ecd4646426112d0cbab865

# sha1
sha1 = hashlib.sha1()
sha1.update(s.encode('utf-8'))
print(sha1.hexdigest())  # 0a77b896e768596437abe61459ef20514bdd8c2c

# sha256
print(hashlib.sha256(s.encode('utf-8')).hexdigest())  # 93908e10a1f783fc83ab53b60e1f116a699bb6c83ccd41a862eea8866d784992
