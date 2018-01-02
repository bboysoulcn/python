# coding:utf-8
import smtplib
from email.mime.text import MIMEText
import os

def mail():
    sender='lifeisnofair@163.com'
    receive='bboysoulcn@gmail.com'
    pwd='meiwenjie5917'
    smtp_host='smtp.163.com'
    msg=MIMEText('温度过高')
    msg['from']=sender
    msg['to']=receive
    msg['subject']='提醒'
    mail=smtplib.SMTP(smtp_host)
    mail.login(sender,pwd)
    print("login successful")
    mail.sendmail(sender,receive,msg.as_string())
    print('send successful')
    mail.quit()

temp=int(os.system('sh ./temp.sh'))
print(temp)
if(temp>10):
    mail()
else:
    print('温度不高')