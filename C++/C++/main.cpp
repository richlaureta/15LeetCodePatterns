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
//    vector<int> nums = {1, 3, 4, 2, 2};
//    
//    cout << findDuplicate(nums) << endl;
    
    //Problem #92 Reverse Linked List II
//    ListNode* head = new ListNode(1);
//    ListNode* node2 = new ListNode(2);
//    ListNode* node3 = new ListNode(3);
//    ListNode* node4 = new ListNode(4);
//    ListNode* node5 = new ListNode(5);
//   
//    int leftIndex = 1;
//    int rightIndex = 3;
//    
//    head->next = node2;
//    node2->next = node3;
//    node3->next = node4;
//    node4->next = node5;
//    
//    ListNode* editedLinkedList = reverseBetween(head, leftIndex, rightIndex);
//    
//    while(editedLinkedList != nullptr)
//    {
//        cout << editedLinkedList->val << endl;
//        editedLinkedList = editedLinkedList->next;
//    }
    
    //Problem # 24 Swap Nodes in Pairs
//    ListNode* head = new ListNode(1);
//    ListNode* node2 = new ListNode(2);
//    ListNode* node3 = new ListNode(3);
//    ListNode* node4 = new ListNode(4);
//    ListNode* node5 = new ListNode(5);
//    
//    head->next = node2;
//    node2->next = node3;
//    node3->next = node4;
//    node4->next = node5;
//    
//    ListNode* swappedPairs = swapPairs(head);
//    
//    while(swappedPairs != nullptr)
//    {
//        cout << swappedPairs->val << endl;
//        swappedPairs = swappedPairs->next;
//    }
    
    //Problem #739 Daily Temperatures
//    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
//    
//    vector<int> daysToWaitForIncrease = dailyTemperatures(temperatures);
//    
//    for(int i = 0; i < daysToWaitForIncrease.size(); i++)
//    {
//        cout << daysToWaitForIncrease[i] << endl;
//    }
    
    //Problem #84 Largest Rectangle in Histogram
//    vector<int> heights = {2, 1, 5, 6, 2, 3};

    
    //Problem #373 Find K Pairs with Smallest Sums
//    vector<int> nums1 = {1, 7, 11};
//    vector<int> nums2 = {2, 4, 6};
//    int k = 3;
//    
//    vector<vector<int>> smallestPairs = kSmallestPairs(nums1, nums2, k);
//    cout << "[";
//    for(int i = 0; i < smallestPairs.size(); i++)
//    {
//        cout << "[";
//        for(int j = 0; j < smallestPairs[i].size(); j++)
//        {   if (j == 0)
//            {
//                cout << smallestPairs[i][j] << ", ";
//            }
//            else
//            {
//                cout << smallestPairs[i][j] << "]";
//            }
//        }
//        if (i != smallestPairs.size() - 1)
//        {
//            cout << ", ";
//        }
//    }
//    
//    cout << "]" << endl;
    
    //Problem #57 Insert Interval
//    vector<vector<int>> intervals = {{1, 3}, {6, 9}};
//    vector<int> newInterval = {2, 5};
//    
//    vector<vector<int>> inserted = insert(intervals, newInterval);
//    
//    for(int i = 0; i < inserted.size(); i++)
//    {
//        for(int j = 0; j < inserted[i].size(); j++)
//        {
//            cout << inserted[i][j] << " ";
//        }
//        cout << endl;
//    }
//
//    //Problem #435 Non-overlapping Intervals
//    vector<vector<int>> intervals = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
//    
//    cout << eraseOverlapIntervals(intervals) << endl;
    
    //Problem #33 Search in Rotated Sorted Array
//    
//    vector<int> nums = {7, 1, 2, 3, 4, 5, 6};
//    int target = 5;
//    
//    cout << modifiedBinarySearch(nums, target) << endl;
    
    //Problem #153 Find Minimum in Rotated Sorted Array
//    vector<int> nums = {3, 4, 5, 1, 2};
//    
//    cout << findMin(nums) << endl;
    
    //Problem #240 Search a 2D Matrix II
