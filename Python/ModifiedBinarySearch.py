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
    
    for row in matrix:
        if row[len(row) - 1] < target:
            continue
        
        leftIndex = 0
        rightIndex = len(row) - 1
        while leftIndex <= rightIndex:
            middleIndex = leftIndex + (rightIndex - leftIndex)//2
            
            if row[middleIndex] == target:
                return True
            elif row[leftIndex] == target:
                return True
            elif row[rightIndex] == target:
                return True
            
            if row[middleIndex] > target:
                rightIndex = middleIndex - 1
            else:
                leftIndex = middleIndex + 1
                
    return False
            
if __name__ == "__main__":
    # nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
     
    print(searchMatrix(nums, target))