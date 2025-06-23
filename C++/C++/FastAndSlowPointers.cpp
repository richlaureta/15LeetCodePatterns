//
//  FastAndSlowPointers.cpp
//  C++
//
//  Created by Richmond Laureta on 6/6/25.
//

#include "Header.h"
#include <iostream>
#include <unordered_map>

using namespace std;

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
    
    while(fastPointer != nullptr && fastPointer->next != nullptr)
    {
        slowPointer = slowPointer->next;
        fastPointer = fastPointer->next->next;
        
        if(slowPointer == fastPointer)
        {
            cout << "The linked list has a cycle. Do you want to remove the cycle? Enter y for yes and press any key for no. ";
            char input;
            cin >> input;
            if(tolower(input) == 'y')
            {
                removeCycle(head);
                return false;
            }
            
            return true;
        }
    }
    
    return false;
}

void removeCycle(ListNode* head){
    ListNode* behindPointer = head;
    ListNode* pointer = head;
    
    unordered_map<ListNode*, int> addressMap;
    size_t counter = 0;
    
    while(pointer != nullptr)
    {
        addressMap[pointer]++;
        
        if(addressMap[pointer] > 1)
        {
            behindPointer->next = nullptr;
            return;
        }
        
        if(counter != 0)
        {
            behindPointer = behindPointer->next;
        }
        
        pointer = pointer->next;
        counter = 1;
    }
}
