//
//  BacktrackingEfficient.cpp
//  C++
//
//  Created by Richmond Laureta on 8/1/25.
//
#include "Header.h"

vector<vector<int>> subsetsEfficient(vector<int>& nums)
{
    // Google CLI AI Generated Answers for Problem #78 Subsets
    
    vector<vector<int>> finalAnswer;
    finalAnswer.push_back({});
    
    for(int num : nums)
    {
        int n = (int)finalAnswer.size();
        for(int i = 0; i < n; i++)
        {
            vector<int> temp = finalAnswer[i];
            temp.push_back(num);
            finalAnswer.push_back(temp);
        }
    }
    
    return finalAnswer;
}
