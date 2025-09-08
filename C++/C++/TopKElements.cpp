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
    //Problem #373 Find K Pairs with Smallest Sums - Solution Concept by YouTuber TechError
    
    vector<vector<int>> result;
    set<tuple<int, int>> visitedPairSet;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;
    
    visitedPairSet.insert(make_tuple(0, 0));
    minHeap.emplace(make_tuple(nums1[0] + nums2[0], 0, 0));
    
    while(k and !minHeap.empty())
    {
        int indexNums1 = get<1>(minHeap.top());
        int indexNums2 = get<2>(minHeap.top());
    
        minHeap.pop();
        
        result.push_back({nums1[indexNums1], nums2[indexNums2]});
        
        if((indexNums1 + 1 < nums1.size()) and (visitedPairSet.count(make_tuple(indexNums1 + 1, indexNums2)) == 0))
        {
            minHeap.push(make_tuple(nums1[indexNums1 + 1] + nums2[indexNums2], indexNums1 + 1, indexNums2));
            visitedPairSet.insert(make_tuple(indexNums1 + 1, indexNums2));
        }
        
        if((indexNums2 + 1 < nums2.size()) and (visitedPairSet.count(make_tuple(indexNums1, indexNums2 + 1)) == 0))
        {
            minHeap.push(make_tuple(nums1[indexNums1] + nums2[indexNums2 + 1], indexNums1, indexNums2 + 1));
            visitedPairSet.insert(make_tuple(indexNums1, indexNums2 + 1));
        }
        
        k--;
    }
    
    return result;
}
