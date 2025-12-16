def findMaxLength(nums: list[int]) -> int:
    #Problem #525 Contiguous Array - Medium - Solution Concept by YouTube Channel Cracking FAANG - Understanding the Solution

    countOffset = 0
    offsetDictionary = {0: -1}
    maxLength = 0
    
    for index, number in enumerate(nums):
        if number == 1:
            countOffset += 1
        else:
            countOffset -= 1
        
        if countOffset == 0:
            maxLength = index + 1
        elif countOffset in offsetDictionary:
            maxLength = max(maxLength, index - offsetDictionary[countOffset])
            continue    
            
        offsetDictionary[countOffset] = index
    
    return maxLength
        
def prefixSum(numbers: list[int]):
    for i in range(1, len(numbers)):
            numbers[i] += numbers[i - 1]

class NumArray:
    #Problem #303 Range Sum Query - Immutable - Easy
    
    def __init__(self, nums: list[int]):
        """
        The first step is to iterate through the nums starting at index 1, whilst iterating, add the previous index-value to the 
        current index-value, and let the current index value equal the sum of both those integers.
        """
        for index in range (1, len(nums)):
            nums[index] += nums[index - 1]
        
        #Make the passed nums equal to the class variable scope.
        self.numberArray = nums

    def sumRange(self, left: int, right: int) -> int:
        #If the left equals 0, just return the number at the index right.
        if left == 0:
            return self.numberArray[right]
        
        #Otherwise, just return the index right minus index left - 1.
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
    # nums = [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
    
    nums = [0, 0, 1, 0, 0, 0, 1, 1]
    
    print(findMaxLength(nums))