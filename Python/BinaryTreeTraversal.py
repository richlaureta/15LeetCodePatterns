from collections import deque
import heapq

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
        ascendingArray.append(node.val)
        inOrderTraversalHere(node.right)

    inOrderTraversalHere(root)
        
    return ascendingArray[k -1]

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node5.left = node3
    node5.right = node6

    node3.left = node2
    node3.right = node4

    node2.left = node1

    root = node5

    k = 4

    print(kthSmallest(root, k))
    