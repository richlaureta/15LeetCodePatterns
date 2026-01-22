//
//  FastAndSlowPointers.cpp
//  C++
//
//  Created by Richmond Laureta on 6/6/25.
//

#include "Header.h"

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
            return true;
        }
    }
    
    return false;
}

bool isHappy(int n)
{
    //Problem #202 Happy Number - Easy
    
    set<int> seen;
    int sum = 0;
    int modulus = n;
    
    while(sum != 1)
    {
        sum = 0;
        while(n > 0)
        {
            modulus = n % 10;
            n = n / 10;
            
            sum += modulus * modulus;
        }
        n = sum;
        if(seen.count(n) > 0)
        {
            return false;
        }
        seen.insert(n);
    }
    
    return true;
}

int findDuplicate(vector<int> &nums)
{
    //Problem #287 Find the Duplicate Number
    
    int slowPointer = nums[0];
    int fastPointer = nums[0];
    
    while(true)
    {
        slowPointer = nums[slowPointer];
        fastPointer = nums[nums[fastPointer]];
        
        if (slowPointer == fastPointer) break;
    }
    
    int pointer1 = nums[0];
    int pointer2 = fastPointer;
    
    while(pointer1 != pointer2)
    {
        pointer1 = nums[pointer1];
        pointer2 = nums[pointer2];
    }
    
    return pointer2;
}
