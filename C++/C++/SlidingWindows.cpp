//
//  SlidingWindows.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"

#include <iostream>
#include <vector>
#include <string>

using namespace std;

double findMaxAverage(vector<int> &nums, int k)
{
    //Problem #643 Maximum Average Subarray I
    
    double total = 0;
    size_t leftIndex = 0;
    double maxSum = 0;

    for (size_t i = 0; i < k; ++i)
    {
        total += nums[i];
    }

    maxSum = total;

    for (size_t i = k; i < nums.size(); ++i)
    {
        total += nums[i] - nums[leftIndex];
        leftIndex++;

        if (total > maxSum)
        {
            maxSum = total;
        }
    }

    return maxSum / k;
}

int maxVowels(string s, int k)
{
    //#Problem # 1456. Maximum Number of Vowels in a Substring of Given Length
    
    int count = 0;
    
    for(int i = 0; i < k; i++)
    {
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            count++;
        }
    }
    
    if(count == k)
    {
        return k;
    }
    
    int left = 0;
    int maxCount = count;
    
    for(int i = k; i < s.size(); i++)
    {
        if(s[left] == 'a' || s[left] == 'e' || s[left] == 'i' || s[left] == 'o' || s[left] == 'u')
        {
            count--;
        }
        
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            count++;
        }
        
        if(count == k){return k;}
        
        left++;
        if(count > maxCount)
        {
            maxCount = count;
        }
        
    }
    return maxCount;
}

int lengthOfLongestSubstring(string s)
{
    //Problem #3 Longest Substring Without Repeating Character
    
    unordered_map<int, int> myMap;
    int count = 0;
    int maxCount = 0;
    int pointer = 0;
    
    while(pointer != s.size())
    {
        if(myMap.count(s[pointer]) == 0)
        {
            myMap[s[pointer]] = pointer;
            count++;
            if(count > maxCount)
            {
                maxCount = count;
            }
        }
        else
        {
            count = 0;
            pointer = myMap[s[pointer]];
            myMap.clear();
        }
        
        pointer++;
    }
    
    return maxCount;
}
