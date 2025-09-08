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

vector<int> topKFrequent(vector<int>& nums, int k)
{
    //Problem #347 Top K Frequent Elements
    
    unordered_map<int, int> frequencyMap;
    
    for(int i = 0; i < nums.size(); ++i)
    {
        frequencyMap[nums[i]]++;
    }
    
    vector<vector<int>> frequencyArray;
    
    for(int i = 0; i < nums.size() + 1; ++i)
    {
        frequencyArray.push_back({});
    }

    for(const auto& pair : frequencyMap)
    {
        frequencyArray[pair.second].push_back(pair.first);
    }
    
    vector<int> topKArray;
    
    for(int i = (int)(frequencyArray.size() - 1); i > - 1; --i)
    {
        if(k == 0)
        {
            return topKArray;
        }
        
        if(frequencyArray[i].size() == 1)
        {
            topKArray.push_back(frequencyArray[i][0]);
            k--;
        }
        else if(frequencyArray[i].size() > 1)
        {
            for(int j = 0; j < frequencyArray[i].size(); j++)
            {
                if(k == 0)
                {
                    return topKArray;
                }
                
                topKArray.push_back(frequencyArray[i][j]);
                k--;
            }
        }
    }
    return topKArray;
}

vector<vector<int>> kSmallestPairs(vector<int> &nums1, vector<int> &nums2, int k)
{
    vector<vector<int>> result;
    cout << "TESTING" << endl;
    return result;
}
