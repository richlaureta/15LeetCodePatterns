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
#include <unordered_map>
#include <iostream>

using namespace std;

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

void removeCycle(ListNode *head);

ListNode* reverseList(ListNode* head);

std::vector<int> nextGreaterElement(std::vector<int> &nums1, std::vector<int> &nums2);

class MaxHeap
{
private:
    vector<int> Heap;
    
public:
    int parent(int index);
    int leftChildIndex(int index);
    int rightChildIndex(int index);
    void insert(int value);
    int remove();
    void swap(int *index1, int *index2);
    void sinkDown(int index);
    void printHeap();
    size_t getSize();
};

int findKthLargest(vector<int> &nums, int k);

vector<vector<int>> mergeIntervals(vector<vector<int>> &intervals);

struct TreeNode
{
    int value;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int val);

};

void preOrder(TreeNode *node);
void inOrder(TreeNode *node);
void postOrder(TreeNode *node);
vector<vector<int>> levelOrder(TreeNode *node);

int maxVowels(string s, int k);

unordered_map<int, vector<int>> edgeListToMap(vector<vector<int>> edgeList);
void depthFirstSearchList(vector<vector<int>> lists, int rootSource);

int networkDelayTime(vector<vector<int>> &times, int n, int k);

vector<int> twoSum(vector<int>& nums, int target);

vector<int> twoSum2(vector<int>& nums, int target);
vector<int> topKFrequent(vector<int>& nums, int k);
