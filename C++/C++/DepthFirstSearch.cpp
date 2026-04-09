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

    unordered_map<int, Node*> nodeMapCopy;
    unordered_set<int> fullyProccessedNodes = {};
    
    while((int)originalCopyQueue.size() > 0)
    {
        int originalCopyQueueSize = (int)originalCopyQueue.size();
        
        for(int index = 0; index < originalCopyQueueSize; index++)
        {
            Node* node0 = originalCopyQueue.front();
            Node* node1;
            
            if(nodeMapCopy[node->val] == nullptr)
            {
                node1 = new Node();
                node1->val = node0->val;
            }
            else
            {
                node1 = nodeMapCopy[node0->val];
            }
            
            if(fullyProccessedNodes.find(originalCopyQueue.front()->val) != fullyProccessedNodes.end())
            {
                node1->neighbors.push_back(nodeMapCopy[originalCopyQueue.front()->val]);
                continue;
            }
            
            originalCopyQueue.pop_front();
            
            for(int index1 = 0; index1 < (int) node0->neighbors.size(); index1++)
            {
                if(nodeMapCopy[node0->neighbors[index1]->val] == nullptr)
                {
                    Node* node2 = new Node();
                    node2->val = node0->neighbors[index1]->val;
                    nodeMapCopy[node2->val] = node2;
                    node1->neighbors.push_back(node2);
                    originalCopyQueue.push_back(node0->neighbors[index1]);
                }
                else
                {
                    node1->neighbors.push_back(nodeMapCopy[node0->neighbors[index1]->val]);
                }
            }
            nodeMapCopy[node1->val] = node1;
            fullyProccessedNodes.insert(node1->val);
        }
    }
    
    return nodeMapCopy[initialNodeValue];
}

void depthFirstSearchPathSumTarget(TreeNode *node, vector<vector<int>> *returnPathLists, vector<int> *pathList, int *sumTarget, int *sum)
{
    //Problem #113 Path Sum II - Medium
    
    if(node == nullptr) return;
    
    *sum += node->val;
    pathList->push_back(node->val);
    
    if(node->left == nullptr and node->right == nullptr)
    {
        if(*sumTarget == *sum) returnPathLists->push_back(*pathList);
        pathList->pop_back();
        *sum -= node->val;
        return;
    }
    
    depthFirstSearchPathSumTarget(node->left, returnPathLists, pathList, sumTarget, sum);
    depthFirstSearchPathSumTarget(node->right, returnPathLists, pathList, sumTarget, sum);
    
    pathList->pop_back();
    *sum -= node->val;
}

vector<vector<int>> pathSum(TreeNode *root, int targetSum)
{
    //Problem #113 Path Sum II - Medium
    
    int sum = 0;
    vector<vector<int>> pathToTargetSum = {};
    vector<int> path = {};
    
    depthFirstSearchPathSumTarget(root, &pathToTargetSum, &path, &targetSum, &sum);
    
    return pathToTargetSum;
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
    //Problem 210 Course Schedule II - Medium - Solution Concept by Google AI Mode Search - Understanding the Solution
    
    unordered_map<int, vector<int>> prerequsitesToCourse = {};
    vector<int> prerequisitesNeeded(numCourses);
    
    for(vector<int> coursePrerequites: prerequisites)
    {
        prerequsitesToCourse[coursePrerequites[1]].push_back(coursePrerequites[0]);
        prerequisitesNeeded[coursePrerequites[0]]++;
    }
    
    deque<int> courseQueue = {};
    for(int index = 0; index < numCourses; index++)
    {
        if(prerequisitesNeeded[index] == 0) courseQueue.push_back(index);
    }
    
    vector<int> prerequisitesPath = {};
    
    while((int)courseQueue.size() > 0)
    {
        int course = courseQueue.front();
        courseQueue.pop_front();
        prerequisitesPath.push_back(course);
        
        for(int course1: prerequsitesToCourse[course])
        {
            prerequisitesNeeded[course1] -= 1;
            if(prerequisitesNeeded[course1] == 0) courseQueue.push_back(course1);
        }
    }
    
    if((int)prerequisitesPath.size() == numCourses) return prerequisitesPath;
    
    return {};
}
