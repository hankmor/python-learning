"""
urllib 提供了操作 url 的一系列功能
https://docs.python.org/3.9/library/urllib.request.html
"""
import json
from urllib import request, parse

# ================================================
# get 请求
# ================================================

# 请求网站，传入 url 或者 Request 对象，返回 http.client.HTTPResponse 对象
# with request.urlopen('https://hankmo.com') as f:
#     print(type(f))
#     data = f.read()  # 读取返回的全部内容
#     print(f.status, f.reason)  # 打印响应的状态码和信息，200 OK
#     # print(data.decode('utf-8')) # 打印网页的全部内容
#     # 通过属性获取header
#     hm = f.headers
#     print(type(hm))  # <class 'http.client.HTTPMessage'>
#     print(hm.get_content_type())  # text/html
#     # HTTPMessage 实现可迭代的 __getitem__、__setitem__、__iter__
#     for x in hm:
#         print(x, hm[x])
#     # 获取 keys
#     # ['Server', 'Date', 'Content-Type', 'Content-Length', 'Last-Modified', 'Connection', 'ETag', 'Accept-Ranges']
#     print(hm.keys())
#     # ['nginx/1.10.3 (Ubuntu)', 'Sat, 16 Dec 2023 01:27:40 GMT', 'text/html', '104342', 'Tue, 17 Oct 2023 08:29:41 GMT', 'close', '"652e45f5-19796"', 'bytes']
#     print(hm.values())
#     print(type(f.getheaders()))  # <class 'list'>
#     for x in f.getheaders():
#         print(x[0], ":", x[1])
#
# # 添加请求头
# req = request.Request('https://hankmo.com')
# req.add_header('User-Agent',
#                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) '
#                'Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))

# ================================================
# post 请求
# ================================================

# 模拟微博登陆
print('> Login to weibo.cn...')
print('获取验证码图片: ')
with request.urlopen('https://passport.weibo.cn/captcha/image') as f:
    s = f.read().decode('utf-8')
    d = json.loads(s)
    img = d['data']['image']
    print(img)
email = input('Email: ')
passwd = input('Password: ')
code = input('Code: ')
# 把参数 encode 为 key=value 的形式
login_data = parse.urlencode([
    ('username', email),  # 用户名
    ('password', passwd),  # 密码
    ('pincode', code),  # 验证码
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('res', 'wel'),
    ('wm', '3349'),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

# 构建一个 Request 对象
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    r = f.read().decode('utf-8')
    print(r)
    d = json.loads(r)
    print("msg: ", d['msg'])
# {"retcode":50011006,"msg":"\u9a8c\u8bc1\u7801\u9519\u8bef\uff0c\u8bf7\u91cd\u65b0\u8f93\u5165","data":{"errline":15}}
# msg:  验证码错误，请重新输入

# 使用 Proxy 请求网站
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass
