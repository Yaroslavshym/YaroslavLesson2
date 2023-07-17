import hashlib

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')



def encode_md5(value:str) -> str:
    resoult = hashlib.md5(value.encode()).hexdigest()
    return resoult


def get_password(password: str) -> str:
    resoult = pwd_context.hash(password)
    return resoult


def verify_password(plain_password: str, hashed_password: str) -> bool:
    result = pwd_context.verify(plain_password, hashed_password)
    return result

res =  get_password('1')
print(res)
h = '$2b$12$.tOrd0AJEK6bmj7379HVVuQto3HFK32pohg9Sx60Nog0IzjUsJHKm'
print(verify_password('1', h))
