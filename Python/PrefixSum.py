from collections import defaultdict

def garbageCollection(garbage: list[str], travel: list[int]) -> int:
    #Problem #2391 Minimum Amount of Time to Collect Garbage - Medium
    
    M = False
    P = False
    G = False
    
    totalMinutesCount = 0
    houseIndex = len(garbage) - 1
    
    for house in reversed(garbage):
        totalMinutesCount += len(house)
        if "M" in house and M == False:
            M = True
            totalMinutesCount += sum(travel[:houseIndex])
        
        if "P" in house and P == False:
            P = True
            totalMinutesCount += sum(travel[:houseIndex])
        
        if "G" in house and G == False:
            G = True
            totalMinutesCount += sum(travel[:houseIndex])
        
        houseIndex -= 1
        
    return totalMinutesCount
    
def subArray(nums: list[int]) -> int:
    #Problem #3427 Sum of Variable Length Subarrays - Easy
    
    for index in range(1, len(nums)):
        nums[index] = nums[index - 1] + nums[index]
    nums.append(0)
    totalSum = 0
    for index in range(0, len(nums) - 1):
        start = max(0, index - (nums[index] - nums[index - 1]))
        totalSum += nums[index]  - nums[start - 1]
            
    return totalSum

def minOperations(boxes: str) -> list[int]:
    #Problem #1769 Minimum Number of Operations to Move All Balls to Each Box - Medium
    
    operationsCountArray = [0] * len(boxes)
    
    for index in range(0, len(boxes)):
        if boxes[index] == '1':
            for index1 in range(0, len(boxes)):
                operationsCountArray[index1]  += abs(index1 - index)
                
    return operationsCountArray

def countPartitions(nums: list[int]) -> int:
    #Problem #3432 Count Partitions with Even Sum Difference - Easy
    
    goingLeftSum = 0
    goingRightSum = sum(nums)
    partitionCount = 0
    
    for index in range(0, len(nums)- 1):
        goingRightSum -= nums[index]
        goingLeftSum += nums[index]
        if (goingLeftSum - goingRightSum) % 2 == 0:
            partitionCount += 1

    return partitionCount

def leftRightDifference(nums: list[int]) -> list[int]:
    #Problem #2574 Left and Right Sum Differences - Easy - Learning from a submitted solution.
    
    leftSum = 0
    rightSum = sum(nums)
    rightSumDifference = []
    
    for index in range(len(nums)):
        rightSum -= nums[index]
        if index > 0:
            leftSum += nums[index - 1]
        rightSumDifference.append(abs(leftSum - rightSum))
          
    return rightSumDifference
        
def runningSum(nums: list[int]) -> list[int]:
    #Problem #1480 Running Sum of 1d Array - Easy
    
    for index in range(1, len(nums)):
        nums[index] += nums[index - 1]
    
    return nums
        

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
    #Problem #560 Subarray Sum Equals K - Medium - Solution Concept by YouTube Channel Deepti Talesra - 
    #Understanding the Solution
    
    #Start by creating a dictionary to store the frequency of the sums. O(n) space.
    sumDictionary = defaultdict(int)
    #nitialize the key 0 to a frequency of 1 so that when you 
    #subtract the k with a difference of 0, you can add 1 to the sumEqualsKCount.
    sumDictionary[0] = 1
    
    #Create a variable for the sum. O(1) space.
    currentSum = 0
    #Create a variable that will return the count of sum(s) equal to k. O(1) space.
    sumEqualsKCount = 0

    
    for number in nums:
        #Add currentSum to the current number.
        currentSum += number
        #Add sumEqualsKCount with the frequency of key, sum minus the difference.
        sumEqualsKCount += sumDictionary[currentSum - k]
        #Then store the sum key, then add 1 to its value.
        sumDictionary[currentSum] += 1

    #Return the count.
    return sumEqualsKCount

if __name__ == "__main__":
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]

    print(garbageCollection(garbage, travel))