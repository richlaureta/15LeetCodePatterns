//
//  MatrixTraversalEfficient.cpp
//  C++
//
//  Created by Richmond Laureta on 7/31/25.
//

#include "Header.h"

void breadthFirstSearchEfficient(int rowNumber, int columnNumber, std::vector<std::vector<char>>& grid)
{
    std::queue<std::pair<int, int>> q;
    q.push({rowNumber, columnNumber});
    grid[rowNumber][columnNumber] = '0'; // Mark as visited

    int rows = (int) grid.size();
    int cols = (int) grid[0].size();

    std::vector<std::pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    while(!q.empty())
    {
        int row = q.front().first;
        int col = q.front().second;
        q.pop();

        for(const auto& dir : directions)
        {
            int newRow = row + dir.first;
            int newCol = col + dir.second;

            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == '1')
            {
                q.push({newRow, newCol});
                grid[newRow][newCol] = '0';
            }
        }
    }
}

int numIslandsEfficient(std::vector<std::vector<char>>& grid)
{
    if (grid.empty() || grid[0].empty())
    {
        return 0;
    }

    int islandCount = 0;
    int rows = (int) grid.size();
    int cols = (int) grid[0].size();

    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if (grid[i][j] == '1')
            {
                islandCount++;
                breadthFirstSearchEfficient(i, j, grid);
            }
        }
    }

    return islandCount;
}
