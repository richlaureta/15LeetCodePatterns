from collections import deque
from collections import defaultdict
import copy

class Node:
     def __ini__(self, val = 0, neighbors = None):
          self.val = val
          self.neighbors = neighbors if neighbors is not None else []

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

def cloneGraph(node: Node) -> Node:
     #Problem #133 Clone Graph - Medium
     
     return copy.deepcopy(node)
                    
def pathSum(root: TreeNode, targetSum: int)-> list[list[int]]:
     #Problem #113 Path Sum II - Medium
     
     sumPath = [0]
     pathToTargetSum = []
     path = []
     
     def pathSumTargetDFS(node: TreeNode):
          if node == None:
               return
          
          sumPath[0] += node.val
          path.append(node.val)
          
          if node.left == None and node.right == None:
               if sumPath[0] == targetSum:
                    pathToTargetSum.append(path.copy())
               path.pop()
               sumPath[0] -= node.val
               return
          
          pathSumTargetDFS(node.left)
          pathSumTargetDFS(node.right)
          
          path.pop()
          sumPath[0] -= node.val
     
     pathSumTargetDFS(root)
     
     return pathToTargetSum
          
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
     #Problem #210 Course Schedule II - Medium - Solution Concept by YouTube Channel NeetCode - Understanding the Solution
     
     cycleSet = set()
     visitedCourseSet = set()
     
     prerequisitesDictionary = defaultdict(list[int])
     prerequisitesPath = []
     
     for coursePrerequisite in prerequisites:
          prerequisitesDictionary[coursePrerequisite[0]].append(coursePrerequisite[1])
     
     def findOrderDFS(course: int) -> bool:
          if course in visitedCourseSet:
               return True
               
          if course in cycleSet:
               return False
          
          cycleSet.add(course)
          
          for course1 in prerequisitesDictionary[course]:
               if findOrderDFS(course1) == False:
                    return False
               
          prerequisitesPath.append(course)
          visitedCourseSet.add(course)
          cycleSet.remove(course)
          return True
     
     for index in range(numCourses):
          if findOrderDFS(index) == False:
               return []

     return prerequisitesPath

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
     
     prerequisites = []
     
     print(findOrder(1, prerequisites))