#邮件发送模块BY-ZYA
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
def Email_send(content,title):
    from_addr = '@nefu.edu.cn'#发件人地址
    password = ''           #密码刚才复制的邮箱的授权码
    to_addr =  'zyazhb@nefu.edu.cn'     #收件人地址
    smtp_server = ''    #邮箱服务器地址
    #设置邮件信息
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = _format_addr('站点状态自动报告系统<%s>'%from_addr)
    msg['To'] = _format_addr('管理员<%s>'%to_addr)
    msg['Subject'] = Header(title,'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server,465)        #发送邮件
    server.set_debuglevel(1)                          #打印出和SMTP服务器交互的所有信息
    server.login(from_addr,password)                  #登录SMTP服务器
    server.sendmail(from_addr,to_addr,msg.as_string())#sendmail():发送邮件，由于可以一次发给多个人，所以传入一个list邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.quit()
    print('邮件发送成功！')
print('sendmail Moudle loaded.');