//    vector<vector<int>> matrix =
//    {
//        {1, 4, 7, 11, 15},
//        {2, 5, 8, 12, 19},
//        {3, 6, 9, 16, 22},
//        {10, 13, 14, 17, 24},
//        {18, 21, 23, 26, 30}
//    };
//    
//    int target = 5;
//    
//    cout << searchMatrix(matrix, target) << endl;
    
    //Problem #257 Binary Tree Paths
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node5 = TreeNode(5);
//    
//    node1.left = &node2;
//    node1.right = &node3;
//    node2.right = &node5;
//    
//    TreeNode root = node1;
//    
//    binaryTreePaths(&root);
    
    //Problem #230 Kth Smallest Element in a BST
    
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node4 = TreeNode(4);
//    TreeNode node5 = TreeNode(5);
//    TreeNode node6 = TreeNode(6);
//    
//    node5.left = &node3;
//    node5.right = &node6;
//    
//    node3.left = &node2;
//    node3.right = &node4;
//    
//    node2.left = &node1;
//    
//    TreeNode *root = &node5;
//    int k = 3;
//    
//    cout << kthSmallest(root, k) << endl;
    //Problem 104 Maximum Depth of Binary Tree
    
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node4 = TreeNode(4);
//    TreeNode node5 = TreeNode(5);
//    TreeNode node6 = TreeNode(6);
//    TreeNode node7 = TreeNode(7);
//    TreeNode node9 = TreeNode(9);
//    TreeNode node20 = TreeNode(20);
//    TreeNode node15 = TreeNode(15);
//    
//    
//    node3.left = &node9;
//    node3.right = &node20;
//    
//    node20.left = &node15;
//    node20.right = &node7;
//    
//    TreeNode *root = &node3;
//    
//    cout << maxDepth(root) << endl;
//
    //Problem #662 Maximum Width of Binary Tree - Solution Concept by YouTuber NeetCodeIO - Understanding the Solution
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node3Duplicate = TreeNode(3);
//    TreeNode node4 = TreeNode(4);
//    TreeNode node5 = TreeNode(5);
//    TreeNode node6 = TreeNode(6);
//    TreeNode node7 = TreeNode(7);
//    TreeNode node9 = TreeNode(9);
//    TreeNode node20 = TreeNode(20);
//    TreeNode node15 = TreeNode(15);
//    
//    node1.left = &node3;
//    node1.right = &node2;
//    
//    node3.left = &node5;
//    node3.right = &node3Duplicate;
//    
//    node2.right = &node9;
//    
//    TreeNode root = node1;
//    
//    cout << widthOfBinaryTree(&root) << endl;
    //Problem #124 Binary Tree Maximum Path Sum - Concept Solution by YouTube Channel NeetCode - Understanding the Solution
    
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node3Duplicate = TreeNode(3);
//    TreeNode node4 = TreeNode(4);
//    TreeNode node5 = TreeNode(5);
//    TreeNode node6 = TreeNode(6);
//    TreeNode node7 = TreeNode(7);
//    TreeNode node9 = TreeNode(9);
//    TreeNode node20 = TreeNode(20);
//    TreeNode node15 = TreeNode(15);
//    TreeNode nodeNegative10 = TreeNode(-10);
//    
//    nodeNegative10.left = &node9;
//    nodeNegative10.right = &node20;
//    
//    node20.left = &node15;
//    node20.right = &node7;
//    
//    TreeNode root = nodeNegative10;
//    
//    cout << maxPathSum(&root) << endl;
    //Problem #107 Binary Tree Level Order Traversal II - Solution Concept by YouTube Channel NeetCode
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node3Duplicate = TreeNode(3);
//    TreeNode node4 = TreeNode(4);
//    TreeNode node5 = TreeNode(5);
//    TreeNode node6 = TreeNode(6);
//    TreeNode node7 = TreeNode(7);
//    TreeNode node9 = TreeNode(9);
//    TreeNode node20 = TreeNode(20);
//    TreeNode node15 = TreeNode(15);
//    TreeNode nodeNegative10 = TreeNode(-10);
//    
//    node3.left = &node9;
//    node3.right = &node20;
//    
//    node20.left = &node15;
//    node20.right = &node7;
//    
//    TreeNode *root = &node3;
//    
//    vector<vector<int>> answer = levelOrderBottom(root);
//    
//    for(int i = 0; i < answer.size(); i++)
//    {
//        for(int j = 0; j < answer[i].size(); j++)
//        {
//            cout << answer[i][j] << " ";
//        }
//        cout << endl;
//    }
    //Problem #133 Clone Graph - Solution Concept by YouTube Channel Sean Chuah - Understanding the Solution
//    
//    Node node1 = Node(1);
//    Node node2 = Node(2);
//    Node node3 = Node(3);
//    Node node4 = Node(4);
//    
//    node1.neighbors =  {&node2, &node4};
//    node2.neighbors = {&node1, &node3};
//    node3.neighbors = {&node2, &node4};
//    node4.neighbors = {&node1, &node3};
//    
//    cloneGraph(&node1);
    
    //Problem #113 Path Sum II
