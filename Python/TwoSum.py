def twoSum(nums: list[int], target: int) -> list[int]:
    #Problem #1 Two Sum - Easy
    numberDictionary = {}
    
    for index, number in enumerate(nums):
        difference = target - number
        if difference in numberDictionary:
            return [numberDictionary[difference], index]
        
        numberDictionary[number] = index

def twoSumII(numbers: list[int], target: int) -> list[int]:
    #Problem #167 Two Sum II - Input Array Is Sorted - Medium
    
    leftPointer = 0
    rightPointer = len(nums) - 1
    
    while(leftPointer < rightPointer):
        totalSum = numbers[leftPointer] + numbers[rightPointer]
        
        if totalSum > target:
            rightPointer -= 1
        elif totalSum < target:
            leftPointer += 1
        else:
            return [leftPointer + 1, rightPointer + 1]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSumII(nums, target))