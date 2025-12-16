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
    
    //Initialize the offset variable. We will add 1 if it is a 1 and will subtract 1 if it is a zero.
    int countOffset = 0;
    //Initialize an unordered map to store the offset value paired with the index.
    //We will start with the imaginary index -1 to store the 0 count offset.
    unordered_map<int, int> offsetMap = {{0, -1}};
    //Initialize a variable to count the maximum length of equal 0’s and 1’s.
    int maxLength = 0;
    
    //Iterate through the nums.
    for(int i = 0; i < nums.size(); i++)
    {
        //If the nums[i] is 1, add 1 to countOffset.
        if(nums[i] == 0) countOffset--;
        //If nums[i] is 0, subtract 1 from countOffset.
        else countOffset++;
        
        //If countOffset becomes 0, let maxLength equal the index + 1.
        if(countOffset == 0)
        {
            maxLength = i + 1;
        }
        //If countOffset is in the dictionary, get the maximum between maxLength and index minus
        //the offsetDictionary[countOffset], and continue.
        else if(offsetMap.find(countOffset) != offsetMap.end())
        {
            maxLength = max(maxLength, i - offsetMap[countOffset]);
            continue;
        }
        
        //Store the countOffset as the key and let that equal the index.
        offsetMap[countOffset] = i;
    }
    
    //Return the maxLength.
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
