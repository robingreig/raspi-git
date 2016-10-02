import smtplib

fromaddrs = 've6rbn@gmail.com'
toaddrs = 'kananaskis@gmail.com'
msg = 'Test email from ve6rbn'

# Credentials
username = 'kananaskis'
password = 'Micr0s0ft2016'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddrs, toaddrs, msg)
server.quit()
