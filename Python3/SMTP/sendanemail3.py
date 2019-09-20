#!/usr/bin/python3

# smtplib module send mail

import smtplib

TO = 'robin.greig@sait.ca'
SUBJECT = 'Raspi15 Battery Voltage LOW!'
TEXT = 'The Battery Voltage is below 24VDC on Raspi15'

# Gmail Sign In
gmail_sender = 'kananaskis@gmail.com'
gmail_passwd = 'glzapvguriwjqfur'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
