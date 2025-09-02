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
    
    if(temperatures.size() != 0)
    {
        decreasingStack.push(0);
    }
    
    for(int i = 1; i < temperatures.size(); ++i)
    {
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
        
        if ((decreasingStack.size() != 0) and (temperatures[i] <= temperatures[decreasingStack.top()]))
        {
            decreasingStack.push(i);
        }
    }
    return returnList;
}

int largestRectangleArea(vector<int> &heights)
{
    //Problem #84 Largest Rectangle in Histogram - Concept Solution by YouTuber Greg Hogg
    
    int maxArea = heights[0];
    vector<vector<int>> increasingStack = {{heights[0], 0}};

    for(int i = 1; i < heights.size(); ++i)
    {
        bool appendFlag = false;
        while ((increasingStack.size() != 0) and (heights[i] < increasingStack[increasingStack.size() - 1][0]))
        {
            int height = increasingStack[increasingStack.size() - 1][0];
            int index = increasingStack[increasingStack.size() - 1][1];
            
            increasingStack.pop_back();
            
            int area = height * (i - index);
            
            if(area > maxArea)
            {
                maxArea = area;
            }
            
            if((increasingStack.size() == 0) or (heights[i]) > increasingStack[increasingStack.size() - 1][0])
            {
                increasingStack.push_back({heights[i], index});
                appendFlag = true;
            }
        }
        
        if(appendFlag == false)
        {
            increasingStack.push_back({heights[i], i});
        }
    }
    
    while(increasingStack.size() != 0)
    {
        int height = increasingStack[increasingStack.size() - 1][0];
        int index = increasingStack[increasingStack.size() - 1][1];
        
        increasingStack.pop_back();
        
        int area = (int)(height * (heights.size() - index));
        
        if(area > maxArea)
        {
            maxArea = area;
        }
    }
    
    return maxArea;
}
