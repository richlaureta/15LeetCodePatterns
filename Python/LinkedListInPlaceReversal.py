from typing import Optional

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

def reverseList(head: ListNode) -> ListNode:
    #Problem #206 Reverse Linked List - Easy
    
    if head == None:
        return head
    
    previousNode = None
    currentNode = head
    nextNode = currentNode.next
    
    while nextNode != None:
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
        nextNode = nextNode.next
    
    currentNode.next = previousNode
    
    return currentNode

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #Problem #92 Reverse Linked List II - Medium
    
    if left == right:
        return head
    
    currentNode = head
    leftNode = None
    traverseIndex = 0
    
    while traverseIndex + 1 < left:
        leftNode = currentNode
        currentNode = currentNode.next
        traverseIndex += 1
    
    pointRightEndNode = currentNode
    
    previousNode = currentNode
    nextNode = currentNode.next
    while traverseIndex + 1 < right:
        currentNode = nextNode
        nextNode = nextNode.next
        currentNode.next = previousNode
        previousNode = currentNode
            
        traverseIndex += 1
    
    pointRightEndNode.next = nextNode
    
    if left > 1:
        leftNode.next = currentNode
        return head

    return currentNode

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    #Problem #24 Swap Nodes in Pairs - Medium
    
    if head == None or head.next == None:
        return head
        
    currentNode = head
        
    nextNode = currentNode.next
    nextNextNode = None
    previousNode = currentNode
    initialSwapFlag = False
        
    while currentNode != None and nextNode != None:                
        nextNextNode = nextNode.next
        currentNode.next = nextNextNode
        nextNode.next = currentNode
        currentNode = nextNextNode

        if initialSwapFlag == True:
            previousNode.next = nextNode
            previousNode = nextNode.next
        if initialSwapFlag == False:
            head = nextNode
            initialSwapFlag = True
        if currentNode != None:
            nextNode = currentNode.next
            
    return head
def swapNodes(head: ListNode, k: int) -> ListNode:
    #Problem #1721 Swapping Nodes in a Linked List - Medium
    
    currentNode = head
    for index in range(k - 1):
        currentNode = currentNode.next
    
    leftSwapPointer = currentNode
    rightSwapPointer = head
    while currentNode.next:
        rightSwapPointer = rightSwapPointer.next
        currentNode = currentNode.next
    
    leftSwapPointer.val, rightSwapPointer.val = rightSwapPointer.val, leftSwapPointer.val
    
    return head
   
if __name__ == "__main__":
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6
    # node6.next = node7
    # node7.next = node8
    # node8.next = node9
    head = node1
    
    currentNode = swapNodes(head, 2)
    
    while currentNode != None:
        print(currentNode.val)
        currentNode = currentNode.next