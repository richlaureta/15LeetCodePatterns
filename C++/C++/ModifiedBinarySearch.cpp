//
//  ModifiedBinarySearch.cpp
//  C++
//
//  Created by Richmond Laureta on 9/11/25.
//

#include "Header.h"

int modifiedBinarySearch(vector<int> &nums, int target)
{
    //Problem #33 Search in Rotated Sorted Array - Medium
    
    int leftIndex = 0, rightIndex = (int)nums.size() - 1;
    
    while(leftIndex <= rightIndex)
    {
        int middleIndex = leftIndex + (rightIndex - leftIndex)/2;
        
        if(nums[middleIndex] == target) return middleIndex;
        else if(nums[leftIndex] == target) return leftIndex;
        else if(nums[rightIndex] == target) return rightIndex;
        
        if(nums[middleIndex] > nums[leftIndex])
        {
            if(target > nums[leftIndex] and target < nums[middleIndex]) rightIndex = middleIndex - 1;
            else leftIndex = middleIndex + 1;
        }
        else
        {
            if(target > nums[middleIndex] and target < nums[rightIndex]) leftIndex = middleIndex + 1;
            else rightIndex = middleIndex - 1;
        }
    }
    
    return -1;
}

int findMin(vector<int> &nums)
{
    //Problem #153 Find Minimum in Rotated Sorted Array - Medium
    
    int leftIndex = 0;
    int rightIndex = (int)nums.size() - 1;

    while (leftIndex < rightIndex) {
        int middleIndex = leftIndex + (rightIndex - leftIndex) / 2;

        if (nums[leftIndex] < nums[rightIndex])
            return nums[leftIndex];

        if (middleIndex - 1 > -1 and nums[middleIndex - 1] > nums[middleIndex])
            return nums[middleIndex];

        if (nums[leftIndex] < nums[middleIndex]) {
            if (nums[middleIndex] > nums[middleIndex + 1])
                return nums[middleIndex + 1];
            else
                leftIndex = middleIndex + 1;
        } else {
            if (nums[middleIndex] > nums[middleIndex + 1])
                return nums[middleIndex + 1];
            else
                rightIndex = middleIndex - 1;
        }
    }

    return nums[leftIndex];
}

bool searchMatrix(vector<vector<int>> &matrix, int target)
{
    //Problem #240 Search a 2D Matrix II - Medium
    
    int row = 0;
    int column = 0;
    
    while(row < (int)matrix.size() and column < (int)matrix[0].size())
    {
        if(matrix[row][column] == target) return true;
        else if(matrix[row][column] < target)
        {
            row++;
            column++;
        }
        else break;
    }
    
    for(int index0 = row; index0 < (int)matrix.size(); index0++)
    {
        if(matrix[index0][0] > target) break;
        
        for(int index1 = 0; index1 < (int)matrix[0].size(); index1++)
        {
            if(matrix[index0][index1] > target) break;
            else if(matrix[index0][index1] == target) return true;
        }
    }
    
    for(int index2 = column; index2 < (int)matrix[0].size(); index2++)
    {
        if(matrix[0][index2] > target) break;
        
        for(int index3 = 0; index3 < (int)matrix.size(); index3++)
        {
            if(matrix[index3][index2] > target) break;
            else if(matrix[index3][index2] == target) return true;
        }
    }
    
    return false;
}
