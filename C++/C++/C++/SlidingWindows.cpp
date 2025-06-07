//
//  SlidingWindows.cpp
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#include "Header.h"

#include <iostream>
#include <vector>

using namespace std;

double findMaxAverage(vector<int> &nums, int k)
{
    double total = 0;
    size_t leftIndex = 0;
    double maxSum = 0;

    for (size_t i = 0; i < k; ++i)
    {
        total += nums[i];
    }

    maxSum = total;

    for (size_t i = k; i < nums.size(); ++i)
    {
        total += nums[i] - nums[leftIndex];
        leftIndex++;

        if (total > maxSum)
        {
            maxSum = total;
        }
    }

    return maxSum / k;
}
