//
//  OverlappingIntervals.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/18/25.
//

#include "Header.h"

vector<vector<int>> mergeIntervals(vector<vector<int>> &intervals)
{
    //Problem #56 Merge Intervals
    sort(intervals.begin(), intervals.end());

    vector<vector<int>> merged = {{intervals[0]}};

    for (size_t i = 1; i < intervals.size(); i++) {
        if ((intervals[i][0] <= merged[merged.size() - 1][1]) &&
            (intervals[i][1] > merged[merged.size() - 1][1])) {
            merged[merged.size() - 1][1] = intervals[i][1];
        } else if (intervals[i][0] > merged[merged.size() - 1][1]) {
            merged.push_back(intervals[i]);
        }
    }
    
    return merged;
}
