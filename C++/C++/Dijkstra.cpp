//
//  Dijkstra.cpp
//  C++
//
//  Created by Richmond Laureta on 7/18/25.
//

#include "Header.h"

int networkDelayTime(vector<vector<int>> &times, int n, int k)
{
    //Problem #743 Network Delay Time
    
    unordered_map<int, vector<vector<int>>> adjacentVertex;

    for(int i = 0; i < times.size() ; ++i)
    {
        adjacentVertex[times[i][0]].push_back({times[i][1], times[i][2]});
    }
    
    unordered_map<int, int> shortestPath;

    auto cmp = [](const vector<int>& a, const vector<int>& b)
    {
            return a[0] > b[0];
    };

    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> minHeap(cmp);
    minHeap.push({0, k});
    
    while(!minHeap.empty())
    {
        int weight0 = minHeap.top()[0];
        int node0 = minHeap.top()[1];

        minHeap.pop();
        
        if(shortestPath.find(node0) != shortestPath.end())
        {
            continue;
        }
        
        shortestPath[node0] = weight0;
    
        for(int i = 0; i < adjacentVertex[node0].size(); ++i)
        {
            int weight1 = adjacentVertex[node0][i][1];
            int node1 = adjacentVertex[node0][i][0];
            
            if(shortestPath.find(node1) == shortestPath.end())
            {
                minHeap.push({weight0 + weight1, node1});
            }
            
        }
    }
    
    if (shortestPath.size() == n)
    {
        int maxTime = 0;
        for (const auto& [_, time] : shortestPath)
        {
            maxTime = max(maxTime, time);
        }
        return maxTime;
    }

    return -1;
}
