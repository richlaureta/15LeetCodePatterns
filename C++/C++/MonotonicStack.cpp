//
//  MonotonicStack.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/9/25.
//

#include "Header.h"

vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
{
    //Problem 496 Next Greater Element I - Easy
    
    stack<int> indexStack({0});
    
    vector<int> increasingVector((int)nums2.size(), -1);
    
    unordered_map<int, int> indexMap = {{nums2[0], 0}};
    
    vector<int> greaterElementVector((int)nums1.size());
    
    for(int index = 1; index < (int)nums2.size(); index++)
    {
        while((int)indexStack.size() > 0 and nums2[indexStack.top()] < nums2[index])
        {
            int stackTop = indexStack.top();
            indexStack.pop();
            increasingVector[stackTop] = nums2[index];
        }
        
        indexStack.push(index);
        indexMap[nums2[index]] = index;
    }
    
    for(int index1 = 0; index1 < (int)greaterElementVector.size(); index1++) greaterElementVector[index1] = increasingVector[indexMap[nums1[index1]]];
    
    return greaterElementVector;
}

vector<int> dailyTemperatures(vector<int> &temperatures)
{
    //Problem #739 Daily Temperatures - Medium
    
    stack<int> stackIndex({0});
    vector<int> increasingVector((int)temperatures.size());
    
    for(int index = 1; index < (int)temperatures.size(); index++)
    {
        while((int)stackIndex.size() > 0 and temperatures[stackIndex.top()] < temperatures[index])
        {
            increasingVector[stackIndex.top()] = index - stackIndex.top();
            stackIndex.pop();
        }
        
        stackIndex.push(index);
    }
    
    return increasingVector;
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
