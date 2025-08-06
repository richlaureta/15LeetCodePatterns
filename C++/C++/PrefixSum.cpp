//
//  PrefixSum.cpp
//  C++
//
//  Created by Richmond Laureta on 8/6/25.
//

#include "Header.h"

int findMaxLength(vector<int> &nums)
{
    //Problem #525 Contiguous Array
    
    //Solution Concept by Youtuber "NeetCodeIO"
    int zeroCount = 0;
    int oneCount = 0;
    int maxResult = 0;
    
    unordered_map<int, int> differenceIndex;
    
    for(int i = 0; i < nums.size(); ++i)
    {
        if(nums[i] == 1)
        {
            oneCount++;
        }
        else
        {
            zeroCount++;
        }
        
        if(differenceIndex.count(oneCount - zeroCount) == 0)
        {
            differenceIndex[oneCount - zeroCount] = i;
        }
        
        if(oneCount == zeroCount)
        {
            maxResult = oneCount + zeroCount;
        }
        else
        {
            int index0 = differenceIndex[oneCount - zeroCount];
            maxResult = max(maxResult, i - index0);
        }
    }
    
    return maxResult;
}
