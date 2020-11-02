from node_class import Node



#definition of the Blockchain class
class Blockchain:
    
    def __init__(self, name):
        self.name = name
        self.head_node = head_node()
    
    def create_node(self):
        hash = create_hash()
        node = Node(hash, self.head_node)
        self.head_node = node
    
    