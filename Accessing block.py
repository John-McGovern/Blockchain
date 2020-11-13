import json

new = {"tran_1" : {
    "hash" : "12345",
    "from" : "me",
    "to" : "you",
    "data" : "hello"
    },
       "tran_2" : {
    "hash" : "2468",
    "from" : "you",
    "to" : "me",
    "data" : "hi"
    }
       }

with open("blockchain_test.json", "w") as blockchain:
    json.dump(new, blockchain)
    
with open("blockchain_test.json") as blockchain:
    blockchain_access = json.load(blockchain)

print(blockchain_access["tran_1"]["hash"])





blockchain_access["tran_3"] = {
    "hash" : "369",
    "from" : "them",
    "to" : "they",
    "data" : "guten tag"}

with open("blockchain_test.json", "w") as blockchain:
    json.dump(blockchain_access, blockchain)
    

with open("blockchain_test.json") as blockchain:
    blockchain_access = json.load(blockchain)

print(blockchain_access["tran_3"]["data"])