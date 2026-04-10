//
//  BreadthFirstSearch.cpp
//  C++
//
//  Created by Richmond Laureta on 10/14/25.
//

#include "Header.h"

vector<vector<int>> levelOrderI(TreeNode* root)
{
    //Problem #102 Binary Tree Level Traversal - Medium
    
    if(root == nullptr) return {};
    
    vector<vector<int>> levelOrderVector = {};
    deque<TreeNode*> nodeQueue = {root};
    vector<int> levelVector = {root->val};
    
    while((int)nodeQueue.size() > 0)
    {
        levelOrderVector.push_back(levelVector);
        levelVector = {};
        int nodeQueueSize = (int)nodeQueue.size();
        
        for(int index = 0; index < nodeQueueSize; index++)
        {
            TreeNode *node = nodeQueue.front();
            nodeQueue.pop_front();
            
            if(node->left != nullptr)
            {
                nodeQueue.push_back(node->left);
                levelVector.push_back(node->left->val);
            }
            
            if(node->right != nullptr)
            {
                nodeQueue.push_back(node->right);
                levelVector.push_back(node->right->val);
            }
        }
    }
    
    return levelOrderVector;
}

int orangesRotting(vector<vector<int>> &grid)
{
    //Problem #994 Rotting Oranges - Medium
    
    deque<pair<int , int>> rotSquareQueue;
    
    bool thereIsA1Flag = false;
    bool thereIsA2Flag = false;
    
    int square1Count = 0;
    
    for(int index = 0; index < grid.size(); index++)
    {
        for(int index1 = 0; index1 < grid[0].size(); index1++)
        {
            if(grid[index][index1] == 1)
            {
                square1Count++;
                thereIsA1Flag = true;
            }
            else if (grid[index][index1] == 2)
            {
                rotSquareQueue.push_back({index, index1});
                thereIsA2Flag = true;
            }
        }
    }
    
    if(thereIsA1Flag == false) return 0;
    else if(thereIsA2Flag == false and thereIsA1Flag == true) return -1;
    
    int minutesToRot = -1;
    int check1Count = 0;
    
    while((int) rotSquareQueue.size() > 0)
    {
        int rotSquareQueueSize = (int) rotSquareQueue.size();
        
        for(int index2 = 0; index2 < rotSquareQueueSize; index2++)
        {
            pair<int, int> square = rotSquareQueue.front();
            rotSquareQueue.pop_front();
            
            pair<int, int> leftDirection = {square.first, square.second - 1};
            pair<int, int> upDirection = {square.first - 1, square.second};
            pair<int, int> rightDirection = {square.first, square.second + 1};
            pair<int, int> downDirection = {square.first + 1, square.second};
            
            if(leftDirection.second > -1 and grid[leftDirection.first][leftDirection.second] == 1)
            {
                check1Count++;
                grid[leftDirection.first][leftDirection.second] = 2;
                rotSquareQueue.push_back(leftDirection);
            }
            
            if(upDirection.first > -1 and grid[upDirection.first][upDirection.second] == 1)
            {
                check1Count++;
                grid[upDirection.first][upDirection.second] = 2;
                rotSquareQueue.push_back(upDirection);
            }
            
            if(rightDirection.second < (int) grid[0].size() and grid[rightDirection.first][rightDirection.second] == 1)
            {
                check1Count++;
                grid[rightDirection.first][rightDirection.second] = 2;
                rotSquareQueue.push_back(rightDirection);
            }
            
            if(downDirection.first < (int) grid.size() and grid[downDirection.first][downDirection.second] == 1)
            {
                check1Count++;
                grid[downDirection.first][downDirection.second] = 2;
                rotSquareQueue.push_back(downDirection);
            }
        }
        
        minutesToRot++;
    }
    
    if(check1Count == square1Count) return minutesToRot;
    
    return -1;
}

int ladderLength(string beginWord, string endWord, vector<string> &wordList)
{
    //Problem #127 Word Ladder: Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    bool inThereFlag = false;
    
    for(int i = 0; i < wordList.size(); i++)
    {
        if(endWord == wordList[i])
        {
            inThereFlag = true;
            break;
        }
    }
    
    if(inThereFlag == false)
    {
        return 0;
    }
    
    unordered_map<string, vector<string>> wordMap;
    wordList.push_back(beginWord);
    
    for(int i = 0; i < wordList.size(); i++)
    {
        int starIndexPlacement = 0;
        for(int j = 0; j < wordList[i].size(); j++)
        {
            string newWord = "";
            for(int k = 0; k < wordList[i].size(); k++)
            {
                if(k == starIndexPlacement)
                {
                    newWord += "*";
                }
                else
                {
                    newWord += wordList[i][k];
                }
            }
            wordMap[newWord].push_back(wordList[i]);
            starIndexPlacement++;
        }
    }
    
    set<string> visited = {beginWord};
    deque<string> q = {beginWord};
    int sequenceCount = 1;
    
    while(q.size() != 0)
    {
        int qSize = (int) q.size();
        for(int i = 0; i < qSize; i++)
        {
            string connectingWord = q.front();
            q.pop_front();
            int starIndexPlacement1 = 0;
            
            if(connectingWord == endWord)
            {
                return sequenceCount;
            }
            
            for(int j = 0; j < connectingWord.size(); j++)
            {
                string newWord1 = "";
                for(int k = 0; k < connectingWord.size(); k++)
                {
                    if(k == starIndexPlacement1)
                    {
                        newWord1 += "*";
                    }
                    else
                    {
                        newWord1 += connectingWord[k];
                    }
                }
                for(int l = 0; l < wordMap[newWord1].size(); l++)
                {
                    if(visited.find(wordMap[newWord1][l]) == visited.end())
                    {
                        visited.insert(wordMap[newWord1][l]);
                        q.push_back(wordMap[newWord1][l]);
                    }
                }
                starIndexPlacement1++;
            }
        }
        sequenceCount++;
    }
    return 0;
}
