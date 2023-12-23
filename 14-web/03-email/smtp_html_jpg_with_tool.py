"""
封装 tool 模块发送 html 邮件
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tool

# 创建邮件对象
msg = MIMEMultipart()
# 创建邮件正文MIMEText对象
msg.attach(MIMEText('''<html>
<head>发送的是html图片</head>
<body>
send with html images...
<p>
<img src="cid:0" with="400">
<img src="cid:1" with="400">
</p>
</body>
</html>''', 'html', 'utf-8'))

# 添加附件
tool.add_attachment(msg, 'jpg', 'test.jpg', 0)
tool.add_attachment(msg, 'gif', 'avatar.gif', 1)

# 发送邮件，需要输入邮件发送信息
tool.input_and_send_mail(msg, '测试html邮件', from_name='墨寒轩', to_name='python大神')
