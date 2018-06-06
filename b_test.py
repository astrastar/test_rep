import json, unittest
import pytest
s = 'Привет'
sb = s.encode('utf-8')
print(sb)

message = {
    'q': 'ff',
    'f': 'rr'
}

jmessage = json.dumps(message)
print(jmessage)