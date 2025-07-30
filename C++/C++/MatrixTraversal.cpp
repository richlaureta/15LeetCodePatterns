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
