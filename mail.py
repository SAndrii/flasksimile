#!/usr/bin/python
# -*- coding: utf-8 -*-
# mail.py example@gmail.com '/root/scripts/example.doc'

import smtplib
import sys
import mimetypes
import email
import email.mime.application

adrs = str(sys.argv[1])
file = str(sys.argv[2])
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'some subject'
msg['From'] = 'service@gmail.com'
msg['To'] = adrs
body = email.mime.Text.MIMEText(""" """)
msg.attach(body)
filename=file
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype=file[-3:])
fp.close()
att.add_header('Content-Disposition','attachment',filename=file)
msg.attach(att)
s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
s.login('service@gmail.com', 'ntktgjhn88') #login and password to your email account
s.sendmail('blablabla@gmail.com',[adrs], msg.as_string()) 
s.quit()
