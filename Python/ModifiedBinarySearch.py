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

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    #Problem # 240 Search a 2D Matrix II
    
    row = len(matrix) - 1
    column = 0 

    while row > -1  and column < len(matrix[0]):
        if matrix[row][column] == target:
            return True
            
        if matrix[row][column] > target:
            row -= 1
        else: column += 1
        
    return False

if __name__ == "__main__":
#    matrix = [
#        [1, 4, 7, 11, 15], 
#        [2, 5, 8, 12, 19], 
#        [3, 6, 9, 16, 22], 
#        [10, 13, 14, 17, 24], 
#        [18, 21, 23, 26, 30]
#        ]
   matrix = [[-5]]
   target = -5

   print(searchMatrix(matrix, target))