//    
//    TreeNode node5 = TreeNode(5);
//    TreeNode node4 = TreeNode(4);
//    TreeNode node11 = TreeNode(11);
//    TreeNode node7 = TreeNode(7);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node8 = TreeNode(8);
//    TreeNode node13 = TreeNode(13);
//    TreeNode node4Duplicate = TreeNode(4);
//    TreeNode node5Duplicate = TreeNode(5);
//    TreeNode node1 = TreeNode(1);
//    
//    node5.left = &node4;
//    node5.right = &node8;
//    
//    node4.left = &node11;
//    
//    node11.left = &node7;
//    node11.right = &node2;
//    
//    node8.left = &node13;
//    node8.right = &node4Duplicate;
//    
//    node4Duplicate.left = &node5Duplicate;
//    node4Duplicate.right = &node1;
//    
//    TreeNode *root = &node5;
//    
//    int targetSum = 22;
//    
//    vector<vector<int>> pathSumLists = pathSum(root,targetSum);
//    
//    for(int i = 0; i < pathSumLists.size(); i++)
//    {
//        for(int j = 0; j < pathSumLists[i].size(); j++)
//        {
//            cout << pathSumLists[i][j] << " ";
//        }
//        cout << endl;
//    }
//    //Problem # 207 Course Schedule - Concept Solution by Deepti Talesra - Understanding the Solution
//    
//    int numCourses = 5;
//    vector<vector<int>> prerequisites = {{1, 0}, {0, 1}};
//    
//    cout << canFinish(numCourses, prerequisites) << endl;
    
    //Problem #210 Course Schedule II - Concept Solution by NeetCode - Understanding the Solution
    
//    int numCourses = 2;
//    vector<vector<int>> prerequisites = {{1, 0}};
//    
//    vector<int> path = findOrder(numCourses, prerequisites);
//    
//    for(int i = 0; i <((int) path.size()); i++)
//    {
//        cout << path[i] << endl;
//    }
    
    //Problem #107 Binary Tree Level Order Traversal II
//    TreeNode node1 = TreeNode(1);
//    TreeNode node2 = TreeNode(2);
//    TreeNode node3 = TreeNode(3);
//    TreeNode node9 = TreeNode(9);
//    TreeNode node20 = TreeNode(20);
//    TreeNode node15 = TreeNode(15);
//    TreeNode node7 = TreeNode(7);
//    
//    node3.left = &node9;
//    node3.right = &node20;
//    node20.left = &node15;
//    node20.right = &node7;
//    
//    TreeNode *root = nullptr;
//    
//    vector<vector<int>> levelTraversal = levelOrderI(root);
//    
//    for(int i = 0; i < levelTraversal.size(); i++)
//    {
//        for(int j = 0; j < levelTraversal[i].size(); j++)
//        {
//            cout << levelTraversal[i][j] << " ";
//        }
//        
//        cout << endl;
//    }
//
    
    //Problem #994 Rotting Oranges - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
//    vector<vector<int>> grid = {
//        {2, 1, 1},
//        {0, 1, 1},
//        {1, 0, 1}
//    };
//    
//    cout << orangesRotting(grid) << endl;
    
    //Problem #127 Word Ladder: Hard - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
//    
//    string beginWord = "hit";
//    string endWord = "cog";
//    
//    vector<string> wordList = {"hot", "dot", "dog", "lot", "log"};
//    
//    cout << ladderLength(beginWord, endWord, wordList) << endl;
    
    //Problem #733 Flood Fill - Easy
    
//    vector<vector<int>> image = {
//        {0, 0, 0},
//        {0, 0, 0},
//        {0, 0, 0}
//    };
//    
//    int sr = 0;
//    int sc = 0;
//    int color = 0;
//    
//    vector<vector<int>> editedImage = floodFill(image, sr, sc, color);
//    
//    for(int i = 0; i < editedImage.size(); i++)
//    {
//        for(int j = 0; j < editedImage[i].size(); j++)
//        {
//            cout << editedImage[i][j] << " ";
//        }
//        cout << endl;
//    }
    //Problem #130 Surrounded Regions - Medium
//    vector<vector<char>> board = {
//        {'X', 'X', 'X', 'X'},
//        {'X', 'O', 'O', 'X'},
//        {'X', 'X', 'O', 'X'},
//        {'X', 'O', 'X', 'X'}
//    };
//    vector<vector<char>> board = {
//        {'X'}
//    };
//    solve(board);
//    
//    for(int i = 0; i < board.size(); i++)
//    {
//        for(int j = 0; j < board[i].size(); j++)
//        {
//            cout << board[i][j] << " ";
//        }
//        cout << endl;
//    }

    //Problem #46 Permutaions - Medium - Solution Concept by Greg Hogg - Understanding the Solution
//    vector<int> nums = {1, 2, 3};
//    
//    vector<vector<int>> answer = permute(nums);
//    
//    for(int i = 0; i < answer.size(); i++)
//    {
//        for(int j = 0; j < answer[i].size(); j++)
//        {
//            cout << answer[i][j] << " ";
//        }
//        cout << endl;
//    }
    
    //Problem #51 N-Queens - Hard - Solution Concept by NeetCode - Understanding the Solution
    int n = 4;
    
    vector<vector<string>> answer = solveNQueens(n);
    
    for(int i = 0; i < answer.size(); i++)
    {
        for(int j = 0; j < answer[i].size(); j++)
        {
            cout << answer[i][j] << endl;
        }
        cout << "---------------------" << endl;
    }
    //TESTING VsCode with C++ in WINDOWS
//    string s = "magaran";
//    string t = "anagram";
//    
//    cout << isAnagram(s, t) << endl;
    
    return EXIT_SUCCESS;
}
