//
//  main.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/7/25.
//
#include "Header.h"

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
//    //Anagram Problem
//    string s = "anagram";
//    string t = "nagaram";
//    
//    cout << "The strings " << s << " and " << t << " are ";
//    
//    if(isAnagram(s, t) == 1)
//    {
//        cout << "Anagrams!" << endl;
//    }
//    else
//    {
//        cout << "not Anagrams!" << endl;
//    }
//    
//    //Maximum Subarray Average I Problem
//    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//    int k = 4;
//    
//    cout << findMaxAverage(arr, k) << endl;
//    
//    //Linked List Cycle Problem
//    ListNode node0 = ListNode(3);
//    ListNode node1 = ListNode(2);
//    ListNode node2 = ListNode(0);
//    ListNode node3 = ListNode(-4);
//    
//    LinkedList linkedList0;
//    
//    linkedList0.insertNode(&node0);
//    linkedList0.insertNode(&node1);
//    linkedList0.insertNode(&node2);
//    linkedList0.insertNode(&node3);
//    linkedList0.insertNode(&node1);
//    
//    if(hasCycle(&node0) == 1)
//    {
//        std::cout << "The linked list has a cycle." << std::endl;
//    }
//    else
//    {
//        std::cout << "The linked list is not a cycle." << std::endl;
//    }
//    
//    removeCycle(&node0);
//    
//    if(hasCycle(&node0) == 1)
//    {
//        std::cout << "The linked list has a cycle." << std::endl;
//    }
//    else
//    {
//        std::cout << "The linked list is not a cycle." << std::endl;
//    }
//    
//    linkedList0.printLinkedList();
//    //Problem #206 Reverse Linked List
//    
//    reverseList(&node0);
//    ListNode* currentNode = &node0;
//    
//    while(currentNode->next != nullptr)
//    {
//        std::cout << currentNode->val << std::endl;
//        currentNode = currentNode->next;
//    }
//    
//    //Problem #496 Next Greater Element I
//    
//    vector<int> nums1 = {4, 1, 2};
//    vector<int> nums2 = {1, 3, 4, 2};
//    
//    nextGreaterElement(nums1, nums2);
    
    //Accessing Heaps
//    MaxHeap myMaxHeap;
//    
//    myMaxHeap.insert(100);
//    myMaxHeap.insert(75);
//    myMaxHeap.insert(80);
//    myMaxHeap.insert(55);
//    myMaxHeap.insert(50);
//    myMaxHeap.insert(60);
//    
//    myMaxHeap.printHeap();
//    
//    myMaxHeap.remove();
//    
//    myMaxHeap.printHeap();
    
    //Find Kth Largest
//    vector<int> nums = {3,2,3,1,2,4,5,5,6};
//    int k = 4;
//    cout << findKthLargest(nums, k) << endl;
    
    
    //Overlapping Intervals
//    vector<vector<int>> listsOfLists = {{1, 3}, {2, 6}, {15, 18}, {8, 10}};
//    
////    vector<vector<int>> listsOfLists = {{1, 4}, {4, 5}};
//    vector<vector<int>> mergedLists = mergeIntervals(listsOfLists);
//    
//    for(size_t i = 0; i < mergedLists.size(); ++i)
//    {
//        for(size_t j = 0; j < mergedLists[i].size(); ++j)
//        {
//            cout << mergedLists[i][j] << " ";
//        }
//        cout << endl;
//    }
    
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(1);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(0);
    root->left->right = new TreeNode(2);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(6);
    
    preOrder(root);
    cout << endl;
    inOrder(root);
    cout << endl;
    postOrder(root);
    cout << endl;
    return EXIT_SUCCESS;
}
