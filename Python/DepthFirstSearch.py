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
     #Problem #210 Course Schedule II - Medium
     
     if len(prerequisites) == 0:
          courseOrder = []
          for index in range(numCourses - 1, -1, -1):
               courseOrder.append(index)
          
          return courseOrder
               
     prerequisiteDictionary = defaultdict(list[int])
     
     for course in prerequisites:
          prerequisiteDictionary[course[0]].append(course[1])
     
     orderList = []
     orderSet = set()
     
     courseQueue = deque([prerequisites[len(prerequisites) - 1][0]])
     
     orderList.append(prerequisites[len(prerequisites) - 1][0])
     orderSet.add(prerequisites[len(prerequisites) - 1][0])
     
     while courseQueue:
          for index in range(len(courseQueue)):
               poppedCourse = courseQueue.popleft()
               if (prerequisiteDictionary[poppedCourse] == [] and poppedCourse > 1):
                    return []
               for index1 in range(len(prerequisiteDictionary[poppedCourse])):
                    if (prerequisiteDictionary[poppedCourse][index1] in orderSet and 
                        poppedCourse in orderSet and 
                        (poppedCourse == 1 or poppedCourse == 0)):
                         return []
                    if prerequisiteDictionary[poppedCourse][index1] not in orderSet:
                         orderList.append(prerequisiteDictionary[poppedCourse][index1])
                         orderSet.add(prerequisiteDictionary[poppedCourse][index1])
                         courseQueue.append(prerequisiteDictionary[poppedCourse][index1])
     
     orderList.reverse()
     
     return orderList
                           
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
     
     print(findOrder(3, prerequisites))