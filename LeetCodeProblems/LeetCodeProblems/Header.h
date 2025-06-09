//
//  Header.h
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//

#ifndef Header_h
#define Header_h


#endif /* Header_h */
#include <string>
#include <vector>

bool isAnagram(std::string s, std::string t);

double findMaxAverage(std::vector<int> &nums, int k);

struct ListNode
{
    int val;
    ListNode *next;
    
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
    ListNode (int x, ListNode *next): val(x), next(next){}
};

class LinkedList
{
private:
    ListNode *Head = NULL;
    
public:
    void insertNode(ListNode *node);
    
    void printLinkedList();
};

bool hasCycle(ListNode *head);

ListNode* reverseList(ListNode* head);
