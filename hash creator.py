from hashlib import sha256

def create_hash(data):
    hash = hashlib.sha256(data)
    return hash


print(create_hash("ok now then"))