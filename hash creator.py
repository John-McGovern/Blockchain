from hashlib import sha256

def create_hash(data):
    hash = sha256(data)
    return hash


print(create_hash("ok now then"))