import sys

def search(nums: list[int], target: int) -> int:
    #Problem #33 Search in Rotated Sorted Array

    if len(nums) < 9:
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
        return -1

    midIndexL = len(nums) // 2
    midIndexR = len(nums) // 2
    evenOrOdd = 0
    if len(nums) % 2 != 0:
        evenOrOdd = 1

    for i in range(0, midIndexL + evenOrOdd):
        if nums[midIndexL] == target:
            return midIndexL
        else:
            midIndexL -= 1

        if nums[midIndexR] == target:
            return midIndexR
        else:
            midIndexR += 1
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
def main():
    # nums = [4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3]
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [1, 2, 3, -1, 0]
    # nums = [7,8,1,2,3,4,5,6]
    # nums = [1, 2, 3, 4, 5, 6]
    # nums = [11, 13, 15, 17]

    # nums = [3, 4, 5, 1, 2]
    print(findMin(nums))

if __name__ == "__main__":
    sys.exit(main())