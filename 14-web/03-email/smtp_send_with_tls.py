"""
使用 smtp 发送邮件，使用 tls 加密邮件避免被拦截
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    """
    从固定的邮件信息格式中解析出需要的地址等信息，比如 name <addr@example.com>, name 为名称，后为空格，再跟真实邮箱地址
    """
    # 解析出 name 和 邮箱
    name, addr = parseaddr(s)
    # name 可能有中文，需要通过 Header 来进行编码
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 构建 MIMEText，第二个参数 'plain' 表示纯文本，最终的 MIME 就是 text/plain，第三个参数为文本编码
msg = MIMEText('this is a plain text email send by python3', 'plain', 'utf-8')

# 发送人地址
from_addr = input('From: ')
# 发件人需要邮箱密码才能发送
pwd = input('Password: ')
# 收件人地址
to_addr = input('To: ')
# 设置 From、To、Subject 等信息，注意，邮件中这些信息通过 name <addr@example.com> 来设置，中间有一个空格，需要自己构建
# 如果有中文，还需要通过 Header 对象进行编码，避免乱码
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)  # 多个收件人以,分隔即可
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
# 发件人的服务器 smtp 地址
smtp_server = input('SMTP Server: ')
# 创建 SMTP server
srv = smtplib.SMTP(smtp_server, 25)
# 开启 tls 加密
srv.starttls()
# 打印详细信息
srv.set_debuglevel(1)
# 登陆服务端
srv.login(from_addr, pwd)
# 发送邮件
srv.sendmail(from_addr, to_addr, msg.as_string())
# 退出登录，关闭 SMTP session
srv.quit()
# 如果发送 成功，会打印2xx的状态码，如： reply: retcode (221); Msg: b'Bye'
