//
//  Backtracking.cpp
//  C++
//
//  Created by Richmond Laureta on 8/1/25.
//
#include "Header.h"

void depthFirstSearchSubsets(int index, vector<int>& nums,
                             vector<int>& partialSolution,
                             vector<vector<int>>& answer) {
    // Problem #78 Subsests - Medium - Solution Concept by YouTube Channel
    // Greg Hogg - Understanding the Solution

    if (index == nums.size()) {
        vector<int> copy = partialSolution;
        answer.push_back(copy);
        return;
    }

    depthFirstSearchSubsets(index + 1, nums, partialSolution, answer);

    partialSolution.push_back(nums[index]);

    depthFirstSearchSubsets(index + 1, nums, partialSolution, answer);

    partialSolution.pop_back();
}

vector<vector<int>> subsets(vector<int>& nums) {
     // Problem #78 Subsests - Medium - Solution Concept by YouTube Channel
     // Greg Hogg - Understanding the Solution

     vector<int> partialSolution;
     vector<vector<int>> answer;

     depthFirstSearchSubsets(0, nums, partialSolution, answer);

     return answer;
 }

void depthFirstSearchPermutation(vector<int> &partialSolution, vector<vector<int>> &answer, vector<int> &nums)
{
    //Problem #46 Permutaions - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    if(partialSolution.size() == nums.size())
    {
        vector<int> copy = partialSolution;
        answer.push_back(copy);
        return;
    }
    
    for(int i = 0; i < nums.size(); i++)
    {
        bool inThereFlag = false;
        
        for(int j = 0; j < partialSolution.size(); j++)
        {
            if(nums[i] == partialSolution[j])
            {
                inThereFlag = true;
                break;
            }
        }
        
        if(inThereFlag == false)
        {
            partialSolution.push_back(nums[i]);
            depthFirstSearchPermutation(partialSolution, answer, nums);
            partialSolution.pop_back();
        }
        else
        {
            inThereFlag = false;
        }
    }
}

vector<vector<int>> permute(vector<int> &nums)
{
    //Problem #46 Permutaions - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    vector<int> partialSolution;
    vector<vector<int>> answer;
    
    depthFirstSearchPermutation(partialSolution, answer, nums);
    
    return answer;
    
}
