from hashlib import sha256

"""
def create_hash(data):
    extra = 0
    data = str(extra) + data
    hash = sha256(data.encode()).hexdigest()
    while hash[0] < 7:
        hash = sha256(data.encode()).hexdigest()
        
    #hash = (sha256(data.encode()) + sha256(extra.encode())).hexdigest()
    return hash
 """       


"""
def create_hash(data):
    hash = None
    extra = 0
    while True:
        try:
            if int(hash[0]) > 7:
                print("Q")
                return hash
        #except ValueError or TypeError:
        except:
            print("I")
            print(hash)
            data = str(extra) + data
            hash = sha256(data.encode()).hexdigest()
            print(type(hash[0]))
            extra = int(extra) + 1
 

def create_hash(data, extra =0):
    while True:
        try:
            print("E")
            print(hash[0])
            if int(hash[0]) > 7:
                print("Q")
                return hash
        #except ValueError or TypeError:
        except:
            #print("I")
            #print(hash)
            data = str(extra) + data
            hash = sha256(data.encode()).hexdigest()
            print(type(hash[0]))
            print(hash)
            extra = int(extra) + 1
            create_hash(data, extra)
"""        

def create_hash(data):
    hash = sha256(data.encode()).hexdigest()
    extra = 0
    while not hash.startswith("00"):
        data = str(extra) + data
        hash = sha256(data.encode()).hexdigest()
        print(type(hash[0]))
        print(hash)
        extra = int(extra) + 1
    return hash



print(create_hash("smelly"))