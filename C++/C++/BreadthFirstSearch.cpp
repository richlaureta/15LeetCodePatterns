//
//  BreadthFirstSearch.cpp
//  C++
//
//  Created by Richmond Laureta on 10/14/25.
//

#include "Header.h"
vector<vector<int>> levelOrderI(TreeNode* root)
{
    //Problem #102 Binary Tree Level Traversal
    
    if(root == nullptr)
    {
        return {};
    }
    
    vector<vector<int>> listReturn;
    
    deque<TreeNode*> myQueue;
    myQueue.push_back(root);
    
    while(!myQueue.empty())
    {
        vector<int> list;
        int queueSize = (int) myQueue.size();
        
        for(int i = 0; i < queueSize; i++)
        {
            list.push_back(myQueue[0]->value);
            TreeNode *node = myQueue[0];
            myQueue.pop_front();
            
            if(node->left != nullptr)
            {
                myQueue.push_back(node->left);
            }
            
            if(node->right != nullptr)
            {
                myQueue.push_back(node->right);
            }
        }
        
        listReturn.push_back(list);
    }
    
    return listReturn;
}
