//
//  MatrixTraversal.cpp
//  C++
//
//  Created by Richmond Laureta on 7/29/25.
//

#include "Header.h"

int numIslands(vector<vector<char>>& grid)
{
    //Problem #200 Number of Islands - Medium
    
    int numberOfIslandsCount = 0;
    
    for(int index = 0; index < (int) grid.size(); index++)
    {
        for(int index1 = 0; index1 < (int)grid[0].size(); index1++)
        {
            if(grid[index][index1] == '1')
            {
                stack<pair<int, int>> squareStack({{index, index1}});
                numberOfIslandsCount++;
                grid[index][index1] = '2';
                
                while((int)squareStack.size() > 0)
                {
                    int row = squareStack.top().first;
                    int column = squareStack.top().second;
                    
                    squareStack.pop();
                    
                    pair<int, int> leftDirection = {row, column -1};
                    pair<int, int> upDirection = {row - 1, column};
                    pair<int, int> rightDirection = {row, column + 1};
                    pair<int, int> downDirection = {row + 1, column};
                    
                    if(leftDirection.second > -1 and grid[leftDirection.first][leftDirection.second] == '1')
                    {
                        grid[leftDirection.first][leftDirection.second] = '2';
                        squareStack.push({leftDirection.first, leftDirection.second});
                    }
                    
                    if(upDirection.first > -1 and grid[upDirection.first][upDirection.second] == '1')
                    {
                        grid[upDirection.first][upDirection.second] = '2';
                        squareStack.push({upDirection.first, upDirection.second});
                    }
                    
                    if(rightDirection.second < (int) grid[0].size() and grid[rightDirection.first][rightDirection.second] == '1')
                    {
                        grid[rightDirection.first][rightDirection.second] = '2';
                        squareStack.push({rightDirection.first, rightDirection.second});
                    }
                    
                    if(downDirection.first < (int) grid.size() and grid[downDirection.first][downDirection.second] == '1')
                    {
                        grid[downDirection.first][downDirection.second] = '2';
                        squareStack.push({downDirection.first, downDirection.second});
                    }
                }
            }
        }
    }
    
    return numberOfIslandsCount;
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

void solve(vector<vector<char>> &board)
{
    //Problem #130 Surrounded Regions - Medium
    
    deque<pair<int, int>> connectedSquaresQueue;
    set<pair<int, int>> seenSquareCells;
    
    for(int index = 0; index < (int)board.size(); index++)
    {
        for(int index1 = 0; index1 < (int)board[0].size(); index1++)
        {
            if(seenSquareCells.find({index, index1}) == seenSquareCells.end() and
               board[index][index1] == 'O' and
               index > 0 and
               index < ((int) board.size()) - 1 and
               index1 > 0 and
               index1 < (int)board[0].size() - 1)
            {
                vector<pair<int, int>> connectedSquaresVector = {{index, index1}};
                connectedSquaresQueue.push_back({index, index1});
                seenSquareCells.insert({index, index1});
                
                bool connectedToEdgeFlag = false;
                
                while((int)connectedSquaresQueue.size() > 0)
                {
                    int connectedSquaresQueueSize = (int)connectedSquaresQueue.size();
                    
                    for(int index2 = 0; index2 < connectedSquaresQueueSize; index2++)
                    {
                        int row = connectedSquaresQueue.front().first;
                        int column = connectedSquaresQueue.front().second;
                        
                        connectedSquaresQueue.pop_front();
                        
                        pair<int, int> leftDirection = {row, column - 1};
                        pair<int, int> upDirection = {row - 1, column};
                        pair<int, int> rightDirection = {row, column + 1};
                        pair<int, int> downDirection = {row + 1, column};
                        
                        if(leftDirection.second > -1 and
                           seenSquareCells.find({leftDirection.first, leftDirection.second}) == seenSquareCells.end() and
                           board[leftDirection.first][leftDirection.second] == 'O')
                        {
                            if(leftDirection.second == 0) connectedToEdgeFlag = true;
                            
                            seenSquareCells.insert({leftDirection.first, leftDirection.second});
                            connectedSquaresQueue.push_back({leftDirection.first, leftDirection.second});
                            connectedSquaresVector.push_back({leftDirection.first, leftDirection.second});
                        }
                        
                        if(upDirection.first > -1 and
                           seenSquareCells.find({upDirection.first, upDirection.second}) == seenSquareCells.end() and
                           board[upDirection.first][upDirection.second] == 'O')
                        {
                            if(upDirection.first == 0) connectedToEdgeFlag = true;
                            
                            seenSquareCells.insert({upDirection.first, upDirection.second});
                            connectedSquaresQueue.push_back({upDirection.first, upDirection.second});
                            connectedSquaresVector.push_back({upDirection.first, upDirection.second});
                        }
                        
                        if(rightDirection.second < (int) board[0].size() and
                           seenSquareCells.find({rightDirection.first, rightDirection.second}) == seenSquareCells.end() and
                           board[rightDirection.first][rightDirection.second] == 'O')
                        {
                            if(rightDirection.second == (int) board[0].size() - 1) connectedToEdgeFlag = true;
                            
                            seenSquareCells.insert({rightDirection.first, rightDirection.second});
                            connectedSquaresQueue.push_back({rightDirection.first, rightDirection.second});
                            connectedSquaresVector.push_back({rightDirection.first, rightDirection.second});
                        }
                        
                        if(downDirection.first < (int) board.size() and
                           seenSquareCells.find({downDirection.first, downDirection.second}) == seenSquareCells.end() and
                           board[downDirection.first][downDirection.second] == 'O')
                        {
                            if(downDirection.first == (int) board.size() - 1) connectedToEdgeFlag = true;
                            
                            seenSquareCells.insert({downDirection.first, downDirection.second});
                            connectedSquaresQueue.push_back({downDirection.first, downDirection.second});
                            connectedSquaresVector.push_back({downDirection.first, downDirection.second});
                        }
                    }
                }
                
                if(connectedToEdgeFlag == false) for(pair<int, int> square: connectedSquaresVector) board[square.first][square.second] = 'X';

            }
        }
    }
}
