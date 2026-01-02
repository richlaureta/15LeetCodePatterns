//
//  PrefixSum.cpp
//  C++
//
//  Created by Richmond Laureta on 8/6/25.
//

#include "Header.h"

int garbageCollection(vector<string> &garbage, vector<int> &travel)
{
    //Problem #2391 Minimum Amount of Time to Collect Garbage - Medium
    
    int totalMinutesCount = 0;
    
    bool M = false;
    bool P = false;
    bool G = false;
    
    for(int index = (int) garbage.size() - 1; index > -1; index--)
    {
        totalMinutesCount += garbage[index].size();
        
        if((garbage[index].find('M') != string::npos) and (M == false))
        {
            M = true;
            for(int i = 0; i < index; i++)
            {
                totalMinutesCount += travel[i];
            }
        }
        
        if((garbage[index].find('P') != string::npos) and (P == false))
        {
            P = true;
            for(int i = 0; i < index; i++)
            {
                totalMinutesCount += travel[i];
            }
        }
        
        if((garbage[index].find('G') != string::npos) and (G == false))
        {
            G = true;
            for(int i = 0; i < index; i++)
            {
                totalMinutesCount += travel[i];
            }
        }
    }
    
    return totalMinutesCount;
}

int subArray(vector<int> &nums)
{
    //Problem #3427 Sum of Variable Length Subarrays - Easy
    
    vector<int> numsCopy = nums;
    for(int index = 1; index < nums.size(); index++)
    {
        numsCopy[index] += numsCopy[index - 1];
    }
    
    int totalSum = 0;
    
    for(int index = 0; index < nums.size(); index++)
    {
        int start = max(0, index - nums[index]);
        
        if(start > 0) totalSum += numsCopy[index] - numsCopy[start - 1];
        else totalSum += numsCopy[index];
    }
    
    return totalSum;
}

vector<int> minOperations(string boxes)
{
    //Problem #1769 Minimum Number of Operations to Move All Balls to Each Box - Medium
    
    vector<int> operationsCountArray(boxes.size());
    
    for(int i = 0; i < boxes.size(); i++)
    {
        if(boxes[i] == '1')
        {
            for(int j = 0; j < operationsCountArray.size(); j++)
            {
                operationsCountArray[j] += abs(j - i);
            }
        }
    }
    
    return operationsCountArray;
}

int countPartitions(vector<int> &nums)
{
    //Problem #3432 Count Partitions with Even Sum Difference - Easy
    
    int goingLeftSum = 0;
    int goingRightSum = accumulate(nums.begin(), nums.end(), 0);
    
    int partitionCount = 0;
    
    for(int index = 0; index < nums.size() - 1; index++)
    {
        goingRightSum -= nums[index];
        goingLeftSum += nums[index];
        
        if((goingLeftSum - goingRightSum) % 2 == 0) partitionCount++;
    }
    
    return partitionCount;
}

vector<int> leftRightDifference(vector<int> &nums)
{
    //Problem #2574 Left and Right Sum Differences - Easy - Learning from Submitted Solution
    
    int leftSum = 0;
    vector<int> leftRightSumDifference;
    int rightSum = accumulate(nums.begin(),nums.end(), 0);
    
    for(int i = 0; i < nums.size(); i++)
    {
        rightSum -= nums[i];
        if(i > 0) leftSum += nums[i - 1];
        leftRightSumDifference.push_back(abs(leftSum - rightSum));
    }
    
    return leftRightSumDifference;
}

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
    //Problem #560 Subarray Sum Equals K - Medium - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    //Start by creating a map to store the frequency of the sums. O(n) space.
    unordered_map<int, int> sumMap;
    //Initialize the key 0 to a frequency of 1 so that when you subtract the k with a difference of 0, you can add 1 to the
    //sumEqualsKCount.
    sumMap[0] = 1;
    
    //Create a variable that will return the count of sum(s) equal to k. O(1) space.
    int sumEqualsKCount = 0;
    //Create a variable for the sum. O(1) space.
    int currentSum = 0;
    
    //Iterate through the nums. O(n) time complexity.
    for(int number: nums)
    {
        //Add currentSum to the current number.
        currentSum += number;
        //Add sumEqualsKCount with the frequency of key, sum minus the difference.
        sumEqualsKCount += sumMap[currentSum - k];
        //Then store the sum key, then add 1 to its value.
        sumMap[currentSum] += 1;
    }
    
    //Return the count.
    return sumEqualsKCount;
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
