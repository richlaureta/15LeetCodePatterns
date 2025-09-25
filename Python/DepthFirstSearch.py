from collections import deque

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

if __name__ == "__main__":
     node1 = Node(1)
     node2 = Node(2)
     node3 = Node(3)
     node4 = Node(4)
     
     node1.neighbors = [node2, node4]
     node2.neighbors = [node1, node3]
     node3.neighbors = [node2, node4]
     node4.neighbors = [node1, node3]
     
     cloneGraph(node1)