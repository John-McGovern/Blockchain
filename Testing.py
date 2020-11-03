from blockchain_basis import Blockchain

new = Blockchain("new")


new.create_node("Hello")


#print(new.head_node)

new.create_node("Bye")

#print(new.head_node)

new.create_node("hmmm")

#print(new.head_node)

#print(new.head_node.next_node)

#print(new.is_node_in_chain("Hello"))

#print(new.is_node_in_chain("Bye"))

#print(new.is_node_in_chain("hmmm"))

print(new.is_node_in_chain("right"))