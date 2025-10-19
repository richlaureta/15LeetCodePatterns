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

def orangesRotting(grid: list[list[int]]) -> int:
    #Problem #994 Rotting Oranges - Solution Concept by YouTube Channel - Deepti Talesra - Understanding the Solution
    
    minuteCount = 0
    freshOrangesCount = 0
    rottenOrangesLocation = []
    
    for row in range (0, len(grid)):
        for index in range(0, len(grid[row])):
            if grid[row][index] == 1:
                freshOrangesCount += 1
            elif grid[row][index] == 2:
                rottenOrangesLocation.append((row, index))
                
    while rottenOrangesLocation and freshOrangesCount > 0:
        minuteCount += 1
        currentList = []
        for rowNumber, columnNumber, in rottenOrangesLocation:
            adjacent = [(rowNumber + 1, columnNumber), (rowNumber - 1, columnNumber), (rowNumber, columnNumber + 1), (rowNumber, columnNumber - 1)] #Down, Up, Right, Left
            for rowIndex, columnIndex in adjacent:
                if rowIndex > -1 and columnIndex > -1 and rowIndex < len(grid) and columnIndex < len(grid[0]) and grid[rowIndex][columnIndex] == 1:
                    grid[rowIndex][columnIndex] = 2
                    freshOrangesCount -= 1
                    currentList.append((rowIndex, columnIndex))
                    
                    if freshOrangesCount == 0:
                        return minuteCount
        
        rottenOrangesLocation = currentList
    
    if freshOrangesCount == 0:
        return minuteCount
    else:
        return -1

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    #Problem #127 World Ladder: Hard - 
    
    if endWord not in wordList:
        return 0
    
    if len(beginWord) == 1:
        return 2
    
    comparisonWord = beginWord
    transformationCount = 1
    sequenceCount = 0
    
    for index0, word in enumerate(wordList):
        off1Count = 0
        if comparisonWord == word:
            continue
        for index1, character in enumerate(word):
            if comparisonWord[index1] != character:
                off1Count += 1
                
                if off1Count > 1:
                    break
        
        if off1Count == 1 or off1Count == 0:
            off1CountHere = 0
            for index2, character in enumerate(word):
                if endWord[index2] != character:
                    off1CountHere += 1
                
                if off1CountHere > 1:
                    break
                
            if off1CountHere == 1 or off1CountHere == 0:
                if off1CountHere == 1:
                    if index0 == len(wordList) - 1:
                        return transformationCount + 2
                    else:
                        return transformationCount + 2
                else:
                    return transformationCount + 1
            
            if off1Count == 1:
                sequenceCount += 1
                transformationCount += 1
                
            comparisonWord = word

    if sequenceCount == 0:
        return 0
    else:
        return transformationCount
    
if __name__ == "__main__":
    beginWord = "hot"
    endWord = "dog"
    
    wordList = ["hot", "dog", "dot"]
    
    print(ladderLength(beginWord, endWord, wordList)) 