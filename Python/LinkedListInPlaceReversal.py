from typing import Optional
import sys


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insertval(self, val):
        node = ListNode(val)

        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head

        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            
            currentNode = currentNode.next
    
    def insertNode(self, node: ListNode):
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
    
    def getEndNode(self) -> ListNode:
        currentNode = self.head

        while True:
            if currentNode.next is None:
                return currentNode
            currentNode = currentNode.next

def hasCycle(head: ListNode) -> bool:
    #Problem #141 Linked List Cycle - Easy
    
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

def reverseList(head: Optional[ListNode]) -> Optional [ListNode]:
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

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #Problem #92 Reverse Linked List II - Medium

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

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    #Problem #24 Swap Nodes in Pairs - Medium

    if (head == None) or (head.next == None):
        return head
    
    currentNode = head
    nextNode = currentNode.next
    nextNextNode = None

    if currentNode.next != None:
        nextNextNode = currentNode.next.next
    
    flag = False

    while nextNextNode != None:
        temporaryNode = currentNode
        temporary2Node = nextNode
        temporary3Node = nextNextNode

        temporary2Node.next = temporaryNode

        if flag == False:
            flag = True
            head = temporary2Node

        temporaryNode4 = temporary3Node.next

        currentNode = temporary3Node
        nextNode = temporaryNode4

        if temporaryNode4 == None:
            temporaryNode.next = temporary3Node
            nextNextNode = None
        else: 
            nextNextNode = temporaryNode4.next

            temporaryNode4.next = currentNode
            temporaryNode.next = temporaryNode4
            currentNode.next = None
    
    
    if flag == False:
        temporaryNode = currentNode
        temporary2Node = currentNode.next

        temporary2Node.next = currentNode
        currentNode.next = None
        head = temporary2Node

    return head


if __name__ == "__main__":
    
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(13)
    node8 = ListNode(14)
    node9 = ListNode(15)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9

    editedLinkedList = swapPairs(head)

    traverse = editedLinkedList

    if (traverse == None) or (traverse == []):
        print(None)
    while traverse != None:
        print(traverse.val)
        traverse = traverse.next