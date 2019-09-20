#!/usr/bin/python3
import smtplib

fromaddrs = 've6rbn@gmail.com'
toaddrs = 'kananaskis@gmail.com'
#sub = 'Raspi15 Voltage Low'
msg = 'Voltage is below 24VDC on Raspi15 Batteries'

# Credentials
username = 'kananaskis'
password = 'glza pvgu riwj qfur'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
#server.sendmail(fromaddrs, toaddrs, sub, msg)
server.sendmail(fromaddrs, toaddrs, msg)
server.quit()
