import sys
from collections import deque

def edgeListToDict(edgeList: list[list] ) -> dict:
        dictMap = {}

        for i in edgeList:
            if i[0] in dictMap:
                dictMap[i[0]].append(i[1])
            else:
                if i[1] is None:
                     dictMap[i[0]] = None
                else:
                     dictMap[i[0]] = [i[1]]

        return dictMap

def depthFirstSearch(directedEdgeToList, rootSource: int):
    if directedEdgeToList is None:
          return []
    
    dictionaryMap = edgeListToDict(directedEdgeToList)

    stack = deque()
    stack.append(rootSource)
    seen = [rootSource]
    
    while stack:
         number = stack.pop()
         print(number)
         if dictionaryMap[number] is None:
              continue
         for i in dictionaryMap[number]:
              if i not in seen:
                   seen.append(i)
                   stack.append(i)

def main():
    #Concept of Graphs

    directedEdgeToList = [[0,1],[0,3], [1,2], [2, None], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2], [5, 4], [6, None], [7, None]]

    print(depthFirstSearch(directedEdgeToList, 0))

if __name__ == "__main__":
    sys.exit(main())