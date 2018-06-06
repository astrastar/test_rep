from socket import *
import json

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8881))
s.listen(5)


def msg_decode(msg):
    b_msg = msg.decode('utf-8')
    j_msg = json.loads(b_msg)
    return j_msg


def msg_encode(msg):
    j_msg = json.dumps(msg)
    b_msg = j_msg.encode('utf-8')
    return b_msg


while True:
    client, addr = s.accept()
    x = client.recv(1024)
    if msg_decode(x).get('action') == 'presence':
        response = {
            'response': '200',
            'text': 'OK'
        }
        client.send(msg_encode(response))
    else:
        response = {
            'response': '400',
            'text': 'Error'
        }
        client.send(msg_encode(response))

    client.close()