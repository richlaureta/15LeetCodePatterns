from collections import deque
from collections import defaultdict

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
     #Problem #133 Clone Graph - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
     
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
     #Problem #113 Path Sum II - Medium - Solution Concept by YouTuber Deepti Talesra - Understanding the Solution
     
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

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
     #Problem #207 Course Schedule - Medium - Solution Concept by YouTube Channel Deepti Talesra - Understanding the Solution
     
        mapList = defaultdict(list)
              
        for course, coursePrerequisite in prerequisites:
            mapList[course].append(coursePrerequisite)

        visited = set()
        
        def cycle(courseNumber: int):
            if courseNumber in visited:
                return True
            
            visited.add(courseNumber)
            
            for subjectNumber in mapList[courseNumber]:
                if cycle(subjectNumber):
                    return True
            
            mapList[courseNumber] = []
            visited.remove(courseNumber)
            
            return False
            
        for courseNumber in range(numCourses):
            if cycle(courseNumber):
                return False
        
        return True
            
def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
     #Problem # 210 Course Schedule II - Medium - Solution Concept by NeetCode - Understanding the Solution
     
     coursePrerequisiteDictionary = defaultdict(list)
     topologyCourseList = []
     visited = set()
     cycle = set()
     
     for subjectNumber in range(numCourses):
          coursePrerequisiteDictionary[subjectNumber] = []
          
     for courseA, courseB in prerequisites:
          coursePrerequisiteDictionary[courseA].append(courseB)
          
     def depthFirstSearchCourse(courseNumber: int) -> bool:
          if courseNumber in cycle:
               return False
          
          if courseNumber in visited:
               return True
          
          cycle.add(courseNumber)
           
          for coursePrerequisite in coursePrerequisiteDictionary[courseNumber]:
               if depthFirstSearchCourse(coursePrerequisite) == False:
                    return False

          cycle.remove(courseNumber)
          visited.add(courseNumber)
          topologyCourseList.append(courseNumber)
          
          return True
          
     for courseNumber in range(numCourses):
          if depthFirstSearchCourse(courseNumber) == False:
               return []
     
     return topologyCourseList
                           
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
     
     numCourses = 4
     prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
     
     print(findOrder(numCourses, prerequisites))