from socket import *
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8881))

while True:
    msg = input('')
    s.send(msg.encode())