//
//  PrefixSum.cpp
//  C++
//
//  Created by Richmond Laureta on 8/6/25.
//

#include "Header.h"

int findMaxLength(vector<int> &nums)
{
    //Problem #525 Contiguous Array - Medium - Solution Concept by YouTube Channel Cracking FAANG - Understanding the Solution

    int countOffset = 0;
    unordered_map<int, int> offsetMap = {{0, -1}};
    
    int maxLength = 0;
    
    for(int i = 0; i < nums.size(); i++)
    {
        if(nums[i] == 0) countOffset--;
    
        else countOffset++;
        
        if(countOffset == 0)
        {
            maxLength = i + 1;
        }
        else if(offsetMap.find(countOffset) != offsetMap.end())
        {
            maxLength = max(maxLength, i - offsetMap[countOffset]);
            continue;
        }
        
        offsetMap[countOffset] = i;
    }
    
    return maxLength;
}

int subArraySum(vector<int> &nums, int k)
{
    //Problem #560 Subarray Sum Equals K - Needs to revisit this for clarification
    
    //Solution Concept by Youtuber "NeetCodeIO"
    int result = 0;
    int currentSum = 0;
    int difference = 0;
    unordered_map<int, int> myMap;
    myMap[0] = 1;
    
    for(int i = 0; i < nums.size(); ++i)
    {
        currentSum += nums[i];
        difference = currentSum - k;
        
        if(myMap.count(difference) > 0)
        {
            result += myMap[difference];
        }
        
        myMap[currentSum] += 1;
        
        if(myMap.count(currentSum) > 0)
        {
            myMap[currentSum] = myMap[currentSum];
        }
    }
    return result;
}

NumArray::NumArray(vector<int> &nums)
{
    //Problem #303 Range Sum Query - Easy
    
    /*
     The first step is to iterate through the nums starting at index 1, whilst iterating,
     add the previous index-value to the current index-value, and let the current index value
     equal the sum of both those integers.
     */
    for(int i = 1; i < nums.size(); i++)
    {
        nums[i] += nums[i - 1];
    }
    
    //Make the passed nums equal to the class variable scope.
    prefixSumArray = nums;
}

int NumArray::sumRange(int leftPointer, int rightPointer)
{
    //Problem #303 Range Sum Query - Easy
    
    //If the left equals 0, just return the number at the index right.
    if(leftPointer == 0) return prefixSumArray.at(rightPointer);
    
    //Otherwise, just return the index right minus index left - 1.
    return prefixSumArray.at(rightPointer) - prefixSumArray.at(leftPointer - 1);
}
