from node_class import Node
from hash_creator import create_hash


#definition of the Blockchain class
class Blockchain:
    
    def __init__(self, name):
        self.name = name
        self.head_node = None
    
    def create_node(self, data):
        hash = create_hash(data)
        node = Node(hash, data, self.head_node)
        self.head_node = node
        
    
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
                
            
        
        
    

