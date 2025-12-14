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
    #Problem #303 Range Sum Query - Immutable - Easy
    #Pattern: Prefix Sum
    
    def __init__(self, nums: List[int]):
        """
        The first thing to do is to iterate through the nums then adding the previous index-value to the current
        index-value and making the current index value to the sum of both those numbers.
        """ 
        for index in range (1, len(nums)):
            nums[index] += nums[index - 1]
        
        #Make the passed nums equal to the class variable scope
        self.numberArray = nums

    def sumRange(self, left: int, right: int) -> int:
        #If the left equals 0 just return the number on the index right
        if left == 0:
            return self.numberArray[right]
        
        #Otherwise just return the index right minus index left - 1
        return self.numberArray[right] - self.numberArray[left - 1]
     
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

if __name__ == "__main__":
    rangeSum = NumArray([-2, 0, 3, -5, 2, -1])
    print(rangeSum.sumRange(0, 2))
    print(rangeSum.sumRange(2, 5))
    print(rangeSum.sumRange(0, 5))
    