from collections import deque
import collections

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
    #Problem #102 Binary Tree Level Order Traversal - Medium
    
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
    #Problem #994 Rotting Oranges - Medium - Solution Concept by YouTube Channel - Deepti Talesra - Understanding the Solution
    
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
    #Problem #127 Word Ladder: Hard - Solution Concept by YouTube channel: NeetCode - Understanding the Solution
    
    if endWord not in wordList:
        return 0
    
    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            nei[pattern].append(word)
            
    visit = set([beginWord])
    q = deque([beginWord])
    res = 1
    
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        res += 1
        
    return 0
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    print(ladderLength(beginWord, endWord, wordList)) 