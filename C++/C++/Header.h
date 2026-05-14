//
//  Header.h
//  C++
//
//  Created by Richmond Laureta on 6/4/25.
//
#pragma once

#ifndef Header_h
#define Header_h

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <optional>
#include <functional>
#include <tuple>
#include <climits>
#include <cmath>
#include <numeric>
#include <utility>
#include <cctype>

using namespace std;

//Prefix Sum

class NumArray
{
public:
    vector<int> prefixSumArray;
    NumArray(vector<int> &nums);
    int sumRange(int leftPointer, int rightPointer);
}; //Problem #303 Range Sum Query - Easy

int findMaxLength(vector<int> &nums); //Problem #525 Contiguous Array - Medium

int subArraySum(vector<int> &nums, int k); //Problem #560 Subarray Sum Equals K - Medium

//Two Pointers

vector<int> twoSum(vector<int>& nums, int target); //Problem #167 Two Sum II - Medium
vector<int> twoSum2(vector<int>& nums, int target); //Problem #167 Two Sum II - Medium

vector<vector<int>> threeSum(vector<int> &nums); //Problem #15 3 Sum - Medium

int maxArea(vector<int> &height); //Problem #11 Container With Most Water - Medium

//Sliding Window

double findMaxAverage(std::vector<int> &nums, int k); //Problem #643 Maximum Average Subarray I - Easy

int lengthOfLongestSubstring(string s); //Problem #3 Longest Substring Without Repeating Characters - Medium

string minWindow(string s, string t); //Problem #76 Minimum Window Substring - Hard

//Fast and Slow Pointers

struct ListNode
{
    int val;
    ListNode *next;
    
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode (int x, ListNode *next): val(x), next(next){}
};


bool hasCycle(ListNode *head); //Problem #141 Linked List Cycle - Easy

bool isHappy(int n); //Problem #202 Happy Number - Easy

int findDuplicate(vector<int> &nums); //Problem #287 Find the Duplicate Number - Medium

//Linked List In-Place Reversal

ListNode* reverseList(ListNode* head); //Problem #206 Reverse Linked List - Easy

ListNode* reverseBetween(ListNode* head, int left, int right); //Problem #92 Reverse Linked List II - Medium

ListNode* swapPairs(ListNode* head); //Problem #24 Swap Nodes in Pairs - Medium

//Monotonic Stack

vector<int> nextGreaterElement(std::vector<int> &nums1, std::vector<int> &nums2); //Problem #496 Next Greater Element I - Easy

vector<int> dailyTemperatures(vector<int>& temperatures); //Problem #739 Daily Temperatures - Medium

int largestRectangleArea(vector<int> &heights); //Problem #84 Largest Rectangle in Histogram - Hard

//Top K Elements or Min/Max Heap

int findKthLargest(vector<int> &nums, int k); //Problem #215 Kth Largest Element in an Array - Medium

vector<int> topKFrequent(vector<int>& nums, int k); //Problem #347 Top K Frequent Element - Medium

vector<vector<int>> kSmallestPairs(vector<int> &nums1, vector<int> &nums2, int k); //Problem #373 Find K Pairs with Smallest Sums - Medium

//Overlapping Intervals

vector<vector<int>> merge(vector<vector<int>> &intervals); //Problem #56 Merge Intervals - Medium

vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval); // Problem #57 Insert Interval - Medium

int eraseOverlapIntervals(vector<vector<int>> &intervals); // Problem #435 Non-Overlapping Intervals - Medium

//Modified Binary Search

int modifiedBinarySearch(vector<int> &nums, int target); //Problem #33 Search in Rotated Sorted Array - Medium

int findMin(vector<int> &nums); //Problem #153 Find Minimum in Rotated Sorted Array - Medium

bool searchMatrix(vector<vector<int>> &matrix, int target); //Problem #240 Search a 2D Matrix II - Medium

//Binary Tree Traversal

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int val);
};

vector<string> binaryTreePaths(TreeNode *root); //Problem #257 Binary Tree Paths - Easy

int kthSmallest(TreeNode *root, int k); //Problem #230 Kth Smallest Element in a BST - Medium

int maxPathSum(TreeNode *root); //Problem #124 Binary Tree Maximum Path Sum - Hard

vector<vector<int>> levelOrderBottom(TreeNode *root); //Problem #107 Binary Tree Level Order Traversal II - Medium


//Depth First Search

class Node {
public:
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

Node* cloneGraph(Node* node); //Problem #133 Clone Graph - Medium

vector<vector<int>> pathSum(TreeNode *root, int targetSum); //Problem #113 Path Sum II - Medium

vector<int> findOrder(int numCourse, vector<vector<int>> &prerequisites); //Problem #210 Course Schedule II - Medium

//Breadth First Search

vector<vector<int>> levelOrder(TreeNode *node); //Problem #102 Binary Tree Level Order Traversal - Medium

int orangesRotting(vector<vector<int>> &grid); //Problem #994 Rotting Oranges - Medium

int ladderLength(string beginWord, string endWord, vector<string> &wordList); //Problem #127 Word Ladder - Hard

//Matrix Traversal

vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color); //Problem #733 Flood Fill - Easy

int numIslands(vector<vector<char>>& grid); //Problem #200 Number of Islands - Medium

