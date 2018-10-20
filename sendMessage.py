import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sendAddr = "smarttrough.test.2019@gmail.com"
recAddr = "smartrough.test.2019@gmail.com"
msg = MIMEMultipart()
msg['From'] = sendAddr
msg['To'] = recAddr
msg['Subject'] = "Test of Message"

body = "Hello World!"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sendAddr, "2019smarttrough")
text = msg.as_string()
server.sendmail(sendAddr, recAddr, text)
server.quit()
