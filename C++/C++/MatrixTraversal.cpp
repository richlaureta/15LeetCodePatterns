//
//  MatrixTraversal.cpp
//  C++
//
//  Created by Richmond Laureta on 7/29/25.
//

#include "Header.h"

void breadthFirstSearch(int rowNumber, int columnNumber, set<vector<int>>& visited, vector<vector<char>>& grid)
{
    queue<vector<int>> q;
    q.push({rowNumber, columnNumber});
    visited.insert({rowNumber, columnNumber});
    
    while(!q.empty())
    {
        int rowNum = q.front()[0];
        int columnNum = q.front()[1];
        q.pop();
        
        vector<vector<int>> directions = {{rowNum - 1, columnNum}, {rowNum, columnNum + 1}, {rowNum + 1, columnNum}, {rowNum, columnNum - 1}};
        
        for(int i = 0; i < directions.size(); ++i)
        {
            if((directions[i][0] > -1) &&
               (directions[i][0] < grid.size()) &&
               (directions[i][1] > -1) &&
               (directions[i][1] < grid[0].size())&&
               (grid[directions[i][0]][directions[i][1]] == '1') &&
               (visited.find({directions[i][0], directions[i][1]}) == visited.end()))
            {
                q.push({directions[i][0], directions[i][1]});
                visited.insert({directions[i][0], directions[i][1]});
            }
        }
    }
}

int numIslands(vector<vector<char>>& grid)
{
    if(grid.size() == 0 || grid.empty())
    {
        return 0;
    }
    
    set<vector<int>> visited;
    int islandCount = 0;
    
    for(int i = 0; i < grid.size(); i++)
    {
        for(int j = 0; j < grid[i].size(); j++)
        {
            if((grid[i][j] == '1') && visited.find({i,j}) == visited.end())
            {
                breadthFirstSearch(i, j, visited, grid);
                islandCount++;
            }
        }
    }
    
    return islandCount;
}

vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
{
    //Problem #733 Flood Fill - Easy
    
    deque<pair<int, int>> fillQueue = {{sr, sc}};
    int fillColor = image[sr][sc];
    image[sr][sc] = color;
    
    while((int) fillQueue.size() > 0)
    {
        int fillQueueSize = (int) fillQueue.size();
        for(int index = 0; index < fillQueueSize; index++)
        {
            int row = fillQueue.front().first;
            int column = fillQueue.front().second;
            
            fillQueue.pop_front();
            
            pair<int, int> leftDirection = {row, column - 1};
            pair<int, int> upDirection = {row - 1, column};
            pair<int, int> rightDirection = {row, column + 1};
            pair<int, int> downDirection = {row + 1, column};
            
            if(leftDirection.second > -1 and
               image[leftDirection.first][leftDirection.second] == fillColor and
               image[leftDirection.first][leftDirection.second] != color)
            {
                fillQueue.push_back({leftDirection.first, leftDirection.second});
                image[leftDirection.first][leftDirection.second] = color;
            }
            
            if(upDirection.first > -1 and
               image[upDirection.first][upDirection.second] == fillColor and
               image[upDirection.first][upDirection.second] != color)
            {
                fillQueue.push_back({upDirection.first, upDirection.second});
                image[upDirection.first][upDirection.second] = color;
            }
            
            if(rightDirection.second < (int) image[0].size() and
               image[rightDirection.first][rightDirection.second] == fillColor and
               image[rightDirection.first][rightDirection.second] != color)
            {
                fillQueue.push_back({rightDirection.first, rightDirection.second});
                image[rightDirection.first][rightDirection.second] = color;
            }
            
            if(downDirection.first < (int)image.size() and
               image[downDirection.first][downDirection.second] == fillColor and
               image[downDirection.first][downDirection.second] != color)
            {
                fillQueue.push_back({downDirection.first, downDirection.second});
                image[downDirection.first][downDirection.second] = color;
            }
            
        }
    }
    
    return image;
}

void breadthFirstSearchRegion(int index0, int index1, vector<vector<char>> &board, bool &nearBorderFlag, set<pair<int,int>> &visited, deque<pair<int, int>> &locationQueue, vector<pair<int,int>> &setToO)
{
    //Problem #130 Surrounded Region - Medium
    
    visited.insert({index0, index1});
    setToO.push_back({index0, index1});
    locationQueue.push_back({index0, index1});
    
    if((index0 == 0) or (index0 == board.size() - 1) or (index1 == 0) or (index1 == board[0].size() - 1))
    {
        nearBorderFlag = true;
    }
    
    while(locationQueue.size() != 0)
    {
        int row = locationQueue.front().first;
        int column = locationQueue.front().second;
        
        locationQueue.pop_front();
        
        vector<pair<int, int>> checkDirections = {{row - 1, column}, {row, column + 1}, {row + 1, column}, {row, column - 1}};
        
        for(int i = 0; i < checkDirections.size(); i++)
        {
            if((checkDirections[i].first > -1) and (checkDirections[i].first < board.size()) and (checkDirections[i].second > -1) and (checkDirections[i].second < board[0].size()) and board[checkDirections[i].first][checkDirections[i].second] == 'O' and (visited.find({checkDirections[i].first, checkDirections[i].second}) == visited.end()))
            {
                visited.insert({checkDirections[i].first, checkDirections[i].second});
                locationQueue.push_back({checkDirections[i].first, checkDirections[i].second});
                setToO.push_back({checkDirections[i].first, checkDirections[i].second});
                
                if((checkDirections[i].first == 0) or (checkDirections[i].first == board.size() - 1) or (checkDirections[i].second == 0) or (checkDirections[i].second == board[0].size() - 1))
                {
                    nearBorderFlag = true;
                }
            }
        }
    }
}

void solve(vector<vector<char>> &board)
{
    //Problem #130 Surrounded Regions - Medium
    
    set<pair<int, int>> visited;
    deque<pair<int, int>> locationQueue;
    vector<pair<int,int>> setToO;
    bool nearBorderFlag = false;
    
    
    for(int i = 0; i < board.size(); i++)
    {
        for(int j = 0; j < board[i].size(); j++)
        {
            if((board[i][j] == 'O') and (visited.find({i, j}) == visited.end()))
            {
                breadthFirstSearchRegion(i, j, board, nearBorderFlag, visited, locationQueue, setToO);
                
                if(nearBorderFlag == false)
                {
                    for(int i = 0; i < setToO.size(); i++)
                    {
                        board[setToO[i].first][setToO[i].second] = 'X';
                    }
                    setToO = {};
                }
                else
                {
                    nearBorderFlag = false;
                    setToO = {};
                }
            }
        }
    }
}
