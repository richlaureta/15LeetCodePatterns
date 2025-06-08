from typing import Optional
import sys


class linkedListNode:
    def __init__(self, value = 0, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insertValue(self, value):
        node = linkedListNode(value)

        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head

        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            
            currentNode = currentNode.nextNode
    
    def insertNode(self, node: linkedListNode):
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head

        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                return
            currentNode = currentNode.nextNode
    
    def printLinkedList(self):
        if self.head is None:
            print('None')
            return
        
        currentNode = self.head

        while True:
            print(f'{currentNode.value} -> ', end="")
            
            if currentNode.nextNode is None:
                print('None')
                return
            
            currentNode = currentNode.nextNode
    
    def getEndNode(self) -> linkedListNode:
        currentNode = self.head

        while True:
            if currentNode.nextNode is None:
                return currentNode
            currentNode = currentNode.nextNode

def hasCycle(head: linkedListNode) -> bool:
    #Problem #141 Linked List Cycle
    
    if head is None:
        return False
    
    slowPointer = head
    fastPointer = head
    
    while True:        
        if slowPointer.nextNode is None:
            return False
            
        slowPointer = slowPointer.nextNode
        
        if fastPointer is None or fastPointer.nextNode is None or fastPointer.nextNode.nextNode is None:
            return False
        fastPointer = fastPointer.nextNode.nextNode

        if slowPointer == fastPointer:
            return True

def reverseList(head: Optional[linkedListNode]) -> Optional [linkedListNode]:
    
    currentNode = head
    previousNode = head
    nextNode = head.nextNode
    
    currentNode.nextNode = None

    while(nextNode != None):
        currentNode = nextNode
        nextNode = nextNode.nextNode        
        currentNode.nextNode = previousNode
        previousNode = currentNode

    while(currentNode != None):
        print(currentNode.value)
        currentNode = currentNode.nextNode
        
    return currentNode




        
def main():
    #Problem #141 Linked List Cycle

    node0 = linkedListNode("3")
    node1 = linkedListNode("2")
    node2 = linkedListNode("0")
    node3 = linkedListNode("-4")

    ll = LinkedList(node0)

    ll.insertNode(node1)

    nodeC = ll.getEndNode()

    ll.insertNode(node2)

    ll.insertNode(node3)

    # ll.insertNode(nodeC)

    print(hasCycle(node0))

    #Problem #206 Reverse Linked List
    reverseList(node0)

if __name__ == "__main__":
    sys.exit(main())