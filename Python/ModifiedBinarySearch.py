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
    
    midIndex = (len(nums)) //2
    right = len(nums) - 1
    minimum = nums[midIndex]
    if nums[midIndex] > nums[right]:
        for i in range(midIndex + 1, len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
    else:
        for i in range(0, midIndex):
            if(nums[i] < minimum):
                minimum = nums[i]
    return minimum

if __name__ == "__main__":
   nums = [4, 5, 6, 7, 0, 1, 2]
   target = 0

   print(search(nums, target))