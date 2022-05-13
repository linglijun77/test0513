# -*- coding: utf-8 -*-
# @File    : sendmail.py
#from openpyxl import Workbook
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.application import MIMEApplication
import smtplib
import time
import datetime
import os
file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))+'/Files/general_result.xls'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(), addr))


def sendMail():
    #输入Email地址和口令
    from_addr = 'yangli@emotibot.com'
    password = 'yangli@Emotibot'
    #输入收件人地址：
    to_list = ['yangyang@emotibot.com','yangli@emotibot.com','lijunling@emotibot.com','viclin@emotibot.com']
    # to_list = ['yangli@emotibot.com']
    #输入SMTP服务器地址：
    smtp_server = 'mail.emotibot.com'

    msg = MIMEMultipart()
    msg['From'] = _format_addr(' <%s> '%from_addr)
    msg['To'] = ','.join(to_list)
    msg['Subject'] = Header(u'BFOP线上环境出话测试结果','utf-8').encode()
    #邮件正文是MIMEText
    msg.attach(MIMEText('今天BFOP线上环境各模块出话测试结果如下（测试机器人test-LY），详情见附件','plain','utf-8'))
    #xlsx类型附件
    part = MIMEApplication(open(file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename='test_result.xls')
    msg.attach(part)

    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,to_list,msg.as_string())
    server.quit()



if __name__ == "__main__":
    sendMail()
