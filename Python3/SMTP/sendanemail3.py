#!/usr/bin/python3

# smtplib module send mail

import smtplib

TO = 'robin.greig@calalta.com'
SUBJECT = 'Raspi15 Battery Voltage Monitor!'
TEXT = 'The Battery Voltage program on Raspi15 has run'

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
