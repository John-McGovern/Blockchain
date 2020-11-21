"""
This file contains the hashing function.
"""



from hashlib import sha256      

"""
The function takes new data and previous blocks hash (defaults to 0, if no previous hash), encodes then hashes it. It then adds a nonce onto the hash to make it harder
to reproduce. The function finally then returns the hash and its pre-hash.

Have to add previous data and new data together at encode stage.
"""
def create_hash(data, previous_pre_hash = str(0).encode()):
    pre_sha = data.encode() + previous_pre_hash
    hash = sha256(pre_sha).hexdigest()
    extra = 0
    while not hash.startswith("00"):
        data = str(extra).encode() + pre_sha
        hash = sha256(data).hexdigest()
        extra = int(extra) + 1
    return hash, pre_sha





#print(create_hash("erm"))
