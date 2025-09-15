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
