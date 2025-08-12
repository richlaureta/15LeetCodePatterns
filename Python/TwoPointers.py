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

def twoSum2(numbers: list[int], target: int) -> list[int]:
    startIndex = 0
    endIndex = len(numbers) - 1

    while startIndex < endIndex:
        if (numbers[startIndex] + numbers[endIndex]) == target:
            return [startIndex + 1, endIndex + 1]
        elif numbers[startIndex] + numbers[endIndex] > target:
            endIndex -= 1
        else: 
            startIndex += 1

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
    # numbers = [2, 7, 11, 15]
    # target = 9

    # print(twoSum2(numbers, target))

    # nums = [-1, 0, 1, 2, -1, -1, -4]

    # print(threeSum(nums))

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(maxArea(height))