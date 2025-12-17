def findMaxLength(nums: list[int]) -> int:
    #Problem #525 Contiguous Array - Medium - Solution Concept by YouTube Channel Cracking FAANG - Understanding the Solution

    #Initialize the offset variable. We will add 1 if it is a 1 and will subtract 1 if it is a zero. 
    # O(1) space complexity.
    countOffset = 0 
    #Initialize a dictionary to store the offset value paired with the index. 
    # We will start with the imaginary index -1 to store the 0 count offset.
    #O(n) space complexity.
    offsetDictionary = {0: -1}
    #Initialize a variable to count the maximum length of equal 0’s and 1’s.
    #O(1) space complexity.
    maxLength = 0
    
    #Iterate through the nums with enumerate.
    #O(n) time complexity.
    for index, number in enumerate(nums):
        #If the nums[i] is 1, add 1 to countOffset.
        if number == 1:
            countOffset += 1
        #If nums[i] is 0, subtract 1 from countOffset. 
        else:
            countOffset -= 1
        
        #If countOffset becomes 0, let maxLength equal the index + 1.
        if countOffset == 0:
            maxLength = index + 1
        
        #If countOffset is in the dictionary, get the maximum between maxLength and index minus 
        # the offsetDictionary[countOffset], and continue.
        elif countOffset in offsetDictionary:
            maxLength = max(maxLength, index - offsetDictionary[countOffset])
            continue    
         
        #Store the countOffset as the key and let that equal the index.   
        offsetDictionary[countOffset] = index
    
    #Return the maxLength.
    return maxLength
        
def prefixSum(numbers: list[int]):
    for i in range(1, len(numbers)):
            numbers[i] += numbers[i - 1]

class NumArray:
    #Problem #303 Range Sum Query - Immutable - Easy
    
    def __init__(self, nums: list[int]):
        """
        The first step is to iterate through the nums starting at index 1, whilst iterating, add the previous index-value to the 
        current index-value, and let the current index value equal the sum of both those integers. O(n) time complexity.
        """
        for index in range (1, len(nums)):
            nums[index] += nums[index - 1]
    
        #Make the passed nums equal to the class variable scope. O(n) space complexity.
        self.numberArray = nums

    def sumRange(self, left: int, right: int) -> int:
        #If the left equals 0, just return the number at the index right.
        if left == 0:
            return self.numberArray[right]
        
        #Otherwise, just return the index right minus index left - 1.
        return self.numberArray[right] - self.numberArray[left - 1]
     
def subArraySum(nums: list[int], k: int) ->int:
    #Problem #560 Subarray Sum Equals K - Medium
    
    sumEqualsKCount = 0
    sumSet = set()
    sumSet.add(nums[0])
    
    for index in range(1, len(nums)):
        if nums[index] == k:
            sumEqualsKCount += 1
        
        nums[index] += nums[index - 1]
        
        if nums[index] - k in sumSet:
            sumEqualsKCount += 1 
        
        sumSet.add(nums[index])
         
        if nums[index] == k:
            sumEqualsKCount += 1
    print(nums)    
    return sumEqualsKCount

if __name__ == "__main__":
    nums = [1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 3, -4]
    k = 3
    print(subArraySum(nums, k))