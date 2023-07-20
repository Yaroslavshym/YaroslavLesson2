import jwt
import datetime
import time


payload = {
    'my_name': 'Yaroslav',
    'password': 'skajsdha',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5),
}

encode_jdw = jwt.encode(
    payload=payload,
    key='secret',
    algorithm='HS256',
)

# print(encode_jdw)

time.sleep(6)
decoded = jwt.decode(
    encode_jdw,
    'secret',
    algorithms='HS256',
    # options={
    #     'verify_signature': False
    # }
)

print(decoded)
