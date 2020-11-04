class Node:
    
    def __init__(self, hash, data, next_node):
        self.hash = hash
        self.data = data
        self.next_node = next_node
    
    def __repr__(self):
        return self.hash
    
    

        