from typing import List
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
    if len(matrix) == 1:
        leftIndex = 0
        rightIndex = len(matrix[0]) - 1
        
        while leftIndex <= rightIndex:
            middleIndex = leftIndex + (rightIndex - leftIndex)//2
            
            if matrix[0][middleIndex] == target:
                return True
            elif matrix[0][leftIndex] == target:
                return True
            elif matrix[0][rightIndex] == target:
                return True
            
            if matrix[0][middleIndex] > matrix[0][leftIndex]:
                if target > matrix[0][leftIndex] and target < matrix[0][middleIndex]:
                    rightIndex = middleIndex - 1
                else:
                    leftIndex = middleIndex + 1
            else:
                if target > matrix[0][middleIndex] and target < matrix[0][rightIndex]:
                    leftIndex = middleIndex + 1
                else:
                    rightIndex = middleIndex - 1

        return False
    
    if len(matrix[0]) == 1:
        leftIndex = 0
        rightIndex = len(matrix) - 1
        
        while leftIndex <= rightIndex:
            middleIndex = leftIndex + (rightIndex - leftIndex)//2
            
            if matrix[middleIndex][0] == target:
                return True
            elif matrix[leftIndex][0] == target:
                return True
            elif matrix[rightIndex][0] == target:
                return True
            
            if matrix[middleIndex][0] > matrix[leftIndex][0]:
                if target > matrix[leftIndex][0] and target < matrix[middleIndex][0]:
                    rightIndex = middleIndex - 1
                else:
                    leftIndex = middleIndex + 1
            else:
                if target > matrix[middleIndex][0] and target < matrix[rightIndex][0]:
                    leftIndex = middleIndex + 1
                else:
                    rightIndex = middleIndex - 1

        return False
    
    upRow = 0
    leftColumn = 0
    bottomRow = len(matrix) - 1
    rightColumn = len(matrix[0]) - 1
    
    while leftColumn < len(matrix[0]) and bottomRow > -1 and upRow < len(matrix) and matrix[bottomRow][rightColumn] >= target: 
        midRow = upRow + (bottomRow - upRow)//2
        midColumn = leftColumn + (rightColumn - leftColumn)//2
        
        if matrix[midRow][midColumn] == target:
            return True
        elif matrix[upRow][leftColumn] == target:
            return True
        elif matrix[bottomRow][rightColumn] == target:
            return True
        
        if matrix[midRow][midColumn] > target:
            bottomRow = midRow - 1
            rightColumn = midColumn - 1
        else:
            upRow = midRow + 1
            leftColumn = midColumn + 1
    
    row = bottomRow + 1
    column = rightColumn + 1
        
    for index0 in range(row, len(matrix)):
        if matrix[index0][0] > target:
            break
        for index1 in range(0, len(matrix[0])):
            if matrix[index0][index1] > target:
                break
            
            if matrix[index0][index1] == target:
                return True

    for index2 in range(column, len(matrix[0])):
        if matrix[0][index2] > target:
            break
        for index3 in range(0, len(matrix)):
            if matrix[index3][index2] > target:
                break
            
            if matrix[index3][index2] == target:
                return True

    return False
            
if __name__ == "__main__":
    # nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    nums = [[1], [2], [3], [4], [5]]
    target = 4
    print(searchMatrix(nums, target))