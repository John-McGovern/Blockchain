"""
This file contains the Node class defintion, which could also be called a block.
"""

class Node:
    
    def __init__(self, hash, data, next_node,  giver, receiver, pre_hash = 0,):
        self.hash = hash
        self.data = data
        self.next_node = next_node
        self.pre_hash= pre_hash
        self.giver = giver
        self.receiver = receiver
        self.json = { f"{self.hash}" :{
                                "from": f"{self.giver}",
                                "to": f"{self.receiver}",
                                "data": f"{self.data}"}
                      }
    
    def __repr__(self):
        return self.hash
    
    

        