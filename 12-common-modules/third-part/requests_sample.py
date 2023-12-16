"""
requests 比官方的 urllib 更好用
"""
import requests

r = requests.get('https://hankmo.com')
print(r)  # <Response [200]>
print(r.status_code)  # 200
# print(r.text)
print(r.encoding)  # 自动检测编码，通过 r,encoding 查看当前使用的编码: ISO-8859-1
print(
    r.headers)  # {'Server': 'nginx/1.10.3 (Ubuntu)', 'Date': 'Sat, 16 Dec 2023 14:38:41 GMT', 'Content-Type': 'text/html', 'Last-Modified': 'Tue, 17 Oct 2023 08:29:41 GMT', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'ETag': 'W/"652e45f5-19796"', 'Content-Encoding': 'gzip'}

# 带参数的URL, 传入 params，它是一个 dict
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)  # 实际请求的 url
# 无论是文本还是二进制，都可以使用 content 获得 bytes
print(r.content)  # b''

# 对于特定类型的响应，例如JSON，可以直接获取：
# r = requests.get(
#     'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# 指定 header
r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.status_code)

# post
r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params)  # 内部自动序列化为JSON
print(r.status_code)

# 上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
# upload_files = {'file': open('report.xls', 'rb')} # 读取文件注意使用 rb 模式读取，才能读到真实文件长度
# r = requests.post(url, files=upload_files)

# 可以直接获取  cookie
# r.cookies['ts']
# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)
# 最后，要指定超时，传入以秒为单位的timeout参数：
# r = requests.get(url, timeout=2.5) # 2.5秒后超时
