//
//  MonotonicStack.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/9/25.
//

#include "Header.h"

std::vector<int> nextGreaterElement(std::vector<int> &nums1, std::vector<int> &nums2)
{
    
    std::stack<int> decreasingStack;
    std::vector<int> array;
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
