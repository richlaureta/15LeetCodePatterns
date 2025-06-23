//
//  BinaryTreeTraversal.cpp
//  C++
//
//  Created by Richmond Laureta on 6/23/25.
//

#include "Header.h"
#include <iostream>

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
