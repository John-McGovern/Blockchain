"""
This file contains the Blockchain app and its methods.
"""
from node_class import Node
from hash_creator import create_hash
from Validation_class_error import Hash_Validation_Error
import json


#Definition of the Blockchain class
class Blockchain:
    """
    The initalisation method for the Blockcahin class. It requires a name and the users of the blockcahin to be given.
    The chains, name, head_node, json and users can be accessed using the self. method
    """
    def __init__(self, name, users):
        self.name = name
        self.head_node = None
        file = {}
        with open(f"{str(name)}.json", 'w') as json.file:
            json.dump(file, json.file)
        self.json = f"{str(name)}.json"
        self.users = users
    """    
    This method creates a node (or block) for the chain. It becomes the head node of the chain. 
    It also checks that the hash meets the nonces requirement are met (the hash starting with 00).
    If it is the node is added to the chain, if not then a error is raised.
    """
    def create_node(self, data, giver, receiver):
        if self.head_node != None:
            hash, pre_hash = create_hash(data, self.head_node.pre_hash)
        else:
            hash, pre_hash = create_hash(data)
        if not hash.startswith("00"):
            raise Hash_Validation_Error("The Hash for this node is invalid")
        node = Node(hash, data, self.head_node, giver, receiver, pre_hash)
        self.head_node = node
        self.update_blockchain_json(node.json)
        return True
     
    """
    This method searches through the chain, with a given username and finds all of the transactions of that user.
    """
    def users_transactions(self, user):
        users_transactions = []
        with open(f"{self.json}") as json.file:
            read = json.load(json.file)
        for hash, items in read.items():
            if read[hash]["from"] == user:
                users_transactions.append(hash)
            elif read[hash]["to"] == user:
                users_transactions.append(hash)
        users_transactions = [read[hash] for hash in users_transactions]
        return users_transactions

    """
    This adds a dictionary to the chain, by accessing its json file.
    """
    def update_blockchain_json(self, dictionary):
        with open(f"{self.json}") as readable:
            add_to = json.load(readable)
        add_to.update(dictionary)
        with open(f"{self.json}", 'w') as json.file:
            json.dump(add_to, json.file)
        
        
   


        
        
    

