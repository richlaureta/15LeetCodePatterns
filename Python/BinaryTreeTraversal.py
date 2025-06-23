import sys

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
    
def preOrder(node: Node):
        if node is None:
             return
        print(node.value, end=" ")
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node: Node):
        if node is None:
             return
        inOrder(node.left)
        print(node.value, end=" ")
        inOrder(node.right)
        

def postOrder(node: Node):
        if node is None:
             return
        postOrder(node.left)
        postOrder(node.right)
        print(node.value, end=" ")


    

def main():
    # Create a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    preOrder(root)
    print()
    inOrder(root)
    print()
    postOrder(root)
    print()
    
if __name__ == "__main__":
    sys.exit(main())