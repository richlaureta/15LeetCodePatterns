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

vector<vector<int>> threeSum(vector<int> &nums)
{
    //Problem #15 3Sum
    
    sort(nums.begin(), nums.end());
    int leftIndex = 0;
    int rightIndex = 0;
    int sum = 0;
    vector<vector<int>> answer;
    
    for(int i = 0; i < nums.size(); i++)
    {
        if((i > 0) and (nums[i] == nums[i-1]))
        {
            continue;
        }
        
        leftIndex = i + 1;
        rightIndex = ((int)nums.size()) - 1;
        
        while(leftIndex < rightIndex)
        {
            sum = nums[i] + nums[leftIndex] + nums[rightIndex];
            
            if(sum > 0)
            {
                rightIndex--;
            }
            else if(sum < 0)
            {
                leftIndex++;
            }
            else
            {
                answer.push_back({nums[i], nums[leftIndex], nums[rightIndex]});
                
                leftIndex++;
                rightIndex--;

                while((leftIndex < rightIndex) and (nums[leftIndex] == nums[leftIndex - 1]))
                {
                    leftIndex++;
                }
                
                
                while((leftIndex < rightIndex) and (nums[rightIndex] == nums[rightIndex + 1]))
                {
                    rightIndex--;

                }
            }
        }
    }
    
    return answer;
}

int maxArea(vector<int> &height)
{
    //Problem #11 Container With The Most Water
    
    int maxArea = 0;
    int leftIndex = 0;
    int rightIndex = (int)(height.size() - 1);
    int minimum = 0;
    
    while(leftIndex < rightIndex)
    {
        if(height[leftIndex] < height[rightIndex])
        {
            minimum = height[leftIndex];
        }
        else if (height[leftIndex] > height[rightIndex])
        {
            minimum = height[rightIndex];
        }
        else
        {
            minimum = height[rightIndex];
        }
        
        int square = minimum * (rightIndex - leftIndex);
        
        if(square > maxArea)
        {
            maxArea = square;
        }
        
        if(height[leftIndex] > height[rightIndex])
        {
            rightIndex--;
        }
        else if (height[leftIndex] < height[rightIndex])
        {
            leftIndex++;
        }
        else
        {
            leftIndex++;
        }
    }
    
    return maxArea;
}
