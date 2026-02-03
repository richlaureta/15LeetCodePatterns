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
    if((head == nullptr) or head->next == nullptr)
    {
        return head;
    }
    
    ListNode* currentNode = head;
    ListNode* nextNode = currentNode->next;
    ListNode* nextNextNode = nullptr;
    
    if (currentNode->next != nullptr)
    {
        nextNextNode = currentNode->next->next;
    }
    
    bool flag = false;
    
    while(nextNextNode != nullptr)
    {
        ListNode* temporaryNode = currentNode;
        ListNode* temporary2Node = nextNode;
        ListNode* temporary3Node = nextNextNode;
        
        temporary2Node->next = temporaryNode;
        
        if(flag == false)
        {
            flag = true;
            head = temporary2Node;
        }
        
        ListNode* temporary4Node = temporary3Node->next;
        
        currentNode = temporary3Node;
        nextNode = temporary4Node;
        
        if(temporary4Node == nullptr)
        {
            temporaryNode->next = temporary3Node;
            nextNextNode = nullptr;
        }
        else
        {
            nextNextNode = temporary4Node->next;
            
            temporary4Node->next = currentNode;
            temporaryNode->next = temporary4Node;
            currentNode->next = nullptr;
        }
    }
    
    if(flag == false)
    {
        ListNode* temporary2Node = currentNode->next;
        
        temporary2Node->next = currentNode;
        currentNode->next = nullptr;
        head = temporary2Node;
    }
    
    return head;
}
