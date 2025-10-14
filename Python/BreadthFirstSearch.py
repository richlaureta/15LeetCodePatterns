from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
    #Problem #102 Binary Tree Level Order Traversal
    
    if root == None:
        return []
    
    myQueue = deque()
    myQueue.appendleft(root)
    
    levelOrderList = []
    
    while myQueue:
        levelList = []
        
        for processNode in list(myQueue):
            levelList.append(processNode.val)
            node = myQueue.popleft()
            
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
            
        levelOrderList.append(levelList)
    
    return levelOrderList
           
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7
    # node9.left = node1
    # node9.right = node2
    
    # root = node3
    
    root = None
    
    print(levelOrder(root))