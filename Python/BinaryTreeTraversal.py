from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
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
    #Problem #102. Binary Tree Level Order Traversal - I learned from a youtuber Greg Hogg

    if root is None:
        return
    
    q = deque()
    q.append(root)
    ans = []

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.value)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(level)
        
    return ans

def binaryTreePaths(root: TreeNode) -> list[str]:
    #Problem #257 Binary Tree Paths - Algo.monster Concept Solution

    resultList = []
    currentPath = []

    def depthFirstSearch(node: TreeNode):
        if node is None:
            return
        
        currentPath.append(str(node.value))

        if node.left == None and node.right == None:
            resultList.append("->".join(currentPath))
        else:
             depthFirstSearch(node.left)
             depthFirstSearch(node.right)
        
        currentPath.pop()

    depthFirstSearch(root)

    return resultList
         
def kthSmallest(root: TreeNode, k: int) -> int:
    #Problem #230 Kth Smallest Element in BST

    ascendingArray = []
    
    def inOrderTraversalHere(node: TreeNode):
        if node == None:
            return
        inOrderTraversalHere(node.left)
        ascendingArray.append(node.value)
        inOrderTraversalHere(node.right)

    inOrderTraversalHere(root)
        
    return ascendingArray[k -1]

def maxDepth(root: TreeNode) -> int:
    #Problem #104 Maximum Depth of Binary Tree - Concept Solution by YouTuber Greg Hogg
    
    if root == None:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return 1 + max(left, right)

def widthOfBinaryTree(root: TreeNode) -> int:
    #Problem #662 Maximum Width of Binary Tree - Solution Concept by YouTuber NeetCodeIO - Understanding the Solution
    
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
   
   node1.left = node3
   node1.right = node2
   
   node3.left = node5
   node3.left = node3Duplicate
   
   node2.right = node9
   
   root = node1
   
   print(widthOfBinaryTree(root))
 
    