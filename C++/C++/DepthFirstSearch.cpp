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
    //Problem #133 Clone Graph - Medium
    
    if(node == nullptr) return node;
    
    int initialNodeValue = node->val;
    
    deque<Node*> originalCopyQueue;

    originalCopyQueue.push_back(node);

    unordered_map<int, Node*> nodeMap;
    unordered_set<int> fullyProccessedNodes = {};
    
    while((int)originalCopyQueue.size() > 0)
    {
        int originalCopyQueueSize = (int)originalCopyQueue.size();
        
        for(int index = 0; index < originalCopyQueueSize; index++)
        {
            Node* node0 = originalCopyQueue.front();
            Node* node1;
            
            if(nodeMap[node->val] == nullptr)
            {
                node1 = new Node();
                node1->val = node0->val;
            }
            else
            {
                node1 = nodeMap[node0->val];
            }
            
            if(fullyProccessedNodes.find(originalCopyQueue.front()->val) != fullyProccessedNodes.end())
            {
                node1->neighbors.push_back(nodeMap[originalCopyQueue.front()->val]);
                continue;
            }
            
            originalCopyQueue.pop_front();
            
            for(int index1 = 0; index1 < (int) node0->neighbors.size(); index1++)
            {
                if(nodeMap[node0->neighbors[index1]->val] == nullptr)
                {
                    Node* node2 = new Node();
                    node2->val = node0->neighbors[index1]->val;
                    nodeMap[node2->val] = node2;
                    node1->neighbors.push_back(node2);
                    originalCopyQueue.push_back(node0->neighbors[index1]);
                }
                else
                {
                    node1->neighbors.push_back(nodeMap[node0->neighbors[index1]->val]);
                }
            }
            nodeMap[node1->val] = node1;
            fullyProccessedNodes.insert(node1->val);
        }
    }
    
    return nodeMap[initialNodeValue];
}

void depthFirstSearchPathSumTarget(TreeNode *node, vector<vector<int>> *returnPathLists, vector<int> *pathList, int *sumTarget)
{
    //Problem #113 Path Sum II - Solution Concept by YouTube Channel Deepti Talesra - Understanding the solution
    
    if((node->left == nullptr) and (node->right == nullptr))
    {
        if(*sumTarget - node->val == 0)
        {
            pathList->push_back(node->val);
            vector<int> pathDeepCopy = *pathList;
            returnPathLists->push_back(pathDeepCopy);
            
            pathList->pop_back();
        }
        return;
    }
    
    *sumTarget -= node->val;
    pathList->push_back(node->val);
    
    if(node->left) depthFirstSearchPathSumTarget(node->left, returnPathLists, pathList, sumTarget);
    if(node->right) depthFirstSearchPathSumTarget(node->right, returnPathLists, pathList, sumTarget);
    
    *sumTarget += node->val;
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

bool depthFirstSearchCourseII(int courseNumber, vector<int> &topologyCourseList, set<int> &visited, set<int> &cycle, unordered_map<int, vector<int>> &coursePrerequisteMap)
{
    //Problem 210 Course Schedule II - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    if(cycle.find(courseNumber) != cycle.end())
    {
        return false;
    }
    
    if(visited.find(courseNumber) != visited.end())
    {
        return true;
    }
    
    cycle.insert(courseNumber);
    
    for(int i = 0; i < coursePrerequisteMap[courseNumber].size(); i++)
    {
        if(depthFirstSearchCourseII(coursePrerequisteMap[courseNumber][i],topologyCourseList, visited, cycle, coursePrerequisteMap) == false)
        {
            return false;
        }
    }
    
    cycle.erase(courseNumber);
    visited.insert(courseNumber);
    topologyCourseList.push_back(courseNumber);
    
    return true;
    
}


vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
{
    //Problem 210 Course Schedule II - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
    
    unordered_map<int, vector<int>> coursePrerequisteMap;
    vector<int> topologyCourseList;
    set<int> visited;
    set<int> cycle;
    
    for(int i = 0; i < numCourses; i++)
    {
        coursePrerequisteMap[i] = {};
    }
    
    for(int i = 0; i < prerequisites.size(); i++)
    {
        coursePrerequisteMap[prerequisites[i][0]].push_back(prerequisites[i][1]);
    }
    
    
    for(int i = 0; i < numCourses; i++)
    {
        if(depthFirstSearchCourseII(i, topologyCourseList, visited, cycle, coursePrerequisteMap) == false)
        {
            return {};
        }
    }
    
    return topologyCourseList;
}
