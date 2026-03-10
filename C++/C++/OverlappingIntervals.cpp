//
//  OverlappingIntervals.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/18/25.
//

#include "Header.h"

vector<vector<int>> merge(vector<vector<int>> &intervals)
{
    //Problem #56 Merge Intervals
    
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> newMergedIntervalsVector = {{intervals[0]}};
    
    for(int index = 0; index < (int)intervals.size() - 1; index++)
    {
        pair<int, int> previousInterval = {newMergedIntervalsVector[(int)newMergedIntervalsVector.size() - 1][0], newMergedIntervalsVector[(int)newMergedIntervalsVector.size() - 1][1]};
        
        if(previousInterval.second >= intervals[index + 1][0])
        {
            if(intervals[index + 1][1] < previousInterval.second)
            {
                newMergedIntervalsVector.pop_back();
                newMergedIntervalsVector.push_back({previousInterval.first, previousInterval.second});
            }
            else
            {
                newMergedIntervalsVector.pop_back();
                newMergedIntervalsVector.push_back({previousInterval.first, intervals[index + 1][1]});
            }
        }
        else newMergedIntervalsVector.push_back({intervals[index + 1][0], intervals[index + 1][1]});
    }
    
    return newMergedIntervalsVector;
}

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    //Problem #57 Insert Interval
    
    intervals.push_back(newInterval);
    
    vector<vector<int>> insertedInterval = merge(intervals);
    
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
