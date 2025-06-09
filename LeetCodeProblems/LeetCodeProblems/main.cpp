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
    //Anagram Problem
    string s = "anagram";
    string t = "nagaram";
    
    cout << "The strings " << s << " and " << t << " are ";
    
    if(isAnagram(s, t) == 1)
    {
        cout << "Anagrams!" << endl;
    }
    else
    {
        cout << "not Anagrams!" << endl;
    }
    
    //Maximum Subarray Average I Problem
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int k = 4;
    
    cout << findMaxAverage(arr, k) << endl;
    
    //Linked List Cycle Problem
    ListNode node0 = ListNode(3);
    ListNode node1 = ListNode(2);
    ListNode node2 = ListNode(0);
    ListNode node3 = ListNode(-4);
    
    LinkedList linkedList0;
    
    linkedList0.insertNode(&node0);
    linkedList0.insertNode(&node1);
    linkedList0.insertNode(&node2);
    linkedList0.insertNode(&node3);
    
    if(hasCycle(&node0) == 1)
    {
        std::cout << "The linked list has a cycle." << std::endl;
    }
    else
    {
        std::cout << "The linked list is not a cycle." << std::endl;
    }
    
    //Problem #206 Reverse Linked List
    
    reverseList(&node0);
    ListNode* currentNode = &node0;
    
    while(currentNode->next != nullptr)
    {
        std::cout << currentNode->val << std::endl;
        currentNode = currentNode->next;
    }
    
    //Problem #496 Next Greater Element I
    
    vector<int> nums1 = {4, 1, 2};
    vector<int> nums2 = {1, 3, 4, 2};
    
    nextGreaterElement(nums1, nums2);
    
    return EXIT_SUCCESS;
}
