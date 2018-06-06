from socket import *
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8881))

pres_msg = {
    'action': 'presence',
    'type': 'online'
}

def msg_encode(msg):
    j_msg = json.dumps(msg)
    b_msg = j_msg.encode('utf-8')
    return b_msg


def msg_decode(msg):
    b_msg = msg.decode('utf-8')
    j_msg = json.loads(b_msg)
    return j_msg


s.send(msg_encode(pres_msg))
response = s.recv(1024)
x = msg_decode(response).get('text')
print(x)

s.close()
