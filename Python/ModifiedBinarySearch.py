def search(nums: list[int], target: int) -> int:
    #Problem #33 Search in Rotated Sorted Array 

    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex <= rightIndex:
        middleIndex = (leftIndex + rightIndex) // 2

        if nums[middleIndex] == target:
            return middleIndex

        if nums[leftIndex] <= nums[middleIndex]:
            if target > nums[middleIndex] or target < nums[leftIndex]:
                leftIndex = middleIndex + 1
            else:
                rightIndex = middleIndex - 1
        else:
            if target < nums[middleIndex] or target > nums[rightIndex]:
                rightIndex = middleIndex - 1
            else:
                leftIndex = middleIndex + 1
    
    return -1

def findMin(nums: list[int]) -> int:
    #Problem #153 Find minimum in Rotated Sorted Array
    
    leftIndex = 0
    rightIndex = len(nums) - 1

    if nums[leftIndex] < nums[rightIndex]:
        return nums[leftIndex]
    
    while leftIndex < rightIndex:
        middleIndex = (leftIndex + rightIndex) // 2

        if nums[middleIndex] > nums[rightIndex]:
            leftIndex = middleIndex + 1
        
        if nums[middleIndex] < nums[rightIndex]:
            rightIndex = middleIndex
        
    return nums[leftIndex]

if __name__ == "__main__":
   nums = [4, 5, 6, 7, 0, 1, 2]

   print(findMin(nums))