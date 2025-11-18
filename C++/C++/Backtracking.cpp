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
