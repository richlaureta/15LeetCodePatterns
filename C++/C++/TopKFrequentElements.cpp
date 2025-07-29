//
//  TopKFrequentElements.cpp
//  C++
//
//  Created by Richmond Laureta on 7/28/25.
//
#include "Header.h"

vector<int> topKFrequent(vector<int>& nums, int k)
{
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
