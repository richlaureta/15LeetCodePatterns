//
//  TopKElements.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/9/25.
//

#include "Header.h"

int findKthLargest(vector<int> &nums, int k)
{
    //Problem #215 Kth Largest Element in an Array - Medium
    
    priority_queue<int, vector<int>, greater<int>> maxK;
    
    for(int number: nums)
    {
        if((int)maxK.size() < k) maxK.push(number);
        else
        {
            maxK.push(number);
            maxK.pop();
        }
    }
    
    return maxK.top();
}

vector<int> topKFrequent(vector<int>& nums, int k)
{
    //Problem #347 Top K Frequent Elements - Medium
    
    unordered_map<int, int> frequencyMap;
    priority_queue<pair<int,int>,  vector<pair<int, int>>, greater<pair<int,int>>> minHeap;
    
    for(int number: nums) frequencyMap[number] += 1;
    
    for(pair<int, int> pairNumberFrequency: frequencyMap)
    {
        if((int)minHeap.size() < k) minHeap.push({pairNumberFrequency.second, pairNumberFrequency.first});
        else
        {
            minHeap.push({pairNumberFrequency.second, pairNumberFrequency.first});
            minHeap.pop();
        }
    }
    
    vector<int> kTopElements = {};
    
    while((int)minHeap.size() != 0)
    {
        kTopElements.push_back(minHeap.top().second);
        minHeap.pop();
    }
    
    return kTopElements;
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
