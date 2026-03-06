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
    //Problem #373 Find K Pairs with Smallest Sums - Medium
    
    priority_queue<vector<int>, vector<vector<int>>, less<vector<int>>> maxHeap;
    
    for(int index0 = 0; index0 < (int)nums1.size(); index0++)
    {
        for(int index1 = 0; index1 < (int)nums2.size(); index1++)
        {
            if((int)maxHeap.size() < k) maxHeap.push({nums1[index0] + nums2[index1], nums1[index0], nums2[index1]});
            else if(nums1[index0] + nums2[index1] < maxHeap.top()[0])
            {
                maxHeap.pop();
                maxHeap.push({nums1[index0] + nums2[index1], nums1[index0], nums2[index1]});
            }
            else break;
        }
    }
    
    vector<vector<int>> smallestSumPairVector;
    
    while(maxHeap.size() > 0)
    {
        vector<int> poppedValue = maxHeap.top();
        maxHeap.pop();
        smallestSumPairVector.push_back({poppedValue[1], poppedValue[2]});
    }
    
    return smallestSumPairVector;
}
