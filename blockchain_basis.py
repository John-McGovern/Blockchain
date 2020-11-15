from node_class import Node
from hash_creator import create_hash
from Validation_class_error import Hash_Validation_Error
import json


#definition of the Blockchain class
class Blockchain:

    
    def __init__(self, name, users):
        self.name = name
        self.head_node = None
        file = {}
        with open(f"{str(name)}.json", 'w') as json.file:
            json.dump(file, json.file)
        self.json = f"{str(name)}.json"
        self.users = users
        
    
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
        
    #no longer works
    def is_node_in_chain(self, data):
        hash = create_hash(data)
        current_node = self.head_node
         
        while True:
            if current_node.hash == hash:
                return True
            elif not current_node.next_node:
                return False
            else:
                current_node = current_node.next_node
    
    def update_blockchain_json(self, dictionary):
        with open(f"{self.json}") as readable:
            add_to = json.load(readable)
        add_to.update(dictionary)
        with open(f"{self.json}", 'w') as json.file:
            json.dump(add_to, json.file)
        
        
   


        
        
    

