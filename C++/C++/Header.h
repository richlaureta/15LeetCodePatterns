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
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <optional>
#include <functional>
#include <tuple>

using namespace std;

bool isAnagram(std::string s, std::string t);

double findMaxAverage(std::vector<int> &nums, int k);

struct ListNode
{
    int val;
    ListNode *next;
    
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
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
int numIslands(vector<vector<char>>& grid);
int numIslandsEfficient(vector<vector<char>>& grid);
vector<vector<int>> subsets(vector<int> &nums);
vector<vector<int>> subsetsEfficient(vector<int> &nums);
string reverseWords(string s);
int fib(int n);
int findMaxLength(vector<int> &nums);
int subArraySum(vector<int> &nums, int k);
vector<vector<int>> threeSum(vector<int> &nums);
int maxArea(vector<int> &height);
int lengthOfLongestSubstring(string s);
string minWindow(string s, string t);
bool isHappy(int n);
int findDuplicate(vector<int> &nums);
ListNode* reverseBetween(ListNode* head, int left, int right);
ListNode* swapPairs(ListNode* head);
vector<int> dailyTemperatures(vector<int>& temperatures);
int largestRectangleArea(vector<int> &heights);
vector<vector<int>> kSmallestPairs(vector<int> &nums1, vector<int> &nums2, int k);
vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval);
int eraseOverlapIntervals(vector<vector<int>> &intervals);
