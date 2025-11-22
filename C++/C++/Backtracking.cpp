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

void depthFirstSearchQueens(int row0,
                            int nSize,
                            set<int> &column,
                            set<int> &positiveDiagonal,
                            set<int> &negativeDiagonal,
                            vector<vector<string>> &result,
                            vector<vector<char>> &board)
{
    //Problem #51 N-Queens - Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    if(row0 == nSize)
    {
        vector<string> copy = {};
        for(int i = 0; i < board.size(); i++)
        {
            string characterCopy = {};
            for(int j = 0; j < board[i].size(); j++)
            {
                characterCopy += board[i][j];
            }
            copy.push_back(characterCopy);
        }
        result.push_back(copy);
        return;
    }
    
    for(int i = 0; i < nSize; i++)
    {
        if((column.find(i) != column.end()) or (positiveDiagonal.find(row0 + i) != positiveDiagonal.end()) or (negativeDiagonal.find(row0 - i) != negativeDiagonal.end()))
        {
            continue;
        }
        
        column.insert(i);
        positiveDiagonal.insert(row0 + i);
        negativeDiagonal.insert(row0 - i);
        board[row0][i] = 'Q';
        
        depthFirstSearchQueens(row0 + 1, nSize, column, positiveDiagonal, negativeDiagonal, result, board);
        
        column.erase(i);
        positiveDiagonal.erase(row0 + i);
        negativeDiagonal.erase(row0 - i);
        board[row0][i] = '.';
    }

}

vector<vector<string>> solveNQueens(int n)
{
    //Problem #51 N-Queens - Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    set<int> column;
    set<int> positiveDiagonal;
    set<int> negativeDiagonal;
    
    vector<vector<string>> result;
    
    vector<char> dots = {};
    
    for(int i = 0; i < n; i++)
    {
        dots.push_back('.');
    }
    
    vector<vector<char>> board;
    
    for(int i = 0; i < n; i++)
    {
        board.push_back(dots);
    }
    
    depthFirstSearchQueens(0, n, column, positiveDiagonal, negativeDiagonal, result, board);
    
    return result;
}
