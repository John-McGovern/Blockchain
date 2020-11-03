from hashlib import sha256

def create_hash(data):
    proof = str(0)
    hash = 11
    while hash[0] != 0 and hash[1] != 0:
        hash = sha256(data.encode()).hexdigest() + sha256(proof).hexdigest()
        proof+=1 
    return hash



#print(create_hash("ok now then"))