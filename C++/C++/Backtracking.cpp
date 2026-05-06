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
    // NeetCode - Understanding the Solution
    
    if(index >= (int)nums.size())
    {
        vector<int> copySubset(partialSolution);
        answer.push_back(copySubset);
        return;
    }
    
    partialSolution.push_back(nums[index]);
    depthFirstSearchSubsets(index + 1, nums, partialSolution, answer);
    
    partialSolution.pop_back();
    depthFirstSearchSubsets(index + 1, nums, partialSolution, answer);
}

vector<vector<int>> subsets(vector<int>& nums) {
     // Problem #78 Subsests - Medium - Solution Concept by YouTube Channel
     // NeetCode - Understanding the Solution

     vector<int> partialSolution;
     vector<vector<int>> answer;

     depthFirstSearchSubsets(0, nums, partialSolution, answer);

     return answer;
 }

void depthFirstSearchPermutation(vector<int> &partialSolution, vector<vector<int>> &answer, vector<int> &nums, unordered_set<int> &numberSet)
{
    //Problem #46 Permutaions - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    if((int)partialSolution.size() == (int)nums.size())
    {
        vector<int> copy(partialSolution);
        answer.push_back(copy);
        return;
    }
    
    for(int number: nums)
    {
        if(numberSet.find(number) == numberSet.end())
        {
            partialSolution.push_back(number);
            numberSet.insert(number);
            depthFirstSearchPermutation(partialSolution, answer, nums, numberSet);
            int poppedNumber = partialSolution[(int)partialSolution.size() - 1];
            partialSolution.pop_back();
            numberSet.erase(poppedNumber);
        }
    }
}

vector<vector<int>> permute(vector<int> &nums)
{
    //Problem #46 Permutaions - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
    
    vector<int> partialSolution;
    vector<vector<int>> answer;
    unordered_set<int> numberSet;
    
    depthFirstSearchPermutation(partialSolution, answer, nums, numberSet);
    
    return answer;
    
}

void depthFirstSearchQueens(int row0,
                            int nSize,
                            unordered_set<int> &columnSet,
                            unordered_set<int> &positiveDiagonalSet,
                            unordered_set<int> &negativeDiagonalSet,
                            vector<vector<string>> &possibleQueenCombinations,
                            vector<vector<char>> &board)
{
    //Problem #51 N-Queens - Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    if(row0 == nSize)
    {
        vector<string> combinations;
        string rowString;
        
        for(vector<char> row: board)
        {
            rowString = "";
            rowString.insert(rowString.end(), row.begin(), row.end());
            combinations.push_back(rowString);
        }
        
        possibleQueenCombinations.push_back(combinations);
        
        return;
    }
    
    
    for(int column = 0; column < nSize; column++)
    {
        if(columnSet.find(column) != columnSet.end() or
           positiveDiagonalSet.find(row0 + column) != positiveDiagonalSet.end() or
           negativeDiagonalSet.find(row0 - column) != negativeDiagonalSet.end())
        {
            continue;
        }
        
        columnSet.insert(column);
        positiveDiagonalSet.insert(row0 + column);
        negativeDiagonalSet.insert(row0 - column);
        board[row0][column] = 'Q';
        
        depthFirstSearchQueens(row0 + 1, nSize, columnSet, positiveDiagonalSet, negativeDiagonalSet, possibleQueenCombinations, board);
        
        columnSet.erase(column);
        positiveDiagonalSet.erase(row0 + column);
        negativeDiagonalSet.erase(row0 - column);
        board[row0][column] = '.';
    }
}

vector<vector<string>> solveNQueens(int n)
{
    //Problem #51 N-Queens - Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    unordered_set<int> columnset = {};
    unordered_set<int> positiveDiagonalSet = {};
    unordered_set<int> negativeDiagonalSet = {};
    
    vector<vector<string>> possibleQueenCombinations = {};
    vector<vector<char>> board(n, vector<char>(n, '.'));
    
    depthFirstSearchQueens(0, n, columnset, positiveDiagonalSet, negativeDiagonalSet, possibleQueenCombinations, board);
    
    return possibleQueenCombinations;
}
