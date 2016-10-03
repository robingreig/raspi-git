#!/usr/bin/python
import smtplib

fromaddrs = 've6rbn@gmail.com'
toaddrs = 'kananaskis@gmail.com'
msg = 'Voltage is below 24VDC on Raspi15 Batteries'

# Credentials
username = 'kananaskis'
password = 'Micr0s0ft2016'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddrs, toaddrs, msg)
server.quit()
