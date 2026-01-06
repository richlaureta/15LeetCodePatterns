def pivotArray(nums: list[int], pivot: int) -> list[int]:
    #Problem #2161 Partition Array According to Given Pivot - Medium
    
    lessThanPivot = []
    equalsPivot = []
    greaterThanPivot = []
    
    for index in range(0, len(nums)):
        if nums[index] < pivot:
            lessThanPivot.append(nums[index])
        elif nums[index] > pivot:
            greaterThanPivot.append(nums[index])
        else:
            equalsPivot.append(nums[index])
            
    return lessThanPivot + equalsPivot + greaterThanPivot

def reversePrefix0(s: str, k:int ) -> str:
    #Problem #3794 String Prefix - Easy
    
    reversedString = ""
    for index in range(k - 1, -1, -1):
        reversedString += s[index]
    
    for index in range(k, len(s)):
        reversedString += s[index]
    
    return reversedString

def reversePrefix(word: str, ch: str) -> str:
    #Problem #2000 Reverse Prefix of Word - Easy
    
    foundIndex = -1
    for index in range(0, len(word)):
        if word[index] == ch:
            foundIndex = index
            break
    
    if foundIndex == -1:
        return word
    
    stringReverseIndex = ""
    
    for index in range(foundIndex, -1, -1):
        stringReverseIndex += word[index]
    
    for index in range(foundIndex + 1, len(word)):
        stringReverseIndex += word[index]
    
    return stringReverseIndex
    
def isStrictlyPalindromic(n: int) -> bool:
    #Problem #2396 Strictly Palindromic Number - Medium
    pass
def countPairs(nums: list[int], target: int) -> int:
    #Problem #2824 Count Pairs Whose Sum is Less Than Target - Easy - Learning from a Submitted Solution
    nums.sort()
    
    leftPointer = 0
    rightPointer = len(nums) - 1
    pairCount = 0
    
    while leftPointer < rightPointer:
        if nums[leftPointer] + nums[rightPointer] < target:
            pairCount += rightPointer - leftPointer
            leftPointer += 1
        else:
            rightPointer -= 1
    return pairCount

def threeSum(nums: list[int]) -> list[list[int]]:
    #Problem #15 3Sum - Medium 
    
    #Sort the array. O(n log n) time complexity.
    nums.sort()
    #Create a storage for the triplets array. O(1) space.
    threeSumArray = []

    #Iterate through the nums array. O(n) time complexity.
    for index in range(0, len(nums)):
        #If the index is greater than 0 and nums[index] is equal to the previous nums, continue.
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        
        #Initialize the leftPointer to index + 1.
        leftPointer = index + 1
        #Initialize the rightPointer to the length of nums - 1.
        rightPointer = len(nums) - 1
        
        #Initialize a while loop, whilst leftPointer is less than rightPointer. O(n) time complexity.
        while leftPointer < rightPointer:
            #Initialize a totalSum variable equal to nums[index] + nums[leftPointer] + nums[rightPointer]. 
            totalSum = nums[index] + nums[leftPointer] + nums[rightPointer]
            
            #If totalSum equals 0, append the triplets [nums[index], nums[leftPointer], nums[rightPointer].    
            if totalSum == 0:
                threeSumArray.append([nums[index], nums[leftPointer], nums[rightPointer]])
                #Increment the leftPointer by 1.
                leftPointer += 1
                
                #Initialize a while loop with the condition leftPointer is less than rightPointer, 
                #and when nums[leftPointer] equals nums[leftPointer - 1].
                while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                    #Increment leftPointer by 1.
                    leftPointer += 1
            #If totalSum is less than 0, increment the leftPointer by 1.
            elif totalSum < 0:
                leftPointer += 1
            #If totalSum is more than 0, decrement the rightPointer by 1.
            else:
                rightPointer -= 1
    
    #Return threeSumArray    
    return threeSumArray 
                   
def twoSum(numbers: list[int], target: int) -> list[int]:
    #Problem #167 Two Sum II - Input Array Is Sorted - Medium
    
    #Start by setting the leftPointer to 0. O(1) space.
    leftPointer = 0
    #Let rightPointer equal the array size - 1. O(1) space.
    rightPointer = len(numbers) - 1
     
    #Initialize a while loop, whilst leftPointer is less than rightPointer. O(n - 1) time complexity.   
    while leftPointer < rightPointer:
        #If numbers[leftPointer] + numbers[rightPointer] equals the target.
        if numbers[leftPointer] + numbers[rightPointer] == target:
            return [leftPointer + 1, rightPointer + 1]
        #If numbers[leftPointer] + numbers[rightPointer] is less than the target, increment the leftPointer by 1.
        elif numbers[leftPointer] + numbers[rightPointer] < target:
            leftPointer += 1
        #If numbers[leftPointer] + numbers[rightPointer] is greater than the target, decrement the rightPointer by 1.
        else:
            rightPointer -= 1
    
def maxArea(height: list[int]) -> int:
    #Problem #11 Container with the Most Water - Medium
    
    #Initialize a leftPointer variable to zero index. O(1) space.
    leftPointer = 0
    #Initialize a rightPointer variable to equal the length of the height array minus - 1.  O(1) space.
    rightPointer = len(height) - 1
    
    #Initialize a variable to store the maximum square value. O(1) space.
    maxSquareArea = 0
    
    #Iterate with the while loop with the condition leftPointer is less than rightPointer. O(n - 1) time complexity. 
    while leftPointer < rightPointer:
        #Calculate the max between the max area now, and the minimum between the leftPointer and 
        # rightPointer index-value multiplied with distance (rightPointer - leftPointer), 
        # and let that equal the variable maxSquareArea.
        maxSquareArea = max(maxSquareArea, min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer))
        
        #If height[leftPointer] is less than height[rightPointer], then increment leftPointer by 1.
        if height[leftPointer] < height[rightPointer]:
            leftPointer += 1
        #Otherwise, decrement rightPointer by 1.
        else:
            rightPointer -= 1
    
    #Return the maxSquareArea.
    return maxSquareArea

def isPalindrome(s: str) -> bool:
    #Problem #125 Valid Palindrome - Easy
    
    alphaNumericString = ''.join(filter(str.isalnum, s)).lower()
    
    return alphaNumericString == alphaNumericString[::-1]
  
if __name__ == "__main__":
    nums = [-3, 4, 3, 2]
    pivot = 2
    
    print(pivotArray(nums, pivot))