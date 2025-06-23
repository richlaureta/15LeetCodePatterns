//
//  LinkedListInPlaceReversal.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/7/25.
//

#include "Header.h"
#include <iostream>

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
