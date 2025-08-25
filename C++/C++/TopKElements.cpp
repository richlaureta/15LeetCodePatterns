//
//  TopKElements.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/9/25.
//

#include "Header.h"

int findKthLargest(vector<int> &nums, int k)
{
    //Problem #215 Kth Largest Element in an Array
    
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    for(int i = 0; i < k; ++i)
    {
        minHeap.push(nums[i]);
    }
    
    for(int i = k; i < nums.size(); ++i)
    {
        if(nums[i] > minHeap.top())
        {
            minHeap.pop();
            minHeap.push(nums[i]);
        }
    }
    
    return minHeap.top();
}
