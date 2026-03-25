from collections import deque
import heapq

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
def preOrder(node: TreeNode):
        if node is None:
             return
        print(node.value, end=" ")
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node: TreeNode):
        if node is None:
             return
        inOrder(node.left)
        print(node.value, end=" ")
        inOrder(node.right)
        

def postOrder(node: TreeNode):
        if node is None:
             return

        postOrder(node.left)
        postOrder(node.right)
        print(node.value, end=" ")

def levelOrder(root: TreeNode) -> list[list[int]]:
    #Problem #102. Binary Tree Level Order Traversal - Medium - I learned from a youtuber Greg Hogg

    if root is None:
        return
    
    q = deque()
    q.append(root)
    ans = []

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(level)
        
    return ans

def binaryTreePaths(root: TreeNode) -> list[str]:
    #Problem #257 Binary Tree Paths - Easy
    
    rootToLeaf = []
    pathToLeaf = []
    
    def preOrderTraversal(node: TreeNode):     
        if node == None:
            return
        
        if node.left == None and node.right == None:
            pathToLeaf.append(str(node.val))
            rootToLeaf.append("".join(pathToLeaf))
            pathToLeaf.pop()
            return
        
        pathToLeaf.append(f'{node.val}->')
        
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
        
        pathToLeaf.pop()
    
    preOrderTraversal(root)
    
    return rootToLeaf    
         
def kthSmallest(root: TreeNode, k: int) -> int:
    #Problem #230 Kth Smallest Element in BST - Medium
    
    inOrder = []
    
    def inOrderTraversal(node: TreeNode):
        if node == None:
            return
        
        inOrderTraversal(node.left)
        inOrder.append(node.val)
        inOrderTraversal(node.right)
            
    inOrderTraversal(root)
    
    return inOrder[k - 1]

def maxDepth(root: TreeNode) -> int:
    #Problem #104 Maximum Depth of Binary Tree - Easy - Concept Solution by YouTuber Greg Hogg - Understanding the Solution
    
    if root == None:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return 1 + max(left, right)

def widthOfBinaryTree(root: TreeNode) -> int:
    #Problem #662 Maximum Width of Binary Tree - Medium - Solution Concept by YouTuber NeetCodeIO - Understanding the Solution
    
    width = 0
    
    queue = deque([[root, 1, 0]])
    previousLevel = 0
    previousNumber = 1
    
    while queue:
        node, number, level = queue.popleft()
        
        if level > previousLevel:
            previousLevel = level
            previousNumber = number
        
        width = max(width, number - previousNumber + 1)
        
        if node.left:
            queue.append([node.left, 2 * number, level + 1])
        if node.right:
            queue.append([node.right, 2 * number + 1, level + 1])
    
    return width

def maxPathSum(root: TreeNode) -> int:
    #Problem #124 Binary Tree Maximum Path Sum - Hard - Concept Solution by YouTube Channel NeetCode - Understanding the Solution

    sum = [root.value]

    def depthFirstSearch(node):
        if node == None:
            return 0

        leftMax = depthFirstSearch(node.left)
        rightMax = depthFirstSearch(node.right)
        leftMax = max(0, leftMax)
        rightMax = max(0, rightMax)

        sum[0] = max(sum[0], node.val + leftMax + rightMax)

        return node.value + max(leftMax, rightMax)

    depthFirstSearch(root)

    return sum[0]
    
def levelOrderBottom(root: TreeNode) -> list[list[int]]:
    #Problem #107 Binary Tree Level Order Traversal - Medium - Concept Solution by NeetCode
    
    answer = deque()
    doubleEndedQueue = deque()
    doubleEndedQueue.append(root)
        
    while doubleEndedQueue:
        length = len(doubleEndedQueue)
        array = []
            
        for i in range(length):
            poppedNode = doubleEndedQueue.popleft()
                
            if poppedNode:
                array.append(poppedNode.value)
                doubleEndedQueue.append(poppedNode.left)
                doubleEndedQueue.append(poppedNode.right)    
            
        if array:
            answer.appendleft(array)
            
    return list(answer)
    
if __name__ == "__main__":
   node1 = TreeNode(1)
   node2 = TreeNode(2)
   node3 = TreeNode(3)
   node3Duplicate = TreeNode(3)
   node4 = TreeNode(4)
   node5 = TreeNode(5)
   node8 = TreeNode(8)
   node9 = TreeNode(9)
   node20 = TreeNode(20)
   node15 = TreeNode(15)
   node7 = TreeNode(7)
   node6 = TreeNode(6)
   nodeNegative10 = TreeNode(-10)
   
   node5.left = node3
   node5.right = node6
   node3.left = node2
   node3.right = node4
   node2.left = node1
   
   root = node5
   
   print(kthSmallest(root, 3))