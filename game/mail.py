# -*- coding: UTF-8 -*-
import email
import smtplib
from email.mime.text import MIMEText

email_addr='lifeisnofair@163.com'
email_pwd='meiwenjie5917'
email_rec='bboysoulcn@gmail.com'
msg=['sadsa','sadsadsa']

email_proj=smtplib.SMTP('smtp.163.com')
email_proj.login(email_addr,email_pwd)
email_proj.sendmail(email_addr,email_rec,)
