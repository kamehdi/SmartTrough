# SmartTrough
A 2018-2019 JMU ISAT Capstone project.
These Python Files are using in order to initiate a transfer of data between an Arduino UNO and a Raspberry Pi 0 W. The medium that is used to instantiate data transfer is with a device called the XBEE Pro S3B. 

serial_test.py is a script that will allow for the data read from the Arduino to be sent through the serial interface and received by the RPi 0 W.

sendMessage.py is a simple script that will send a blank email from the RPi 0 W to a gmail account used for testing.

sendMessagePressure.py is a script that will allow for the data from the Arduino to be sent to the RPi and then sent in an email to the test gmail account. The data along with other text from the Arduino scripts will seen within an attachment in the email sent.
