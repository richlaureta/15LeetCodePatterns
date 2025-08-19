from typing import Optional
from time import sleep
import sys
import random
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

def findDuplicate(nums: list[int]) -> int:
    fastPointer = 1
    slowPointer = 1

    while True:
        if nums[slowPointer] == nums[fastPointer] and slowPointer != fastPointer:
            print("Cycle Detected!")
            print(slowPointer)
            print(fastPointer)
            break

        if slowPointer == len(nums) - 1:
            slowPointer = 0
        else:
            slowPointer += 1

        if fastPointer == len(nums) - 1:
            fastPointer = 1
        elif fastPointer == len(nums) - 2:
            fastPointer = 0
        else:
            fastPointer += 2

def isHappy(n: int) -> bool:
    #Problem #202 Happy Number

    digits = [int(d) for d in str(n)]
    sum = 0
    seen = set()
    
    while True: 
        for number in digits:
            sum += number * number
        
        digits = [int(d) for d in str(sum)]
        print(sum)
        if sum == 1:
            return True
        if sum in seen:
            return False
        seen.add(sum)
        
        sum = 0

if __name__ == "__main__":
    n = 2
    print(isHappy(n))