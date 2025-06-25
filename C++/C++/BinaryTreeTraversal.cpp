//
//  BinaryTreeTraversal.cpp
//  C++
//
//  Created by Richmond Laureta on 6/23/25.
//

#include "Header.h"
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

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
