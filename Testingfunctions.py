from time import sleep
from SendMessage import send_message
from failedEmail import messageReader
send_message('awegwegweff@yahoo.com','Testing 123', 'Hello this is kenneth')
sleep(5)
send_message('trankenneth@sbcglobal.net','Testing 123', 'Hello this is kenneth')
sleep(30)
send = messageReader('awegwegweff@yahoo.com')
sleep(5)
send2 = messageReader('trankenneth@sbcglobal.net')
print (send)
print (send2)