from blockchain_basis import Blockchain
import json

new = Blockchain("new")


new.create_node("Hello", "A", "B")





    

new.create_node("Bye", "B", "C")



new.create_node("hmmm", "C","A")


with open("new.json") as readable:
    add_to = json.load(readable)

print(add_to)

for key, value in add_to.items():
    for hasher, data in add_to[key].items():
        if data == "A":
            print(value)

#print(new.head_node.next_node)

#print(new.is_node_in_chain("Hello"))

#print(new.is_node_in_chain("Bye"))

#print(new.is_node_in_chain("hmmm"))

#print(new.is_node_in_chain("right"))



