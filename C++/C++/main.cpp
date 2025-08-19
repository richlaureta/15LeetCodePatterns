//
//  main.cpp
//  LeetCodeProblems
//
//  Created by Richmond Laureta on 6/7/25.
//
#include "Header.h"

int main(int argc, const char * argv[]) {
    //    //Anagram Problem
    //    string s = "anagram";
    //    string t = "nagaram";
    //
    //    cout << "The strings " << s << " and " << t << " are ";
    //
    //    if(isAnagram(s, t) == 1)
    //    {
    //        cout << "Anagrams!" << endl;
    //    }
    //    else
    //    {
    //        cout << "not Anagrams!" << endl;
    //    }
    //
    //    //Maximum Subarray Average I Problem
    //    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    //    int k = 4;
    //
    //    cout << findMaxAverage(arr, k) << endl;
    //
    //    //Linked List Cycle Problem
    //    ListNode node0 = ListNode(3);
    //    ListNode node1 = ListNode(2);
    //    ListNode node2 = ListNode(0);
    //    ListNode node3 = ListNode(-4);
    //
    //    LinkedList linkedList0;
    //
    //    linkedList0.insertNode(&node0);
    //    linkedList0.insertNode(&node1);
    //    linkedList0.insertNode(&node2);
    //    linkedList0.insertNode(&node3);
    //    linkedList0.insertNode(&node1);
    //
    //    if(hasCycle(&node0) == 1)
    //    {
    //        std::cout << "The linked list has a cycle." << std::endl;
    //    }
    //    else
    //    {
    //        std::cout << "The linked list is not a cycle." << std::endl;
    //    }
    //
    //    removeCycle(&node0);
    //
    //    if(hasCycle(&node0) == 1)
    //    {
    //        std::cout << "The linked list has a cycle." << std::endl;
    //    }
    //    else
    //    {
    //        std::cout << "The linked list is not a cycle." << std::endl;
    //    }
    //
    //    linkedList0.printLinkedList();
    //    //Problem #206 Reverse Linked List
    //
    //    reverseList(&node0);
    //    ListNode* currentNode = &node0;
    //
    //    while(currentNode->next != nullptr)
    //    {
    //        std::cout << currentNode->val << std::endl;
    //        currentNode = currentNode->next;
    //    }
    //
    //    //Problem #496 Next Greater Element I
    //
    //    vector<int> nums1 = {4, 1, 2};
    //    vector<int> nums2 = {1, 3, 4, 2};
    //
    //    nextGreaterElement(nums1, nums2);
    
    //Accessing Heaps
    //    MaxHeap myMaxHeap;
    //
    //    myMaxHeap.insert(100);
    //    myMaxHeap.insert(75);
    //    myMaxHeap.insert(80);
    //    myMaxHeap.insert(55);
    //    myMaxHeap.insert(50);
    //    myMaxHeap.insert(60);
    //
    //    myMaxHeap.printHeap();
    //
    //    myMaxHeap.remove();
    //
    //    myMaxHeap.printHeap();
    
    //Find Kth Largest
    //    vector<int> nums = {3,2,3,1,2,4,5,5,6};
    //    int k = 4;
    //    cout << findKthLargest(nums, k) << endl;
    
    
    //Overlapping Intervals
    //    vector<vector<int>> listsOfLists = {{1, 3}, {2, 6}, {15, 18}, {8, 10}};
    //
    ////    vector<vector<int>> listsOfLists = {{1, 4}, {4, 5}};
    //    vector<vector<int>> mergedLists = mergeIntervals(listsOfLists);
    //
    //    for(size_t i = 0; i < mergedLists.size(); ++i)
    //    {
    //        for(size_t j = 0; j < mergedLists[i].size(); ++j)
    //        {
    //            cout << mergedLists[i][j] << " ";
    //        }
    //        cout << endl;
    //    }
    
    //    // Tree Traversal
    //    TreeNode root = TreeNode(3);
    //    TreeNode node1 = TreeNode(1);
    //    TreeNode node2 = TreeNode(5);
    //    TreeNode node3 = TreeNode(0);
    //    TreeNode node4 = TreeNode(2);
    //    TreeNode node5 = TreeNode(4);
    //    TreeNode node6 = TreeNode(6);
    //
    //    root.left = &node1;
    //    root.right = &node2;
    //    node1.left = &node3;
    //    node1.right = &node4;
    //    node2.left = &node5;
    //    node2.right = &node6;
    //
    //    preOrder(&root);
    //    cout << endl;
    //    inOrder(&root);
    //    cout << endl;
    //    postOrder(&root);
    //    cout << endl;
    //
    //    vector<vector<int>> listoflist = levelOrder(&root);
    //    for(int i = 0; i < listoflist.size(); i++)
    //    {
    //        for(int j = 0; j < listoflist[i].size(); j++)
    //        {
    //            cout << listoflist[i][j] << " ";
    //        }
    //        cout << endl;
    //    }
    
    //#Problem #1456. Maximum Number of Vowels in a Substring of Given Length
    
    //    string s = "leetcode";
    //    int k = 2;
    //    cout << maxVowels(s, k) << endl;
    
    //Depth First Search Comprehension
    
//    vector<vector<int>> A = {{0, 1}, {1, 2}, {0, 3}, {3, 4}, {3, 6}, {3, 7}, {4, 2}, {4, 5}, {5, 2}};
//
//    depthFirstSearchList(A, 0);
    
//    vector<vector<int>> times = {{2,1,1}, {2,3,1}, {3,4,1}};
//    int n = 4;
//    int k = 2;
//
//    cout << networkDelayTime(times, n, k) << endl;
    
    //Problem #1 Two Sum
    
//    vector<int> nums = {2, 7, 11, 15};
//    int target = 9;
//    vector<int> solution = twoSum(nums, target);
//
//    for(int i = 0; i < solution.size(); i++)
//    {
//        cout << solution[i] << " ";
//    }
//    cout << endl;
//
    
    //Problem #167 Two Sum II - Input Array is Sorted
//    vector<int> numbers = {2, 7, 11, 15};
//    int target = 9;
//
//    vector<int> answerthis = twoSum2(numbers, target);
//
//    for(size_t i = 0; i < answerthis.size(); ++i)
//    {
//        cout << answerthis[i] << " ";
//    }
//    cout << endl;
//
    //Problem #347 Top K Frequent Elements
    
//    vector<int> nums =  {-1, -1};
//    int k = 1;
//
//    vector<int> topKFrequentElements = topKFrequent(nums, k);
//
//    for(int i = 0; i < topKFrequentElements.size(); i++)
//    {
//        cout << topKFrequentElements[i] << endl;
//    }
    
    //Problem #200 Number of Islands
//    vector<vector<char>> grid = {
//        {'1','1','1','1','0'},
//        {'1','1','0','1','0'},
//        {'1','1','0','0','0'},
//        {'0','0','0','0','0'}
//    };
    
//    vector<vector<char>> grid = {
//        {'1','1','0','0','0'},
//        {'1','1','0','0','0'},
//        {'0','0','1','0','0'},
//        {'0','0','0','1','1'}
//    };
//
//    cout << numIslands(grid) << endl;
    
    // Problem #78 Subsets
//    vector<int> nums = {1, 2, 3};
//
//    vector<vector<int>> powerSet = subsets(nums);
//
//    for(const auto& iterator: powerSet){
//        for(int i = 0; i < iterator.size(); i++)
//        {
//            cout << iterator[i] << " ";
//        }
//        cout << ", " << endl;
//    }
    
    //Problem #151 Reverse Words in a String
//    string s = "  hello world  ";
//
//    string answer = reverseWords(s);
//    cout << answer << endl;
//
//    cout << s.size() << endl;
//    cout << answer.size() << endl;
    
    //Problem #509 Fibonacci Number
//    cout << fib(3) << endl;
    
    //Problem #525 Contiguous Array
//    vector<int> nums = {1, 1, 1, 0, 0};
//    cout << findMaxLength(nums) << endl;
//
    //Problem #560 Subarray Sum Equals K
//    vector<int> nums = {1, 1, 1};
//    int k = 2;
//
//    cout << subArraySum(nums, k) << endl;
    
    //Problem #15 3Sum
//    vector<int> nums = {-2, 0, 1, 1, 2};
//    vector<vector<int>> result = threeSum(nums);
//
//    for(int i = 0; i < result.size(); i++)
//    {
//        for(int j = 0; j < result[i].size(); j++)
//        {
//            cout << result[i][j] << " ";
//        }
//        cout << endl;
//    }
//    cout << endl;
    
    //Problem #11 Container With The Most Water
//    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
//
//    cout << maxArea(height) << endl;
    
    // Problem #3 Longest Substring Without Repeating Characters
//    string s = "abcabcbb";
//    cout << lengthOfLongestSubstring(s) << endl;
//
    // Problem #76 Minimum Window Substring
//    string s = "a";
//    string t = "aa";
//
//    cout << minWindow(s, t) << endl;
    
    //Problem #202 Happy Number
//    int n = 19;
//    
//    cout << isHappy(n) << endl;
    
    //Problem #287 Find The Duplicate Number
    vector<int> nums = {1, 3, 4, 2, 2};
    
    cout << findDuplicate(nums) << endl;
    //TESTING
//    set<vector<int>> mySet = {{1, 2}, {3,    4}};
//    
//    if(mySet.find({3,  4, 0}) != mySet.end())
//    {
//        cout << "The coordinate is in the set." << endl;
//    }
//    else
//    {
//        cout << "The coordinate is not in the set." << endl;
//    }
    return EXIT_SUCCESS;
    
    
}
