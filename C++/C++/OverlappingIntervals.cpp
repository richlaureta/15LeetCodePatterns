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
    //Problem #57 Insert Interval - Medium
    
    vector<vector<int>> newIntervalsVector = {};
    bool insertedFlag = false;
    int index = 0;
    
    for(vector<int> interval: intervals)
    {
        if(newInterval[0] >= interval[0] and
           newInterval[0] <= interval[1] and
           newInterval[1] >= interval[1])
        {
            newIntervalsVector.push_back({interval[0], newInterval[1]});
            insertedFlag = true;
            break;
        }
        else if(newInterval[0] >= interval[0] and
                newInterval[0] < interval[1] and
                newInterval[1] < interval[1])
        {
            newIntervalsVector.push_back({interval[0], interval[1]});
            insertedFlag = true;
            break;
        }
        else if(newInterval[0] == interval[0] and
                newInterval[1] == interval[1])
        {
            newIntervalsVector.push_back({newInterval[0], newInterval[1]});
            insertedFlag = true;
            break;
        }
        else if(newInterval[0] < interval[0] and
                newInterval[1] >= interval[0] and
                newInterval[1] < interval[1])
        {
            newIntervalsVector.push_back({newInterval[0], interval[1]});
            insertedFlag = true;
            break;
        }
        else if(newInterval[1] < interval[0])
        {
            newIntervalsVector.push_back({newInterval[0], newInterval[1]});
            newIntervalsVector.push_back({interval[0], interval[1]});
            insertedFlag = true;
            break;
        }
        else if(newInterval[0] > interval[1]) newIntervalsVector.push_back({interval[0], interval[1]});
        
        index++;
    }
    
    index++;
    
    for(int index1 = index; index1 < (int)intervals.size(); index1++)
    {
        vector<int> previousInterval = newIntervalsVector[(int)newIntervalsVector.size() - 1];
        
        if (previousInterval[0] < intervals[index1][0] and
            previousInterval[1] < intervals[index1][1] and
            previousInterval[1] >= intervals[index1][0])
        {
            newIntervalsVector.pop_back();
            newIntervalsVector.push_back({previousInterval[0], intervals[index1][1]});
        }
        else if(previousInterval[1] < intervals[index1][0]) newIntervalsVector.push_back({intervals[index1][0], intervals[index1][1]});
    }
    
    if(insertedFlag == false) newIntervalsVector.push_back(newInterval);
    
    return newIntervalsVector;
}

int eraseOverlapIntervals(vector<vector<int>> &intervals)
{
    //Problem 435 Non-overlapping Intervals - Medium
    
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b)
    {
        return a[1] < b[1];
    });
    
    int previousEndTime = intervals[0][1];
    
    int minimumOverlapCount = 0;
    
    for(int index = 1; index < (int)intervals.size(); index++)
    {
        if(intervals[index][0] < previousEndTime) minimumOverlapCount++;
        else previousEndTime = intervals[index][1];
    }
    
    return minimumOverlapCount;
}
