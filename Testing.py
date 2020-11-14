from blockchain_basis import Blockchain
import json

new = Blockchain("new")


new.create_node("Hello", "A", "B")


"""
with open("new.json") as readable:
    add_to = json.load(readable)
"""


    

new.create_node("Bye", "B", "C")



new.create_node("hmmm", "C","A")



#print(new.head_node.next_node)

#print(new.is_node_in_chain("Hello"))

#print(new.is_node_in_chain("Bye"))

#print(new.is_node_in_chain("hmmm"))

#print(new.is_node_in_chain("right"))



