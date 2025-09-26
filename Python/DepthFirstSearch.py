from collections import deque

class TreeNode:
    #Definition for a binary tree node. LeetCode Problem #113 Path Sum II
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def edgeListToDict(edgeList: list[list] ) -> dict:
        dictMap = {}

        for i in edgeList:
            if i[0] in dictMap:
                dictMap[i[0]].append(i[1])
            else:
                 dictMap[i[0]] = [i[1]]

        return dictMap


def deptFirstSearchEdgeList(directedEdgeToList, rootSource: int):
    if directedEdgeToList is None:
          return []
    
    dictionaryMap = edgeListToDict(directedEdgeToList)

    print(dictionaryMap)

    myStack = deque()
    myStack.append(rootSource)
    seen = [rootSource]
    
    while myStack:
         number = myStack.pop()
         print(number)
         if number not in dictionaryMap:
              continue
         for i in dictionaryMap[number]:
              if i not in seen:
                   seen.append(i)
                   myStack.append(i)

def arrayOfEdgesToAdjacencyMatrix(araryEdges: list[list], rows: int, columns: int) -> list[list]:
     matrix = []

     for i in range(rows):
          matrix.append([])
          for j in range(columns):
               matrix[i].append(0)
     
     for i in araryEdges:
          matrix[i[0]][i[1]] = 1
     
     return matrix

class Node:
     def __init__(self, val = 0, neighbors = None):
          self.val = val
          self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
     #Problem #133 Clone Graph - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
     
     originalAndCopy = {}
     
     def depthFirstSearchClone(node: Node, originalAndCopy):
          if node in originalAndCopy:
               return originalAndCopy[node]
          
          nodeCopy = Node(node.val)
          originalAndCopy[node] = nodeCopy
          
          for point in node.neighbors:
               nodeCopy.neighbors.append(depthFirstSearchClone(point, originalAndCopy))
          return nodeCopy
     
     return depthFirstSearchClone(node, originalAndCopy) if node is not None else None

def pathSum(root: TreeNode, targetSum: int)-> list[list[int]]:
     #Problem #113 Path Sum II - Solution Concept by YouTuber Deepti Talesra - Understanding the Solution
     
     if root is None:
          return []
     
     sumPath = [targetSum]
     pathList: list[int] = []
     returnPathList: list[list[int]] = []
     
     def depthFirstSearchPathSumTarget(node: TreeNode):
          if node.left is None and node.right is None:
               
               if sumPath[0] - node.val == 0:
                    pathList.append(node.val)
                    copyPathList = pathList.copy()
                    returnPathList.append(copyPathList)
                    pathList.pop()
               
               return
     
          pathList.append(node.val)
          sumPath[0] -= node.val
          
          if node.left:
               depthFirstSearchPathSumTarget(node.left)
          
          if node.right:
               depthFirstSearchPathSumTarget(node.right)
          
          pathList.pop()
          sumPath[0] += node.val
          
          return 

     depthFirstSearchPathSumTarget(root)
     
     return returnPathList
                              
if __name__ == "__main__":
     node1 = TreeNode(1)
     node1Duplicate = TreeNode(1)
     node2 = TreeNode(2)
     node3 = TreeNode(3)
     node4 = TreeNode(4)
     node5 = TreeNode(5)
     node6 = TreeNode(6)
     node7 = TreeNode(7)
     node8 = TreeNode(8)
     node11 = TreeNode(11)
     node13 = TreeNode(13)
     node4Duplicate = TreeNode(4)
     node5Duplicate = TreeNode(5)
     
     # node5.left = node4
     # node5.right = node8
     
     # node4.left = node11
     
     # node11.left = node7
     # node11.right = node2
     
     # node8.left = node13
     # node8.right = node4Duplicate
     
     # node4Duplicate.left = node5Duplicate
     # node4Duplicate.right = node1
     
     node1.left = node1Duplicate
     node1.right = node3
     
     root = node1
     targetSum = 5
     
     print(pathSum(root, targetSum))