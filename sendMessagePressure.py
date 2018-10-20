import time
import serial
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

prevPress = None
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()

while True:
    #ser = serial.Serial('/dev/ttyUSB0',9600)
    #x = str(ser.readline())
    #curPress = x[2:(len(x)-5)]
    #curPress = curPress.strip(' ')
    #ser.flushInput()
    curPress = ser.readline()
    print(curPress)

    curDat = datetime.datetime.now()
    d = curDat.strftime("%Y-%m-%d")
    t = curDat.strftime("%I:%M:%S %p")

    if curPress == " ":
        print('{} {} \t No Data'.format(d,t))

    elif curPress != prevPress:

        sendAddr = "smarttrough.test.2019@gmail.com"
        recAddr = "5712450037@vtext.com"
        msg = MIMEMultipart()
        msg['From'] = sendAddr
        msg['To'] = recAddr
        msg['Subject'] = "Test of Message"

        body = curPress
        msg.attach(MIMEText(body, 'Current Pressure'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sendAddr, "2019smarttrough")
        text = msg.as_string()
        server.sendmail(sendAddr, recAddr, text)
        server.quit()

    else:
        print(curPress)
