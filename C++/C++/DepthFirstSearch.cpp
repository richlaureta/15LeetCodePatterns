//
//  DepthFirstSearch.cpp
//  C++
//
//  Created by Richmond Laureta on 7/2/25.
//

#include "Header.h"
#include <iostream>

unordered_map<int, vector<int>> edgeListToMap(vector<vector<int>> edgeList)
{
    unordered_map<int, vector<int>> myMap;
    
    for(int i = 0; i < edgeList.size(); i++)
    {
        if(myMap.count(edgeList[i][0]) > 0)
        {
            myMap[edgeList[i][0]].push_back(edgeList[i][1]);
        }
        else
        {
            myMap[edgeList[i][0]] = {edgeList[i][1]};
        }
    }
    
    return myMap;
}

void depthFirstSearchList(vector<vector<int>> lists, int rootSource)
{
    if(lists.size() == 0)
    {
        return;
    }
    
    unordered_map<int, vector<int>> myMap = edgeListToMap(lists);
    stack<int> myStack;
    myStack.push(rootSource);
    vector<int> seen = {rootSource};
    
    while(myStack.size() != 0)
    {
        
        int number = myStack.top();
        cout << number << " ";
        myStack.pop();
        
        for(int i = 0; i < myMap[number].size(); i++)
        {
            auto it = find(seen.begin(), seen.end(), myMap[number][i]);
            if(it == seen.end())
            {
                seen.push_back(myMap[number][i]);
                myStack.push(myMap[number][i]);
            }
        }
    }
    
    cout << endl;
}
