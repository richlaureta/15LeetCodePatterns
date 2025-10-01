//
//  DepthFirstSearch.cpp
//  C++
//
//  Created by Richmond Laureta on 7/2/25.
//

#include "Header.h"

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

unordered_map<Node*, Node*> originalAndCopy;

Node* cloneGraph(Node* node)
{
    //Problem #133 Clone Graph - Solution Concept by YouTube Channel Sean Chuah - Understanding the Solution
    
    if(node == nullptr) return nullptr;
    
    Node* nodeCopy = new Node(node->val);
    
    if(node->neighbors.size() == 0) return nodeCopy;
    
    vector<Node*> neighborsHere;
    
    originalAndCopy[node] = nodeCopy;
    
    for(auto& point: node->neighbors)
    {
        if(originalAndCopy.find(point) != originalAndCopy.end())
        {
            neighborsHere.push_back(originalAndCopy[point]);
        }
        else
        {
            neighborsHere.push_back(cloneGraph(point));
        }
    }
    
    nodeCopy->neighbors = neighborsHere;
    
    return nodeCopy;
}

void depthFirstSearchPathSumTarget(TreeNode *node, vector<vector<int>> *returnPathLists, vector<int> *pathList, int *sumTarget)
{
    //Problem #113 Path Sum II - Solution Concept by YouTube Channel Deepti Talesra - Understanding the solution
    
    if((node->left == nullptr) and (node->right == nullptr))
    {
        if(*sumTarget - node->value == 0)
        {
            pathList->push_back(node->value);
            vector<int> pathDeepCopy = *pathList;
            returnPathLists->push_back(pathDeepCopy);
            
            pathList->pop_back();
        }
        return;
    }
    
    *sumTarget -= node->value;
    pathList->push_back(node->value);
    
    if(node->left) depthFirstSearchPathSumTarget(node->left, returnPathLists, pathList, sumTarget);
    if(node->right) depthFirstSearchPathSumTarget(node->right, returnPathLists, pathList, sumTarget);
    
    *sumTarget += node->value;
    pathList->pop_back();
    
    return;
}

vector<vector<int>> pathSum(TreeNode *root, int targetSum)
{
    //Problem #113 Path Sum II - Solution Concept by YouTube Channel Deepti Talesra - Understanding the solution
    
    if(root == nullptr)
    {
        return {};
    }
    vector<vector<int>> returnPathLists;
    vector<int> pathList;
    
    depthFirstSearchPathSumTarget(root, &returnPathLists, &pathList, &targetSum);
    
    return returnPathLists;
}

bool isThereCycle(int courseNumber, set<int> *visited, unordered_map<int, vector<int>> &courseMap)
{
    //Problem 207 Course Schedule - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    
    if(visited->count(courseNumber) > 0)
    {
        return true;
    }
    
    visited->insert(courseNumber);
    
    for(int i = 0; i < courseMap[courseNumber].size(); i++)
    {
        if(isThereCycle(courseMap[courseNumber][i], visited, courseMap))
        {
            return true;
        }
    }
    
    courseMap[courseNumber] = {};
    visited->erase(courseNumber);
    
    return false;
}

bool canFinish(int numCourses, vector<vector<int>> prerequisites)
{
    //Problem 207 Course Schedule - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
    unordered_map<int, vector<int>> courseMap;
    
    for(int i = 0; i < prerequisites.size(); i++)
    {
        courseMap[prerequisites[i][0]].push_back(prerequisites[i][1]);
    }
    
    set<int> visited;
    
    for(int i = 0; i < numCourses; i++)
    {
        if(isThereCycle(i, &visited, courseMap))
        {
            return false;
        }
    }
    
    return true;
}
