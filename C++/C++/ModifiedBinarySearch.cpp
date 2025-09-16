//
//  ModifiedBinarySearch.cpp
//  C++
//
//  Created by Richmond Laureta on 9/11/25.
//

#include "Header.h"

int modifiedBinarySearch(vector<int> &nums, int target)
{
    //Problem #33 Search in Rotated Sorted Array
    
    int leftIndex = 0;
    int rightIndex = (int) nums.size() - 1;
    
    while(leftIndex <= rightIndex)
    {
        int middleIndex = (leftIndex + rightIndex) / 2;
        
        if(nums[middleIndex] == target) return middleIndex;
        
        if(nums[leftIndex] <= nums[middleIndex])
        {
            if((target > nums[middleIndex]) or (target < nums[leftIndex])) leftIndex = middleIndex + 1;
            else rightIndex = middleIndex - 1;
        }
        else
        {
            if((target < nums[middleIndex]) or (target > nums[rightIndex])) rightIndex = middleIndex - 1;
            else leftIndex = middleIndex + 1;
        }
    }
    
    return -1;
}

int findMin(vector<int> &nums)
{
    //Problem #153 Find Minimum in Rotated Sorted Array
    
    int leftIndex = 0;
    int rightIndex = (int) nums.size() - 1;
    
    while(leftIndex < rightIndex)
    {
        int midIndex = (int)((leftIndex + rightIndex) / 2);
        
        if (nums[midIndex] > nums[rightIndex])
        {
            leftIndex = midIndex + 1;
        }
        
        if(nums[midIndex] < nums[rightIndex])
        {
            rightIndex = midIndex;
        }
    }
    
    return nums[rightIndex];
}

bool searchMatrix(vector<vector<int>> &matrix, int target)
{
    //Problem #240 Search a 2D Matrix II
    
    int row = (int)matrix.size() - 1;
    int column = 0;
    
    while(row > -1 and column < matrix[0].size())
    {
        if(matrix[row][column] == target) return true;
        
        if(matrix[row][column] > target) row--;
        else column++;
    }
    return false;
}
