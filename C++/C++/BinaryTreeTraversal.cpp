//
//  BinaryTreeTraversal.cpp
//  C++
//
//  Created by Richmond Laureta on 6/23/25.
//

#include "Header.h"

TreeNode::TreeNode(int val) : val(val), left(nullptr), right(nullptr){}

void preOrder(TreeNode *node)
{
    if(node == nullptr)
    {
        return;
    }
    
    cout << node->val << " ";
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
    cout << node->val << " ";
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
    cout << node->val << " ";
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
            level.push_back(myQueue.front()->val);
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

void btpPreorderTraversal(TreeNode *node, vector<string> &rootToLeaf, vector<string> &pathToLeaf)
{
    //Problem #257 Binary Tree Paths - Easy
    
    if(node == nullptr) return;
    
    if(node->left == nullptr and node->right == nullptr)
    {
        pathToLeaf.push_back(to_string(node->val));
        rootToLeaf.push_back(accumulate(pathToLeaf.begin(), pathToLeaf.end(), string("")));
        pathToLeaf.pop_back();
        return;
    }
    
    pathToLeaf.push_back(to_string(node->val) + "->");
    
    btpPreorderTraversal(node->left, rootToLeaf, pathToLeaf);
    btpPreorderTraversal(node->right, rootToLeaf, pathToLeaf);
    
    pathToLeaf.pop_back();
}

vector<string> binaryTreePaths(TreeNode *root)
{
    //Problem #257 Binary Tree Paths - Easy
    
    vector<string> rootToLeaf = {};
    vector<string> pathToLeaf = {};
    
    btpPreorderTraversal(root, rootToLeaf, pathToLeaf);
    
    return rootToLeaf;
}

void inOrderTraversal(TreeNode *node, vector<int> &ascendingArray)
{
    //Problem #230 Kth Smallest Element in BST
    
    if(node == nullptr) return;
    
    inOrderTraversal(node->left, ascendingArray);
    ascendingArray.push_back(node->val);
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
    //Problem #104 Maximum Depth of Binary Tree - Easy
    
    if(root == nullptr) return 0;
    
    int depthCount = 0;
    
    deque<TreeNode*> nodeQueue = {root};
    
    while((int)nodeQueue.size() > 0)
    {
        depthCount += 1;
        int nodeQueueSize = (int)nodeQueue.size();
        for(int index = 0; index < nodeQueueSize; index++)
        {
            TreeNode *node = nodeQueue.front();
            nodeQueue.pop_front();
            
            if(node->left != nullptr) nodeQueue.push_back(node->left);
            
            if(node->right != nullptr) nodeQueue.push_back(node->right);
        }
    }
    
    return depthCount;
}

int widthOfBinaryTree(TreeNode *root)
{
    //Problem #662 Maximum Width of Binary Tree - Medium - Solution Concept by YouTube Channel Timoth H Chang
    
    deque<pair<TreeNode*, int>> nodeQueueIndex = {{root, 1}};
    
    int maxWidth = 0;
    
    while((int)nodeQueueIndex.size() > 0)
    {
        int leftIndex = nodeQueueIndex[0].second;
        int rightIndex = nodeQueueIndex[(int)nodeQueueIndex.size() - 1].second;
        
        maxWidth = max(maxWidth, rightIndex - leftIndex + 1);
        
        int nodeQueueIndexSize = (int)nodeQueueIndex.size();
        
        for(int index = 0; index < nodeQueueIndexSize; index++)
        {
            TreeNode* node = nodeQueueIndex.front().first;
            int nodeIndex = nodeQueueIndex.front().second;
            nodeQueueIndex.pop_front();
            if(node->left != nullptr) nodeQueueIndex.push_back({node->left, 2 * nodeIndex});
            if(node->right != nullptr) nodeQueueIndex.push_back({node->right, 2 * nodeIndex + 1});
        }
    }
    
    return maxWidth;
}

int depthFirstSearchSum(TreeNode *node, int *maxSum)
{
    //Problem #124 Binary Tree Maximum Path Sum - Solution Concept by NeetCode - Understanding the Solution
    
    if(node == nullptr)
    {
        return 0;
    }
    
    int leftSum = depthFirstSearchSum(node->left, maxSum);
    int rightSum = depthFirstSearchSum(node->right, maxSum);
    
    leftSum = max(leftSum, 0);
    rightSum = max(rightSum, 0);
    
    *maxSum = max(*maxSum, node->val + leftSum + rightSum);
    
    return node->val + max(leftSum, rightSum);
}

int maxPathSum(TreeNode *root)
{
    //Problem #124 Binary Tree Maximum Path Sum - Solution Concept by NeetCode - Understanding the Solution
    
    int maxSum = INT_MIN;
    depthFirstSearchSum(root, &maxSum);
    return maxSum;
}

vector<vector<int>> levelOrderBottom(TreeNode *root)
{
    //Problem #107 Binary Tree Level Order Traversal II - Medium
    
    if(root == nullptr) return {};
    
    deque<TreeNode*> nodeQueue = {root};
    vector<vector<int>> bottomTopLevelOrderVector = {};
    vector<int> levelValues = {root->val};
    
    while((int)nodeQueue.size() > 0)
    {
        bottomTopLevelOrderVector.push_back(levelValues);
        levelValues = {};
        int nodeQueueSize = (int) nodeQueue.size();
        
        for(int index = 0; index < nodeQueueSize; index++)
        {
            TreeNode *node = nodeQueue.front();
            nodeQueue.pop_front();
            
            if(node->left != nullptr)
            {
                levelValues.push_back(node->left->val);
                nodeQueue.push_back(node->left);
            }
            
            if(node->right != nullptr)
            {
                levelValues.push_back(node->right->val);
                nodeQueue.push_back(node->right);
            }
        }
    }
    
    reverse(bottomTopLevelOrderVector.begin(), bottomTopLevelOrderVector.end());
    
    return bottomTopLevelOrderVector;
}
