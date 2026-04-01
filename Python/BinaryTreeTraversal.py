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
    #Problem #104 Maximum Depth of Binary Tree - Easy
     
    if root == None:
        return 0
    
    depthCount = 0
    
    nodeQueue = deque([root])
    
    while nodeQueue:
        depthCount += 1
        for index in range(len(nodeQueue)):
            node = nodeQueue.popleft()
            if node.left != None:
                nodeQueue.append(node.left)
            
            if node.right != None:
                nodeQueue.append(node.right)
            
    return depthCount

def widthOfBinaryTree(root: TreeNode) -> int:
    #Problem #662 Maximum Width of Binary Tree - Medium - Solution Concept by YouTube Channel Timothy H Chang - Understanding the Solution
    
    nodeQueueIndex =  deque([(root, 1)])
    maxWidth = 0
    
    while nodeQueueIndex:
        leftMostNode, lefttIndex = nodeQueueIndex[0]
        rightMostNode, rightIndex = nodeQueueIndex[len(nodeQueueIndex) - 1]
        
        maxWidth = max(maxWidth, rightIndex - lefttIndex + 1)
        
        for index in range(len(nodeQueueIndex)):
            node, indexNode = nodeQueueIndex.popleft()
            if node.left != None:
                nodeQueueIndex.append((node.left, 2 * indexNode))
            if node.right != None:
                nodeQueueIndex.append((node.right, 2 * indexNode + 1))
    
    return maxWidth

def maxPathSum(root: TreeNode) -> int:
    #Problem #124 Binary Tree Maximum Path Sum - Hard - Solution from a Submitted Code in LeetCode 
    #Understanding the Solution

    maxSum = [float('-inf')]
    
    def maxPathDFS(node: TreeNode):
        if node == None:
            return 0
        
        if node.left == None and node.right == None:
            maxSum[0] = max(maxSum[0], node.val)
            return node.val
        
        leftNodeValue = max(maxPathDFS(node.left), 0)
        rightNodeValue = max(maxPathDFS(node.right), 0)
        
        maxSum[0] = max(maxSum[0], leftNodeValue + node.val + rightNodeValue)
        
        return max(leftNodeValue, rightNodeValue) + node.val
    
    maxPathDFS(root)
    
    return maxSum[0]
    
def levelOrderBottom(root: TreeNode) -> list[list[int]]:
    #Problem #107 Binary Tree Level Order Traversal II - Medium
    
    if root == None:
        return []
    
    nodeQueue = deque([root])
    bottomToTopLevelOrder = []
    levelValues = [root.val]
    
    while nodeQueue:
        bottomToTopLevelOrder.append(levelValues)
        levelValues = []
        for index in range(len(nodeQueue)):
            node = nodeQueue.popleft()
            if node.left != None:
                levelValues.append(node.left.val)
                nodeQueue.append(node.left)
            if node.right != None:
                levelValues.append(node.right.val)
                nodeQueue.append(node.right)
    
    bottomToTopLevelOrder.reverse()
    
    return bottomToTopLevelOrder

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
   
   nodeNegative10.left = node9
   nodeNegative10.right = node20
   node20.left = node15
   node20.right = node7

   root = nodeNegative10
   
   print(maxPathSum(root))