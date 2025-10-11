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
#include <climits>

using namespace std;


class Node {
public:
    //LeetCode Definition of Node Problem #133 Clone Graph
    
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

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
int modifiedBinarySearch(vector<int> &nums, int target);
int findMin(vector<int> &nums);
bool searchMatrix(vector<vector<int>> &matrix, int target);
void depthFirstSearch(TreeNode *node, vector<string> &currentPath, vector<string> &resultList);
vector<string> binaryTreePaths(TreeNode *root);
int kthSmallest(TreeNode *root, int k);
void inOrderTraversal(TreeNode *node);
int maxDepth(TreeNode* root);
int widthOfBinaryTree(TreeNode *root);
int maxPathSum(TreeNode *root);
int depthFirstSearchSum(TreeNode *node, int *maxSum);
vector<vector<int>> levelOrderBottom(TreeNode *root);
Node* cloneGraph(Node* node);
vector<vector<int>> pathSum(TreeNode *root, int targetSum);
void depthFirstSearchPathSumTarget(TreeNode *node, vector<vector<int>> *returnPathLists, vector<int> *pathList, int *sumTarget);
bool canFinish(int numCourses, vector<vector<int>> prerequisites);
bool isThereCycle(int courseNumber, set<int> *visited, unordered_map<int, vector<int>> &courseMap);
vector<int> findOrder(int numCourse, vector<vector<int>> &prerequisites);
bool depthFirstSearchCourseII(int courseNumber, vector<int> &topologyCourseList, set<int> &visited, set<int> &cycle, unordered_map<int, vector<int>> &coursePrerequisteMap);
