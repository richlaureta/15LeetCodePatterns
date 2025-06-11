#These codes from this file are from Udemy titled Python Data Structures & Algorithms + LEETCODE Exercises by Scott Barett

import sys

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def leftChild(self, index):
        return 2 * index + 1
    
    def rightChild(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1) // 2
    
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
    
    def insert(self, number):
        self.heap.append(number)
        currentIndex = len(self.heap) - 1

        while number > self.heap[self.parent(currentIndex)] and currentIndex > 0:
            self.swap(currentIndex, self.parent(currentIndex))
            currentIndex = self.parent(currentIndex)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        poppedValue = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sinkDown(0)

        return poppedValue
    
    def sinkDown(self, index):
        pass
def main():
    addingToHeap = MaxHeap()

    addingToHeap.insert(80)
    addingToHeap.insert(75)
    addingToHeap.insert(65)
    addingToHeap.insert(55)
    addingToHeap.insert(50)
    addingToHeap.insert(60)
    print(addingToHeap.heap)

    addingToHeap.remove()

    print(addingToHeap.heap)

if __name__ == "__main__":
    sys.exit(main())