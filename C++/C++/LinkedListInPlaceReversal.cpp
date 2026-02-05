//
//  LinkedListInPlaceReversal.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/7/25.
//

#include "Header.h"

ListNode* reverseList(ListNode *head)
{
    //Problem #206 Reverse Linked List - Easy
    
    if(head == nullptr) return head;
    
    ListNode *previousNode = nullptr;
    ListNode *currentNode = head;
    ListNode *nextNode = currentNode->next;
    
    while(nextNode != nullptr)
    {
        currentNode->next = previousNode;
        previousNode = currentNode;
        currentNode = nextNode;
        nextNode = nextNode->next;
    }
    
    currentNode->next = previousNode;
    
    return currentNode;
}

ListNode* reverseBetween(ListNode* head, int left, int right)
{
    // Problem #92 Reverse Linked List II
    
    if(left == right) return head;
    
    ListNode *currentNode = head;
    ListNode *leftNode = nullptr;
    int traverseIndex = 0;
    
    while(traverseIndex + 1 < left)
    {
        leftNode = currentNode;
        currentNode = currentNode->next;
        traverseIndex++;
    }
    
    ListNode *pointRightEndNode = currentNode;
    
    ListNode *previousNode = currentNode;
    ListNode *nextNode = currentNode->next;
    while(traverseIndex + 1 < right)
    {
        currentNode = nextNode;
        nextNode = nextNode->next;
        currentNode->next = previousNode;
        previousNode = currentNode;
        traverseIndex++;
    }
    
    pointRightEndNode->next = nextNode;
    
    if(left > 1)
    {
        leftNode->next = currentNode;
        return head;
    }
    
    return currentNode;
}

ListNode* swapPairs(ListNode* head)
{
    //Problem #24 Swap Nodes in Pairs - Medium
    
    if(head == nullptr or head->next == nullptr) return head;
    
    ListNode *currentNode = head;
    
    ListNode *nextNode = currentNode->next;
    ListNode *nextNextNode = nullptr;
    ListNode *previousNode = currentNode;
    bool initialSwapFlag = false;
    
    while(currentNode != nullptr and nextNode != nullptr)
    {
        nextNextNode = nextNode->next;
        currentNode->next = nextNextNode;
        nextNode->next = currentNode;
        currentNode = nextNextNode;
        
        if(initialSwapFlag == true)
        {
            previousNode->next = nextNode;
            previousNode = nextNode->next;
        }
        if(initialSwapFlag == false)
        {
            head = nextNode;
            initialSwapFlag = true;
        }
        if(currentNode != nullptr) nextNode = currentNode->next;
    }
    
    return head;
}

ListNode* swapNodes(ListNode* head, int k)
{
    //Problem 1721 Swapping Nodes in a Linked List - Medium
    
    ListNode *currentNode = head;
    for(int index = 0; index < k - 1; index++) currentNode = currentNode->next;
    
    ListNode *leftSwapPointer = currentNode;
    ListNode *rightSwapPointer = head;
    
    while(currentNode->next)
    {
        rightSwapPointer = rightSwapPointer->next;
        currentNode = currentNode->next;
    }
    
    swap(leftSwapPointer->val, rightSwapPointer->val);
    
    return head;
}
