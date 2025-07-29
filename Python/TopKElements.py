import sys
import heapq
from collections import Counter
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

    #My Intuitive Solution
    # myDictionary = {}
    # myHeap = []

    # for i in range(0, len(nums)):
    #     if nums[i] not in myDictionary:
    #         myDictionary[nums[i]] = 1
    #     else:
    #         myDictionary[nums[i]] += 1
    
    # for key in myDictionary:
    #     heapq.heappush(myHeap, [myDictionary[key], key])

    # topLargest = heapq.nlargest(k, myHeap)
    # topKArray = []

    # for i in topLargest:
    #     topKArray.append(i[1])
    
    # return topKArray

    #Optimized Solution

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


def main():
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 3

    # print(findKthLargestElement(nums, k))

    nums = [1,1,1,2,2,3]

    print(topKFrequent(nums, 2))
if __name__ == "__main__":
    sys.exit(main())