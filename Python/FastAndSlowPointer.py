from typing import Optional
from time import sleep
import sys
import random
class linkedListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

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
    #Problem #141 Linked List Cycle - Easy
    
    slowPointer = head
    fastPointer = head
    
    while fastPointer != None and fastPointer.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        
        if slowPointer == fastPointer:
            return True
    
    return False

def findDuplicate(nums: list[int]) -> int:
    #Problem #287 Find the Duplicate Number - Medium
    #Start at index 0 which is the valuePointer 

    slowPointer = nums[0]
    fastPointer = nums[0]

    while True:
        slowPointer = nums[slowPointer] #Syntax for slowPointer
        fastPointer = nums[nums[fastPointer]] #Syntax for fastPointer
        if slowPointer == fastPointer:
            break

    #Find the entry Point of the cycle 
    pointer1 = nums[0] 
    pointer2 = fastPointer #This pointer is at the meeting point 
    
    while pointer1 != pointer2:
        pointer1 = nums[pointer1] #The value(pointer) is at index 0
        pointer2 = nums[pointer2] #This is the meeting point 

    return pointer2

def isHappy(n: int) -> bool:
    #Problem #202 Happy Number - Easy
    #TESTING
    squaresSum = n
    seenNumbers = set()
    while squaresSum != 1:
        temporaryNumber = squaresSum
        numberSum = 0
        while temporaryNumber != 0:
            squaresSum = temporaryNumber % 10
            temporaryNumber //= 10
            numberSum += squaresSum ** 2
        squaresSum = numberSum    
        if squaresSum in seenNumbers:
            return False
        seenNumbers.add(numberSum)
        
    return True
if __name__ == "__main__":
    n = 19
    print(isHappy(n))

