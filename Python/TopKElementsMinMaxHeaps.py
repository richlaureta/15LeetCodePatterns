import heapq
from collections import Counter
from collections import defaultdict

class MaxHeap:
    #These code concept for maxHeap are from Udemy titled Python Data Structures & Algorithms + LEETCODE Exercises by Scott Barett

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
        maxNumberIndex = index

        while True:
            leftIndex = self.leftChild(index)
            rightIndex = self.rightChild(index)

            if (leftIndex < len(self.heap)) and self.heap[leftIndex] > self.heap[maxNumberIndex]:
                maxNumberIndex = leftIndex
            
            if (rightIndex < len(self.heap)) and (self.heap[rightIndex] > self.heap[maxNumberIndex]):
                maxNumberIndex = rightIndex

            if maxNumberIndex != index:
                self.swap(maxNumberIndex, index)
                index = maxNumberIndex
            else:
                return

def findKthLargestElement(nums: list[int], k: int) -> int:
    #Problem #215 Kth Largest Element in an Array - Medium - This solution uses heap.
    
    maxK = []
    
    for index in range(len(nums)):
        if len(maxK) < k:
            heapq.heappush(maxK, nums[index])
        else:
            heapq.heappushpop(maxK, nums[index])
    
    return maxK[0]

def topKFrequent(nums: list[int], k: int) -> list[int]:
    #Problem #347 Top K Frequent Elements - Medium
    
    frequencyDictionary = defaultdict(int)
    minHeap = []
    for number in nums:
        frequencyDictionary[number] += 1
    
    
    for uniqueNumber in frequencyDictionary:
        if len(minHeap) < k:
            heapq.heappush(minHeap, [frequencyDictionary[uniqueNumber], uniqueNumber])
        else:
            heapq.heappushpop(minHeap, [frequencyDictionary[uniqueNumber], uniqueNumber])
    
    topElements = []
    for frequency, element in minHeap:
        topElements.append(element)
    
    return topElements

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    #Problem #373 Find K Pairs with Smallest Sums - Medium
    
    kSmallestPairSum = []
    
    for firstNumber in nums1:
        for secondNumber in nums2:
            if len(kSmallestPairSum) < k:
                heapq.heappush_max(kSmallestPairSum, [firstNumber + secondNumber, firstNumber, secondNumber])
            elif firstNumber + secondNumber < kSmallestPairSum[0][0]:
                heapq.heappushpop_max(kSmallestPairSum, [firstNumber + secondNumber, firstNumber, secondNumber])
            else:
                break
    
    kSmallestPairSumList = []
    
    while kSmallestPairSum:
        poppedSum = heapq.heappop_max(kSmallestPairSum)
        kSmallestPairSumList.append([poppedSum[1], poppedSum[2]])
    
    return kSmallestPairSumList
if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    
    k = 2

    print(kSmallestPairs(nums1, nums2, k))