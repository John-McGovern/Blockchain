from hashlib import sha256      

def create_hash(data):
    hash = sha256(data.encode()).hexdigest()
    extra = 0
    while not hash.startswith("00"):
        data = str(extra) + data
        hash = sha256(data.encode()).hexdigest()
        extra = int(extra) + 1
    return hash



#print(create_hash("smelly"))