import sys
from typing import List

def findMaxLength(nums: list[int]) -> int:
    #Problem #525 Contiguous Array

    #Solution Concept by Youtuber NeetCodeIO
    zeroCount = 0
    oneCount = 0
    result = 0
    differenceIndex = {} # count of 1 - count of 0 -> index 

    for index, value in enumerate(nums):
        if value == 1:
            oneCount += 1
        else:
            zeroCount += 1

        if (oneCount - zeroCount) not in differenceIndex:
            differenceIndex[oneCount - zeroCount] = index
        
        if oneCount == zeroCount:
            result = oneCount + zeroCount
        else:
            index0 = differenceIndex[oneCount - zeroCount]
            result = max(result, index - index0)

    return result

def prefixSum(numbers: List[int]):
    for i in range(1, len(numbers)):
            numbers[i] += numbers[i - 1]

class NumArray:
    #Problem #303 Range Sum Query - Immutable

    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        self.prefixSumArray = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSumArray[right]
        else:
            return (self.prefixSumArray[right] - self.prefixSumArray[left - 1])

def subArraySum(nums: list[int], k: int) ->int:
    #Problem #560 Subarray Sum Equals K
    
    #Solution Concept by Youtube Channel NeetCodeIO
    result = 0
    currentSum = 0
    prefixSums = {0 : 1}

    for number in nums:
        currentSum += number
        difference = currentSum - k

        result += prefixSums.get(difference, 0)
        prefixSums[currentSum] = 1 + prefixSums.get(currentSum, 0)

    return result

def main():
    # nums: List[int] = [-2,0,3,-5,2,-1]

    # prefixSum(nums)
    
    # print(nums)

    # nums = [1, 1, 1, 0, 0]

    # print(findMaxLength(nums))

    nums = [0, 1, 0, 1, 0, 1]
    k = 2

    print(subArraySum(nums, k))

if __name__ == "__main__":
    sys.exit(main())