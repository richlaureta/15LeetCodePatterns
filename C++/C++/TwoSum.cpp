//
//  TwoSum.cpp
//  C++
//
//  Created by Richmond Laureta on 7/25/25.
//

#include "Header.h"
#include <iostream>
vector<int> twoSum(vector<int>& nums, int target)
{
    unordered_map<int, int> myMap;
    
    for(int i = 0; i < nums.size(); i++)
    {
        int difference = target - nums[i];
        
        if (myMap.count(difference) > 0)
        {
            return {myMap[difference], i};
        }
        
        myMap[nums[i]] = i;
    }
    
    return {};
}
