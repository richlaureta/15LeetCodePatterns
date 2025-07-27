//
//  TwoPointers.cpp
//  C++
//
//  Created by Richmond Laureta on 7/25/25.
//

#include "Header.h"

vector<int> twoSum2(vector<int>& nums, int target)
{
    // Problem #167 Two Sum II - Input Array is Sorted
    
    int startIndex = 0;
    int endIndex = int(nums.size() - 1);
    
    while(startIndex < endIndex)
    {
        if((nums[startIndex] + nums[endIndex]) > target)
        {
            endIndex--;
        }
        else if((nums[startIndex] + nums[endIndex]) < target)
        {
            startIndex++;
        }
        else
        {
            return {++startIndex, ++endIndex};
        }
    }
    
    return {};
}
