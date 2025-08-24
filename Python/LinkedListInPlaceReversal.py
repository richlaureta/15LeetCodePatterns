from typing import Optional
import sys


class linkedListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insertval(self, val):
        node = linkedListNode(val)

        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head

        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            
            currentNode = currentNode.next
    
    def insertNode(self, node: linkedListNode):
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head

        while True:
            if currentNode.next is None:
                currentNode.next = node
                return
            currentNode = currentNode.next
    
    def printLinkedList(self):
        if self.head is None:
            print('None')
            return
        
        currentNode = self.head

        while True:
            print(f'{currentNode.val} -> ', end="")
            
            if currentNode.next is None:
                print('None')
                return
            
            currentNode = currentNode.next
    
    def getEndNode(self) -> linkedListNode:
        currentNode = self.head

        while True:
            if currentNode.next is None:
                return currentNode
            currentNode = currentNode.next

def hasCycle(head: linkedListNode) -> bool:
    #Problem #141 Linked List Cycle
    
    if head is None:
        return False
    
    slowPointer = head
    fastPointer = head
    
    while True:        
        if slowPointer.next is None:
            return False
            
        slowPointer = slowPointer.next
        
        if fastPointer is None or fastPointer.next is None or fastPointer.next.next is None:
            return False
        fastPointer = fastPointer.next.next

        if slowPointer == fastPointer:
            return True

def reverseList(head: Optional[linkedListNode]) -> Optional [linkedListNode]:
    if head is None:
        return head
    
    currentNode = head
    previousNode = head
    next = head.next
    
    currentNode.next = None

    while(next != None):
        currentNode = next
        next = next.next        
        currentNode.next = previousNode
        previousNode = currentNode

    return currentNode

def reverseBetween(head: Optional[linkedListNode], left: int, right: int) -> Optional[linkedListNode]:
    #Problem #92 Reverse Linked List II

    rememberLeftNode = None
    rememberReversedLeftNode = None
    currentNode = head
    leftIndex = 1
    
    while currentNode != None:
        if leftIndex + 1 == left:
            rememberLeftNode = currentNode
            rememberReversedLeftNode = currentNode.next
        
        if leftIndex == left:
            previousNode = None
            nextHere = currentNode.next

            while leftIndex != right:
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextHere
                nextHere = nextHere.next
                leftIndex += 1
            
            currentNode.next = previousNode

            if rememberLeftNode == None:
                head.next = nextHere
                head = currentNode
            else:
                rememberLeftNode.next = currentNode

            if rememberReversedLeftNode != None:
                rememberReversedLeftNode.next = nextHere

            return head
        
        currentNode = currentNode.next
        leftIndex += 1

if __name__ == "__main__":
    
    head = linkedListNode(5)
    node2 = linkedListNode(5)
    node3 = linkedListNode(6)
    node4 = linkedListNode(9)
    node5 = linkedListNode(10)
    node6 = linkedListNode(11)
    node7 = linkedListNode(13)
    node8 = linkedListNode(14)
    node9 = linkedListNode(15)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9

    editedLinkedList = reverseBetween(head, 1, 5)

    traverse = editedLinkedList

    if traverse == None:
        print(None)
    while traverse != None:
        print(traverse.val)
        traverse = traverse.next