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

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    //Problem #57 Insert Interval
    
    intervals.push_back(newInterval);
    
    vector<vector<int>> insertedInterval = mergeIntervals(intervals);
    
    return insertedInterval;
}

int eraseOverlapIntervals(vector<vector<int>> &intervals)
{
    //Problem 435 Non-overlapping Intervals
    
    if(intervals.size() == 1)
    {
        return 0;
    }
    
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b)
    {
        return a[1] < b[1];
    });
    
    int keepCount = 1;
    
    int previousEndTime = intervals[0][1];
    
    for(int i = 1; i < intervals.size(); ++i)
    {
        if(intervals[i][0] >= previousEndTime)
        {
            keepCount++;
            previousEndTime = intervals[i][1];
        }
    }
    
    return (int)intervals.size() - keepCount;
}