void solve(vector<vector<char>> &board); //Problem #130 Surrounded Regions - Medium

//Backtracking

vector<vector<int>> permute(vector<int> &nums); //Problem #46 Permutations - Medium

vector<vector<int>> subsets(vector<int> &nums); //Problem #78 Subsets - Medium

vector<vector<string>> solveNQueens(int n);
void depthFirstSearchQueens(int row0,
                            int nSize,
                            unordered_set<int> &columnSet,
                            unordered_set<int> &positiveDiagonalSet,
                            unordered_set<int> &negativeDiagonalSet,
                            vector<vector<string>> &possibleQueenCombinations,
                            vector<vector<char>> &board); // Problem #51 N-Queens - Hard

//Dynamic Programming

int climbStairs(int n); //Problem #70 Climbing Stairs - Easy

int coinChange(vector<int> &coins, int amount); //Problem #322 Coin Change - Medium

int lengthOfLIS(vector<int> &nums); //Problem #300 Longest Increasing Subsequence - Medium

bool canPartition(vector<int> &nums); //Problem #416 Partition Equal Subset Sum - Medium

struct PairHash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1, T2>& p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        return h1 ^ (h2 << 1);
    }
};
int maxCoins(vector<int> &nums);
int depthFirstSearchCoins(int leftPointer, int rightPointer, vector<int> &nums, unordered_map<pair<int,int>, int, PairHash> &coinMap); //Problem #312 Burst Balloons - Hard

int longestCommonSubsequence(string text1, string text2); //Problem #1143 Longest Common Subsequence - Medium

//Miscelaneous

bool isAnagram(std::string s, std::string t);

class LinkedList
{
private:
    ListNode *Head = NULL;
    
public:
    void insertNode(ListNode *node);
    
    void printLinkedList();
};

void removeCycle(ListNode *head);

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

void preOrder(TreeNode *node);
void inOrder(TreeNode *node);
void postOrder(TreeNode *node);

int maxVowels(string s, int k);

unordered_map<int, vector<int>> edgeListToMap(vector<vector<int>> edgeList);
void depthFirstSearchList(vector<vector<int>> lists, int rootSource);
int networkDelayTime(vector<vector<int>> &times, int n, int k);
vector<int> topKFrequent(vector<int>& nums, int k);
int numIslandsEfficient(vector<vector<char>>& grid);
vector<vector<int>> subsetsEfficient(vector<int> &nums);
string reverseWords(string s);
int fib(int n);
bool searchMatrix(vector<vector<int>> &matrix, int target);
void btpPreorderTraversal(TreeNode *node, vector<string> &rootToLeaf, vector<string> &pathToLead);
void inOrderTraversal(TreeNode *node);
int maxDepth(TreeNode* root);
int widthOfBinaryTree(TreeNode *root);
int depthFirstSearchSum(TreeNode *node, int *maxSum);
void depthFirstSearchPathSumTarget(TreeNode *node, vector<vector<int>> *returnPathLists, vector<int> *pathList, int *sumTarget, int *sum);
bool canFinish(int numCourses, vector<vector<int>> prerequisites);
bool isThereCycle(int courseNumber, set<int> *visited, unordered_map<int, vector<int>> &courseMap);
bool depthFirstSearchCourseII(int courseNumber, vector<int> &topologyCourseList, set<int> &visited, set<int> &cycle, unordered_map<int, vector<int>> &coursePrerequisteMap);
vector<vector<int>> levelOrderI(TreeNode *root);
void depthFirstSearchPermutation(vector<int> &partialSolution, vector<vector<int>> &answer, vector<int> &nums, unordered_set<int> &numberSet);
void depthFirstSearchSubsets(int index, vector<int>& nums, vector<int>& partialSolution, vector<vector<int>>& answer);
int fib1(int n);
int fibonacciFormula(int n);
int fib2(int n);
int functionNumber(int n, unordered_map<int, int> &sequenceMap);
int functionNumber1(int number, unordered_map<int, int> &waysMap);
int climbStairs1(int n);
int minimumCoins(vector<int> &coins, unordered_map<int, int> &coinsMap, int numberAmount);
int coinChange1(vector<int> &coins, int amount);
int lengthOfLIS1(vector<int> &nums);
int maxCoins1(vector<int> &nums);
bool isPalindrome(string s);
int recursion0(int n);
int recursion1(int n);
int countGoodSubstrings(string s);
vector<int> runningSum(vector<int> &nums);
vector<int> leftRightDifference(vector<int> &nums);
int countPairs(vector<int> &nums, int target);
int countPartitions(vector<int> &nums);
vector<int> minOperations(string boxes);
int subArray(vector<int> &nums);
int garbageCollection(vector<string> &garbage, vector<int> &travel);
string reversePrefix(string word, char ch);
string reversePrefix0(string s, int k);
vector<int> pivotArray(vector<int> &nums, int pivot);
bool isStrictlyPalindromic(int n);
vector<int> decrypt(vector<int> &code, int k);
int countKConstraintSubstrings(string s, int k);
int minOperations1(vector<int> &nums);
ListNode *swapNodes(ListNode *head, int k);
bool isValidSudoku(vector<vector<char>> &board);

#endif // !Header_h
