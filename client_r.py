from socket import *
import json
import logging


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8881))

while True:
    msg = s.recv(1024)
    print(msg)