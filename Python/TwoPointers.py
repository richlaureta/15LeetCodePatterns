def threeSum(nums: list[int]) -> list[list[int]]:
    #Problem #15 3Sum - Medium
    
    nums.sort()
    threeSumArray = []
        
    for index in range(0, len(nums)):
        if index > 0 and nums[index] == nums[index - 1]:
            continue
            
        leftPointer = index + 1
        rightPointer = len(nums) - 1
            
        while leftPointer < rightPointer: 
            totalSum = nums[index] + nums[leftPointer] + nums[rightPointer]
                
            if totalSum == 0:
                threeSumArray.append([nums[index], nums[leftPointer], nums[rightPointer]])
                leftPointer += 1
                while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                    leftPointer += 1
            elif totalSum < 0:
                leftPointer += 1
            else:
                rightPointer -= 1
            
        return threeSumArray
        
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