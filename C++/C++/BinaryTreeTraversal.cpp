//
//  BinaryTreeTraversal.cpp
//  C++
//
//  Created by Richmond Laureta on 6/23/25.
//

#include "Header.h"

TreeNode::TreeNode(int val) : value(val), left(nullptr), right(nullptr){}

void preOrder(TreeNode *node)
{
    if(node == nullptr)
    {
        return;
    }
    
    cout << node->value << " ";
    preOrder(node->left);
    preOrder(node->right);
}

void inOrder(TreeNode *node)
{
    if(node == nullptr)
    {
        return;
    }
    
    inOrder(node->left);
    cout << node->value << " ";
    inOrder(node->right);
}


void postOrder(TreeNode *node)
{
    if(node == nullptr)
    {
        return;
    }
    
    postOrder(node->left);
    postOrder(node->right);
    cout << node->value << " ";
}

vector<vector<int>> levelOrder(TreeNode *node)
{
//Problem #102 Binary Tree Level Order Traversal
    
    if(node == nullptr)
    {
        return {};
    }
    vector<vector<int>> myList;
    queue<TreeNode*> myQueue;
    
    myQueue.push(node);
    
    while(!myQueue.empty())
    {
        vector<int> level;
        size_t length = myQueue.size();
        for(size_t i = 0; i < length; i++)
        {
            level.push_back(myQueue.front()->value);
            TreeNode *nodeCopy = myQueue.front();
            myQueue.pop();
            
            if(nodeCopy->left != nullptr) {myQueue.push(nodeCopy->left);}
            if(nodeCopy->right != nullptr) {myQueue.push(nodeCopy->right);}
        }
        length = myQueue.size();
        myList.push_back(level);
    }
    return myList;
}

void depthFirstSearch(TreeNode *node, vector<string> &currentPath, vector<string> &listResult)
{
    //Problem #257 Binary Tree Paths - Algo.monster Concept Solution
    
    if(node == nullptr)
    {
        return;
    }
    
    currentPath.push_back(to_string(node->value));
    
    if ((node->left == nullptr) and (node->right == nullptr))
    {
        string concatenatedString = "";
        for(int i = 0; i < currentPath.size(); i++)
        {
            if(i < currentPath.size() - 1)
            {
                concatenatedString += currentPath[i] + "->";
            }
            else concatenatedString += currentPath[i];
        }
        
        listResult.push_back(concatenatedString);
    }
    else
    {
        depthFirstSearch(node->left, currentPath, listResult);
        depthFirstSearch(node->right, currentPath, listResult);
    }
    
    currentPath.pop_back();
}

vector<string> binaryTreePaths(TreeNode *root)
{
    //Problem #257 Binary Tree Paths - Algo.monster Concept Solution
    
    vector<string> listResult;
    vector<string> currentPath;
    
    depthFirstSearch(root, currentPath, listResult);
    
    return listResult;
}

void inOrderTraversal(TreeNode *node, vector<int> &ascendingArray)
{
    //Problem #230 Kth Smallest Element in BST
    
    if(node == nullptr) return;
    
    inOrderTraversal(node->left, ascendingArray);
    ascendingArray.push_back(node->value);
    inOrderTraversal(node->right, ascendingArray);
}

int kthSmallest(TreeNode *root, int k)
{
    //Problem #230 Kth Smallest Element in BST
    
    vector<int> ascendingArray;
    inOrderTraversal(root, ascendingArray);
    return ascendingArray[k - 1];
}

int maxDepth(TreeNode* root)
{
    //Problem #104 Maximum Depth of Binary Tree - Solution concept by Greg Hogg
    
    if(root == nullptr) return 0;
    
    int leftDepthCount = maxDepth(root->left);
    int rightDepthCount = maxDepth(root->right);
    
    return 1 + max(leftDepthCount, rightDepthCount);
}

int widthOfBinaryTree(TreeNode *root)
{
    //Problem #662 Maximum Width of Binary Tree - Solution Concept by YouTuber NeetCodeIO - Understanding the Solution
    
    unsigned int width = 0;
    unsigned int previousLevel = 0;
    unsigned int previousNumber = 1;
    
    queue<TreeNode*> nodeQueues;
    queue<vector<unsigned int>> numbersAndLevels;
    
    nodeQueues.push(root);
    numbersAndLevels.push({1, 0});
    
    
    while(nodeQueues.size() != 0)
    {
        TreeNode* node = nodeQueues.front();
        nodeQueues.pop();
        unsigned int number = numbersAndLevels.front()[0];
        unsigned int level = numbersAndLevels.front()[1];
        numbersAndLevels.pop();
        
        if (level > previousLevel)
        {
            previousLevel = level;
            previousNumber = number;
        }
        
        width = max(width, number - previousNumber + 1);
        
        if(node->left != nullptr)
        {
            nodeQueues.push(node->left);
            numbersAndLevels.push({number * 2, level + 1});
        }
        
        if(node->right != nullptr)
        {
            nodeQueues.push(node->right);
            numbersAndLevels.push({(number * 2) + 1, level + 1});
        }
    }
    
    return (int) width;
}
