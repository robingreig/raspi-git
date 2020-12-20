#!/usr/bin/python3

# smtplib module send mail

import smtplib

DEBUG = 0

TO = 'robin.greig@calalta.com'
SUBJECT = 'Raspi15 Battery Voltage HIGH!'
TEXT = 'The Battery Voltage is above 27VDC on Raspi15 & charger is turning off'

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
    if DEBUG == 1:
      print ('email sent')
except:
    if DEBUG == 1:
      print ('error sending mail')

server.quit()
