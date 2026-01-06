//
//  TwoPointers.cpp
//  C++
//
//  Created by Richmond Laureta on 7/25/25.
//

#include "Header.h"

vector<int> pivotArray(vector<int> &nums, int pivot)
{
    //Problem #2161 Partition Array According to Given Plot - Medium
    
    vector<int> lessThanPivot = {};
    vector<int> greaterThanPivot = {};
    
    int pivotCounts = 0;
    
    for(int number: nums)
    {
        if(number < pivot) lessThanPivot.push_back(number);
        else if(number > pivot) greaterThanPivot.push_back(number);
        else pivotCounts++;
    }
    
    for(int i = 0; i < pivotCounts; i++)
    {
        lessThanPivot.push_back(pivot);
    }
    
    for(int number: greaterThanPivot)
    {
        lessThanPivot.push_back(number);
    }
    
    return lessThanPivot;
}

string reversePrefix0(string s, int k)
{
    string reversedString = "";
    
    for(int index = k - 1; index > -1; index--)
    {
        reversedString += s[index];
    }
    
    for(int index = k; index < s.size(); index++)
    {
        reversedString += s[index];
    }
    
    return reversedString;
}

string reversePrefix(string word, char ch)
{
    //Problem #2000 Reverse Prefix of Word - Easy
    
    int foundIndex = -1;
    
    for(int index = 0; index < word.size(); index++)
    {
        if(word[index] == ch)
        {
            foundIndex = index;
            break;
        }
    }
    
    if(foundIndex == -1) return word;
    
    string reversedStringIndex = "";
    
    for(int index = foundIndex; index > -1; index--)
    {
        reversedStringIndex += word[index];
    }
    
    for(int index = foundIndex + 1; index < word.size(); index++)
    {
        reversedStringIndex += word[index];
    }
    
    return reversedStringIndex;
}

int countPairs(vector<int> &nums, int target)
{
    //Problem #2824 Count Pairs Whose Sum is Less than Target - Easy - Learning from a Submitted Solution
    
    sort(nums.begin(), nums.end());
    
    int leftPointer = 0;
    int rightPointer = (int) nums.size() - 1;
    int pairCount = 0;
    
    while(leftPointer < rightPointer)
    {
        if(nums[leftPointer] + nums[rightPointer] < target)
        {
            pairCount += (rightPointer - leftPointer);
            leftPointer++;
        }
        else rightPointer--;
    }
    
    return pairCount;
}
vector<int> runningSum(vector<int> &nums)
{
    //Problem #1480 Running Sum 1d Array - Easy
    
    for(int i = 1; i < nums.size(); i++)
    {
        nums[i] += nums[i - 1];
    }
    
    return nums;
}

vector<int> twoSum2(vector<int>& numbers, int target)
{
    // Problem #167 Two Sum II - Input Array is Sorted - Medium
    
    //Start by setting the leftPointer to 0. O(1) space.
    int leftPointer = 0;
    //Let rightPointer equal the vector size - 1. O(1) space.
    int rightPointer = (int)numbers.size() - 1;
    
    //Initialize a while loop, whilst leftPointer is less than rightPointer. O(n - 1) time complexity.
    while (leftPointer < rightPointer)
    {
        //If numbers[leftPointer] + numbers[rightPointer] equals the target. Return the array [leftPointer + 1, rightPointer +  1].
        if(numbers[leftPointer] + numbers[rightPointer] == target) return {++leftPointer, ++rightPointer};
        //If numbers[leftPointer] + numbers[rightPointer] is less than the target, increment the leftPointer by 1.
        else if (numbers[leftPointer] + numbers[rightPointer] < target) leftPointer++;
        //If numbers[leftPointer] + numbers[rightPointer] is greater than the target, decrement the rightPointer by 1.
        else rightPointer--;
    }
    
    return {};
}

vector<vector<int>> threeSum(vector<int> &nums)
{
    //Problem #15 3Sum - Medium
    
    //Sort the array. O(n log n) time complexity.
    sort(nums.begin(), nums.end());
    //Create a storage for the triplets array. O(1) space.
    vector<vector<int>> threeSumArray;
    
    //#Iterate through the nums vector. O(n) time complexity.
    for(int i = 0; i < nums.size(); i++)
    {
        //If the index is greater than 0 and nums[index] is equal to the previous nums, continue.
        if((i > 0) and (nums[i] == nums[i - 1]))
        {
            continue;
        }
        
        //Initialize the leftPointer to index + 1.
        int leftPointer = i + 1;
        //Initialize the rightPointer to the length of nums - 1.
        int rightPointer = (int)nums.size() - 1;
        
        //Initialize a while loop, whilst leftPointer is less than rightPointer. O(n) time complexity.
        while(leftPointer < rightPointer)
        {
            //Initialize a totalSum variable equal to nums[index] + nums[leftPointer] + nums[rightPointer].
            int totalSum = nums[i] + nums[leftPointer] + nums[rightPointer];
            
            //If totalSum equals 0, append the triplets [nums[index], nums[leftPointer], nums[rightPointer].
            if(totalSum == 0)
            {
                threeSumArray.push_back({nums[i], nums[leftPointer], nums[rightPointer]});
                //#Increment the leftPointer by 1.
                leftPointer++;
                //Initialize a while loop with the condition leftPointer is less than rightPointer,
                //and when nums[leftPointer] equals nums[leftPointer - 1].
                while((leftPointer < rightPointer) and (nums[leftPointer] == nums[leftPointer - 1]))
                {
                    //Increment leftPointer by 1.
                    leftPointer++;
                }
            }
            else if(totalSum < 0)
            {
                //If totalSum is less than 0, increment the leftPointer by 1.
                leftPointer++;
            }
            //If totalSum is more than 0, decrement the rightPointer by 1.
            else rightPointer--;
        }
    }
    
    //Return threeSumArray
    return threeSumArray;
}

int maxArea(vector<int> &height)
{
    //Problem #11 Container With The Most Water - Medium
    
    //Initialize a leftPointer variable to zero index. O(1) space.
    int leftPointer = 0;
    //Initialize a rightPointer variable to equal the length of the height array minus - 1.  O(1) space.
    int rightPointer = (int) height.size() - 1;
    
    //Initialize a variable to store the maximum square value. O(1) space.
    int maxSquareArea = 0;
    
    //Iterate with the while loop with the condition leftPointer is less than rightPointer. O(n - 1) time complexity.
    while(leftPointer < rightPointer)
    {
        /*
        Calculate the max between the max area now, and the minimum between the leftPointer and
        # rightPointer index-value multiplied with distance (rightPointer - leftPointer),
        # and let that equal the variable maxSquareArea.
        */
        maxSquareArea = max(maxSquareArea, min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer));
        
        //If height[leftPointer] is less than height[rightPointer], then increment leftPointer by 1.
        if(height[leftPointer] < height[rightPointer]) leftPointer++;
        //Otherwise, decrement rightPointer by 1.
        else rightPointer--;
    }
    
    //Return the maxSquareArea.
    return maxSquareArea;
}
