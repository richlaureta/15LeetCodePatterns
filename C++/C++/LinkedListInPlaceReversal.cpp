//
//  LinkedListInPlaceReversal.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/7/25.
//

#include "Header.h"

ListNode* reverseList(ListNode *head)
{
    ListNode* previousNode = head;
    ListNode* currentNode = head;
    ListNode* nextNode = head->next;
    
    currentNode->next = nullptr;
    
    while (nextNode != nullptr)
    {
//        std::cout << currentNode->val << std::endl;
        currentNode = nextNode;
        nextNode = nextNode->next;
        currentNode->next = previousNode;
        previousNode = currentNode;
    }
    
    return currentNode;
}

ListNode* reverseBetween(ListNode* head, int left, int right)
{
    // Problem #92 Reverse Linked List II
    
    ListNode* currentNode = head;
    ListNode* rememberLeftNode = nullptr;
    ListNode* rememberReversedLeftNode = nullptr;
    int leftIndex = 1;
    
    while(currentNode != nullptr)
    {
        if(leftIndex + 1 == left)
        {
            rememberLeftNode = currentNode;
            rememberReversedLeftNode = currentNode->next;
        }
        
        if(leftIndex == left)
        {
            ListNode* previousNode = nullptr;
            ListNode* nextNode = currentNode->next;
            
            while(leftIndex != right)
            {
                currentNode->next = previousNode;
                previousNode = currentNode;
                currentNode = nextNode;
                nextNode = nextNode->next;
                leftIndex++;
            }
            currentNode->next = previousNode;
            
            if(rememberLeftNode == nullptr)
            {
                head->next = nextNode;
                head = currentNode;
            }
            else
            {
                rememberLeftNode->next = currentNode;
            }
            
            if(rememberReversedLeftNode != nullptr)
            {
                rememberReversedLeftNode->next = nextNode;
            }
            
            return head;
        }
        
        currentNode = currentNode->next;
        leftIndex++;
    }
    return head;
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
