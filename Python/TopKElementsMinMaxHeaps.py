import heapq
from collections import Counter

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
    #Problem #215 Kth Largest Element in an Array

    array = []

    for i in range(0, k):
        heapq.heappush(array, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > array[0]:
            heapq.heappop(array)
            heapq.heappush(array, nums[i])
    
    return array[0]

def topKFrequent(nums: list[int], k: int) -> list[int]:
    #Problem #347 Top K Frequent Elements

    frequencyArray = [0] * (len(nums) + 1)
    myDictionary = Counter(nums)

    for key in myDictionary:
        if frequencyArray[myDictionary[key]] == 0:
            frequencyArray[myDictionary[key]] = [key]
        else:
            frequencyArray[myDictionary[key]].append(key)
   
    topKArray = []

    for indexItem in reversed(frequencyArray):
        if k == 0:
            break

        if indexItem == 0:
            continue
        elif indexItem != 0 and len(indexItem) > 1:
            for item in indexItem:
                if k == 0:
                    break

                topKArray.append(item)
                k -= 1
        else:
            topKArray.append(indexItem[0])
            k -= 1
    
    return topKArray

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    #Problem #373 Find K Pairs with Smallest Sums - Concept Solution by YouTuber TechError

    result = []
    visitedPairSet = set()
    minHeap = []

    sum = nums1[0] + nums2[0]
    heapq.heappush(minHeap, (sum, 0, 0))
    visitedPairSet.add((0, 0))

    while k and minHeap:
        sum, indexList1, indexList2 = heapq.heappop(minHeap)
        result.append([nums1[indexList1], nums2[indexList2]])

        if indexList1 + 1 < len(nums1) and (indexList1 + 1, indexList2) not in visitedPairSet:
            heapq.heappush(minHeap, (nums1[indexList1+1] + nums2[indexList2], indexList1 + 1, indexList2 ))
            visitedPairSet.add((indexList1 + 1, indexList2))

        if indexList2 + 1 < len(nums2) and (indexList1, indexList2 + 1) not in visitedPairSet:
            heapq.heappush(minHeap, (nums1[indexList1] + nums2[indexList2 + 1], indexList1, indexList2 + 1))
            visitedPairSet.add((indexList1, indexList2 + 1))

        k -= 1 
    
    return result

if __name__ == "__main__":
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]

    k = 3

    print(kSmallestPairs(nums1, nums2, k))