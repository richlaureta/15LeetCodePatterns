//
//  BreadthFirstSearch.cpp
//  C++
//
//  Created by Richmond Laureta on 10/14/25.
//

#include "Header.h"

vector<vector<int>> levelOrderI(TreeNode* root)
{
    //Problem #102 Binary Tree Level Traversal
    
    if(root == nullptr)
    {
        return {};
    }
    
    vector<vector<int>> listReturn;
    
    deque<TreeNode*> myQueue;
    myQueue.push_back(root);
    
    while(!myQueue.empty())
    {
        vector<int> list;
        int queueSize = (int) myQueue.size();
        
        for(int i = 0; i < queueSize; i++)
        {
            list.push_back(myQueue[0]->value);
            TreeNode *node = myQueue[0];
            myQueue.pop_front();
            
            if(node->left != nullptr)
            {
                myQueue.push_back(node->left);
            }
            
            if(node->right != nullptr)
            {
                myQueue.push_back(node->right);
            }
        }
        
        listReturn.push_back(list);
    }
    
    return listReturn;
}

int orangesRotting(vector<vector<int>> &grid)
{
    //Problem #994 Rotting Oranges - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    int freshOrangesCount = 0;
    int minuteCount = 0;
    vector<vector<int>> rottenOrangesLocation = {};
    
    for(int i = 0; i < grid.size(); i++)
    {
        for(int j = 0; j < grid[i].size(); j++)
        {
            if(grid[i][j] == 1)
            {
                freshOrangesCount++;
            }
            else if(grid[i][j] == 2)
            {
                rottenOrangesLocation.push_back({i, j});
            }
        }
    }
    
    while ((rottenOrangesLocation.size() != 0) and freshOrangesCount > 0)
    {
        minuteCount++;
        
        vector<vector<int>> currentList = {};
        
        for(int i = 0; i < rottenOrangesLocation.size(); i++)
        {
            vector<vector<int>> adjacent = {{rottenOrangesLocation[i][0] + 1, rottenOrangesLocation[i][1]}, {rottenOrangesLocation[i][0], rottenOrangesLocation[i][1] - 1}, {rottenOrangesLocation[i][0] - 1, rottenOrangesLocation[i][1]}, {rottenOrangesLocation[i][0], rottenOrangesLocation[i][1] + 1}}; //Down, Left, Up, Right
            
            for(int j = 0; j < adjacent.size(); j++)
            {
                if((adjacent[j][0] > -1) and (adjacent[j][0] < grid.size()) and (adjacent[j][1] > -1) and (adjacent[j][1] < grid[0].size()) and (grid[adjacent[j][0]][adjacent[j][1]] == 1))
                {
                    grid[adjacent[j][0]][adjacent[j][1]] = 2;
                    freshOrangesCount--;
                    currentList.push_back({adjacent[j][0], adjacent[j][1]});
                    
                    if(freshOrangesCount == 0)
                    {
                        return minuteCount;
                    }
                }
            }
        }
        
        rottenOrangesLocation = currentList;
    }
    
    if(freshOrangesCount == 0)
    {
        return minuteCount;
    }
    else
    {
        return -1;
    }
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
