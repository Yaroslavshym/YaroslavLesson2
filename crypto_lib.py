import hashlib
def encode_md5(value:str) -> str:
    resoult = hashlib.md5(value.encode()).hexdigest()
    return resoult


print(encode_md5('6666666777'))
