//
//  FastAndSlowPointers.cpp
//  C++
//
//  Created by Richmond Laureta on 6/6/25.
//

#include "Header.h"
#include <iostream>

void LinkedList::insertNode(ListNode *node)
{
    if(Head == NULL)
    {
        Head = node;
        return;
    }
    
    ListNode *currentNode = Head;
    
    while(currentNode->next != NULL)
    {
        currentNode = currentNode->next;
    }
    
    currentNode->next = node;
}

void LinkedList::printLinkedList()
{
    if(Head == NULL)
    {
        std::cout << "NULL" << std::endl;
        return;
    }
    
    ListNode *currentNode = Head;
    
    while(currentNode != NULL)
    {
        std::cout << currentNode->val << " -> ";
        currentNode = currentNode->next;
    }
    
    
    std::cout << "NULL" << std::endl;
}

bool hasCycle (ListNode *head)
{
    ListNode *slowPointer = head;
    ListNode *fastPointer = head;
    
    while(fastPointer != NULL && fastPointer->next != NULL)
    {
        slowPointer = slowPointer->next;
        fastPointer = fastPointer->next->next;
        
        if(slowPointer == fastPointer)
        {
            return true;
        }
    }
    
    return false;
}
