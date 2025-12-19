def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    answer = []
    leftIndex = 0
    rightIndex = 0
    sum = 0
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: #Help of Google CLI AI - debugged snippet code
            continue

        leftIndex = i + 1
        rightIndex = len(nums) - 1
        
        while leftIndex < rightIndex:
            sum = nums[i] +  nums[leftIndex] + nums[rightIndex]

            if sum == 0:
                answer.append([nums[i], nums[leftIndex], nums[rightIndex]])
                

                rightIndex -= 1
                while(leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex + 1]):
                    rightIndex -= 1

                leftIndex += 1
                while(leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex - 1]):
                    leftIndex += 1
                
            elif sum > 0:
                rightIndex -= 1
            else:
                leftIndex += 1
    return answer

def twoSum(numbers: list[int], target: int) -> list[int]:
    #Problem #167 Two Sum II - Input Array Is Sorted - Medium
    
    #Start by setting the leftPointer to 0. O(1) space.
    leftPointer = 0
    #Let rightPointer equal the size - 1. O(1) space.
    rightPointer = len(numbers) - 1
        
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
    #Problem #11 Container with the Most Water
    
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
    nums = [-1, 0]
    target = -1
    
    print(twoSum(nums, target))