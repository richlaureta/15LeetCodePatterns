import sys
import heapq

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
    myDictionary = {}
    myHeap = []

    for i in range(0, len(nums)):
        if nums[i] not in myDictionary:
            myDictionary[nums[i]] = 1
        else:
            myDictionary[nums[i]] += 1
    
    for key in myDictionary:
        heapq.heappush(myHeap, [myDictionary[key], key])

    topLargest = heapq.nlargest(k, myHeap)
    topKArray = []

    for i in topLargest:
        topKArray.append(i[1])
    
    return topKArray

    
def main():
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 3

    # print(findKthLargestElement(nums, k))

    nums = [1, 1, 1, 2, 2, 3]

    print(topKFrequent(nums, 3))
if __name__ == "__main__":
    sys.exit(main())