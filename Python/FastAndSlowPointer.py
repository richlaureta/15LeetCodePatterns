from typing import Optional
from time import sleep
import sys

class linkedListNode:
    def __init__(self, value, nextNode = None):
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
    
    pointer = head
    mySet = set()

    while pointer != None:
       if(str(hex(id(pointer)))) in mySet:
           return True
       mySet.add(str(hex(id(pointer))))
       
       pointer = pointer.nextNode

    return False
    # slowPointer = head
    # fastPointer = head
    
    # while True:        
    #     if slowPointer.nextNode is None:
    #         return False
            
    #     slowPointer = slowPointer.nextNode
        
    #     if fastPointer is None or fastPointer.nextNode is None or fastPointer.nextNode.nextNode is None:
    #         return False
    #     fastPointer = fastPointer.nextNode.nextNode

    #     if slowPointer == fastPointer:
    #         breakCycle = input("The linked list has a cycle, do you want to break it? Enter y for yes, Enter n for no.").lower

    #         return True
        
def main():
    node0 = linkedListNode("3")
    node1 = linkedListNode("2")
    node2 = linkedListNode("0")
    node3 = linkedListNode("-4")

    ll = LinkedList(node0)

    ll.insertNode(node1)

    nodeC = ll.getEndNode()

    ll.insertNode(node2)

    ll.insertNode(node3)

    ll.insertNode(nodeC)

    print(hasCycle(node0))

if __name__ == "__main__":
    sys.exit(main())