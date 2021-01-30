#!/usr/bin/python3

# smtplib module send mail

import smtplib

TO = 'robin.greig@calalta.com'
SUBJECT = 'House Temp LOW'
TEXT = 'The House Temp is below 15C'

# Gmail Sign In
gmail_sender = 'kananaskis@gmail.com'
gmail_passwd = 'gjodocqcmaqozrgq'

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
