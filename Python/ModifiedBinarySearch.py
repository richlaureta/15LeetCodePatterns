def search(nums: list[int], target: int) -> int:
    #Problem #33 Search in Rotated Sorted Array - Medium
    
    leftIndex = 0
    rightIndex = len(nums) - 1
    
    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex)//2
        
        if nums[middleIndex] == target:
            return middleIndex
        elif nums[leftIndex] == target:
            return leftIndex
        elif nums[rightIndex] == target:
            return rightIndex
        
        if nums[middleIndex] > nums[leftIndex]:
            if target > nums[leftIndex] and target < nums[middleIndex]:
                rightIndex = middleIndex - 1
            else:
                leftIndex = middleIndex + 1
        else:
            if target > nums[middleIndex] and target < nums[rightIndex]:
                leftIndex = middleIndex + 1
            else:
                rightIndex = middleIndex - 1

    return -1

def findMin(nums: list[int]) -> int:
    #Problem #153 Find minimum in Rotated Sorted Array - Medium

    leftIndex = 0
    rightIndex = len(nums) - 1
    
    while leftIndex < rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex)//2
        
        if nums[leftIndex] < nums[rightIndex]:
            return nums[leftIndex]
        
        if nums[middleIndex - 1] > nums[middleIndex]:
            return nums[middleIndex]
        
        if nums[leftIndex] < nums[middleIndex]:
            if nums[middleIndex] > nums[middleIndex + 1]:
                return nums[middleIndex + 1]
            else:
                leftIndex = middleIndex + 1
        else:
            if nums[middleIndex] > nums[middleIndex + 1]:
                return nums[middleIndex + 1]
            else:
                rightIndex = middleIndex - 1
    
    return nums[leftIndex]

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    #Problem # 240 Search a 2D Matrix II - Medium
    
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
    nums = [3, 1, 2]
     
    print(findMin(nums))