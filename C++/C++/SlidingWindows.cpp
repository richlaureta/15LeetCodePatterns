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
    string vowels = "aeiou";
    int count = 0;
    
    for(int i = 0; i < k; i++)
    {
        if(vowels.find(s[i]) != std::string::npos)
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
        if(vowels.find(s[left]) != std::string::npos)
        {
            count--;
        }
        
        if(vowels.find(s[i]) != std::string::npos)
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
