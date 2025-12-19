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
    
    maxWaterSquare = 0
    leftIndex = 0
    rightIndex = len(height) - 1

    while leftIndex < rightIndex:
        minimum = min(height[leftIndex], height[rightIndex])
        square = minimum * (rightIndex - leftIndex)

        if square > maxWaterSquare:
            maxWaterSquare = square
        
        if height[leftIndex] > height[rightIndex]:
            rightIndex -= 1
        elif height[leftIndex] < height[rightIndex]:
            leftIndex += 1
        else:
            leftIndex += 1
    
    return maxWaterSquare
            
        
if __name__ == "__main__":
    nums = [0, 0, 0]
    
    print(threeSum(nums))