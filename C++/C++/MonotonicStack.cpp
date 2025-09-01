//
//  MonotonicStack.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/9/25.
//

#include "Header.h"

vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
{
    
    stack<int> decreasingStack;
    vector<int> array;
    unordered_map<int, int> queryMap;
    
    int size = (int)nums2.size();
    
    for (int i = size - 1; i >= 0; --i)
    {
        while(!decreasingStack.empty() && nums2[i] > decreasingStack.top())
        {
            decreasingStack.pop();
        }
        
        if(!decreasingStack.empty() && nums2[i] < decreasingStack.top())
        {
            queryMap[nums2[i]] = decreasingStack.top();
        }
        else
        {
            queryMap[nums2[i]] = -1;
        }
        
        decreasingStack.push(nums2[i]);
        
    }
    
    for(int i = 0; i < nums1.size(); ++i)
    {
        array.push_back(queryMap[nums1[i]]);
    }
    
    return array;
}

vector<int> dailyTemperatures(vector<int> &temperatures)
{
    //Problem #739 Daily Temperatures
    
    vector<int> returnList(temperatures.size(), 0);
    stack<int> decreasingStack;
    
    for(int i = 0; i < temperatures.size(); ++i)
    {
        if(decreasingStack.size() == 0)
        {
            decreasingStack.push(i);
            continue;
        }
        
        while(temperatures[i] > temperatures[decreasingStack.top()])
        {
            int poppedIndex = decreasingStack.top();
            decreasingStack.pop();
            returnList[poppedIndex] = i - poppedIndex;
            
            if(decreasingStack.size() == 0)
            {
                decreasingStack.push(i);
                break;
            }
        }
        
        if (temperatures[i] <= temperatures[decreasingStack.top()])
        {
            decreasingStack.push(i);
        }
    }
    return returnList;
}
