#! /usr/bin/python3
# coding:utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from  email.mime.base import MIMEBase
from email import encoders
import os.path

From="xxx"
To="xxx"
file_name="result.html"

server=smtplib.SMTP("smtp.126.com")
server.login(From,password)

#构建MIMEMultipart对象为根容器
main_msg=MIMEMultipart()

#构造MIMEText对象做为邮件内容
text_msg=MIMEText('python send email','plain','utf-8')
main_msg.attach(text_msg)

#构造MIMEBase对象做为邮件附件
contype='application/octet-stream'
maintype, subtype=contype.split('/',1)

#读取文件内容并格式化
data=open(file_name,'rb')
file_msg=MIMEBase(maintype,subtype)
file_msg.set_payload(data.read())
data.close()
encoders.encode_base64(file_msg)

#设置附件头
file_msg.add_header('Content-Disposition','attachment',filename=file_name)
main_msg.attach(file_msg)

#设置根容器属性
main_msg['From']=From
main_msg['To']=To
main_msg['Subject']='Test Result'

try:
    server.sendmail(From,To,main_msg.as_string())
finally:
    server.quit()
