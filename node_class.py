class Node:
    
    def __init__(self, hash, data, next_node, pre_hash = 0):
        self.hash = hash
        self.data = data
        self.next_node = next_node
        self.pre_hash= pre_hash
    
    def __repr__(self):
        return self.hash
    
    

        