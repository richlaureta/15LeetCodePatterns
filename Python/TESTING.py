class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(10)
node2 = Node(20)
node_addresses1 = {}

# Dictionary to store memory addresses of nodes
node_addresses = {node1: hex(id(node1)), node2: hex(id(node2))}
node_addresses1[node1] = 1
print(node_addresses1)
