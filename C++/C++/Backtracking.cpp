//
//  Backtracking.cpp
//  C++
//
//  Created by Richmond Laureta on 8/1/25.
//
#include "Header.h"

void backtrack(int index, int sizeOfNums, vector<vector<int>>& finalAnswer, vector<int>& tracker, vector<int>& nums)
{
    if(index == sizeOfNums)
    {
        finalAnswer.push_back({tracker});
        return;
    }
    
    backtrack(index + 1, sizeOfNums, finalAnswer, tracker, nums);
    
    tracker.push_back({nums[index]});
    
    backtrack(index + 1, sizeOfNums, finalAnswer, tracker, nums);
    
    tracker.pop_back();
}

vector<vector<int>> subsets(vector<int>& nums)
{
    //Problem #78 Subsests Concept by Greg Hogg(YouTuber)
    
    int sizeOfnums = (int)nums.size();
    vector<vector<int>> finalAnswer;
    vector<int> tracker;
    
    backtrack(0, sizeOfnums, finalAnswer, tracker, nums);
    return finalAnswer;
}

