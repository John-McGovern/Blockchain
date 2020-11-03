from node_class import Node
from hash_creator import create_hash


#definition of the Blockchain class
class Blockchain:
    
    def __init__(self, name):
        self.name = name
        self.head_node = None
    
    def create_node(self, data):
        hash = create_hash(data)
        node = Node(hash, self.head_node)
        self.head_node = node
    

new = Blockchain("new")


new.create_node("Hello")


print(new.head_node)

new.create_node("Bye")

print(new.head_node)
