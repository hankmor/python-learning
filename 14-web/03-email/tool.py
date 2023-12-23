import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr


def format_addr(s):
    """
    从固定的邮件信息格式中解析出需要的地址等信息，比如 name <addr@example.com>, name 为名称，后为空格，再跟真实邮箱地址
    """
    # 解析出 name 和 邮箱
    name, addr = parseaddr(s)
    # name 可能有中文，需要通过 Header 来进行编码
    return formataddr((Header(name, 'utf-8').encode(), addr))


def add_attachment(msg, type, fp, cid):
    if not os.path.isfile(fp):
        raise ValueError(f'not a file: {fp}')
    filename = os.path.basename(fp)
    with open(fp, 'rb') as f:
        # 设置附件的MIME和文件名
        mime = MIMEBase('image', type, filename=filename)
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename=filename)  # 这个名字为附件的名称
        mime.add_header('Content-ID', f'<{cid}>')  # 给附件编号，在 html 可以引用附件
        mime.add_header('X-Attachment-Id', str(cid))
        # 把附件的内容读进来
        mime.set_payload(f.read(), 'utf-8')
        # 用Base64编码
        encoders.encode_base64(mime)
        # 添加附件对象到MIMEMultipart
        msg.attach(mime)


def input_and_send_mail(msg, subject, from_name='', to_name=''):
    # 发送人地址
    from_addr = input('From: ')
    # 发件人需要邮箱密码才能发送
    pwd = input('Password: ')
    # 收件人地址
    to_addr = input('To: ')
    # 设置 From、To、Subject 等信息，注意，邮件中这些信息通过 name <addr@example.com> 来设置，中间有一个空格，需要自己构建
    # 如果有中文，还需要通过 Header 对象进行编码，避免乱码
    msg['From'] = format_addr(f'{from_name} <%s>' % from_addr)
    msg['To'] = format_addr(f'{to_name} <%s>' % to_addr)  # 多个收件人以,分隔即可
    msg['Subject'] = Header(subject, 'utf-8').encode()
    # 发件人的服务器 smtp 地址
    smtp_server = input('SMTP Server: ')
    # 创建 SMTP server
    srv = smtplib.SMTP(smtp_server, 25)
    # 打印详细信息
    srv.set_debuglevel(1)
    # 登陆服务端
    srv.login(from_addr, pwd)
    # 发送邮件
    srv.sendmail(from_addr, to_addr, msg.as_string())
    # 退出登录，关闭 SMTP session
    srv.quit()
    # 如果发送 成功，会打印2xx的状态码，如： reply: retcode (221); Msg: b'Bye'
