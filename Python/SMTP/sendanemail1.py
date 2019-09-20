#!/usr/bin/python
import smtplib

fromaddrs = 've6rbn@gmail.com'
toaddrs = 'kananaskis@gmail.com'
SUBJECT = 'Raspi15 Voltage Low'
TEXT = 'Voltage is below 24VDC on Raspi15 Batteries'
msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

# Credentials
username = 'kananaskis'
password = 'glza pvgu riwj qfur'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddrs, toaddrs, msg)
server.quit()
