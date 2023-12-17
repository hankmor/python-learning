"""
chardet 库用来检测编码
"""
import chardet

# 检测给定字节的编码
r = chardet.detect(b'Hello, world!')
# 检测出的编码结果对象，confidence为概率，1.0表示100%
print(r)  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

# 中文编码为 utf-8
r = chardet.detect('你好，世界！'.encode('utf-8'))
print(r)  # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# 中文编码为 unicode
print('你好，世界！'.encode('unicode-escape'))  # b'\\u4f60\\u597d\\uff0c\\u4e16\\u754c\\uff01'
r = chardet.detect('你好，世界！'.encode('unicode-escape'))
print(r)  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

print('你好，世界！'.encode('gbk'))  # b'\xc4\xe3\xba\xc3\xa3\xac\xca\xc0\xbd\xe7\xa3\xa1'
r = chardet.detect('你好，世界！'.encode('gbk'))
print(r)  # {'encoding': 'TIS-620', 'confidence': 0.20239943177034195, 'language': 'Thai'}

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))  # {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))  # {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
