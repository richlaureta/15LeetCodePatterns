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
    
    levelOrderList = []
    nodeQueue = deque([root])
    levelList = [root.val]
    
    while nodeQueue:
        levelOrderList.append(levelList)
        levelList = []
        for index in range(len(nodeQueue)):
            node = nodeQueue.popleft()
            if node.left != None:
                nodeQueue.append(node.left)
                levelList.append(node.left.val)
            
            if node.right != None:
                nodeQueue.append(node.right)
                levelList.append(node.right.val)
        
    return levelOrderList

def orangesRotting(grid: list[list[int]]) -> int:
    #Problem #994 Rotting Oranges - Medium 

    rotSquareQueue = deque()
    thereIsA1Flag = False
    thereIsA2Flag = False
    
    square1Count = 0
    
    for index in range(len(grid)):
        for index1 in range(len(grid[0])):
            if grid[index][index1] == 1:
                square1Count += 1
                thereIsA1Flag = True
            elif grid[index][index1] == 2:
                rotSquareQueue.append([index, index1])
                thereIsA2Flag = True
                
    if thereIsA1Flag == False:
        return 0
    elif thereIsA2Flag == False and thereIsA1Flag == True:
        return -1
    
    minutesToRot = -1
    check1Count = 0
    
    while rotSquareQueue:
        for index2 in range(len(rotSquareQueue)):
            square = rotSquareQueue.popleft()
            
            leftDirection = [square[0], square[1] - 1]
            upDirection = [square[0] - 1, square[1]]
            rightDirection = [square[0], square[1] + 1]
            downDirection = [square[0] + 1, square[1]]
            
            if leftDirection[1] > -1 and grid[leftDirection[0]][leftDirection[1]] == 1:
                check1Count += 1
                grid[leftDirection[0]][leftDirection[1]] = 2
                rotSquareQueue.append(leftDirection)
            
            if upDirection[0] > -1 and grid[upDirection[0]][upDirection[1]] == 1:
                check1Count += 1
                grid[upDirection[0]][upDirection[1]] = 2
                rotSquareQueue.append(upDirection)
            
            if rightDirection[1] < len(grid[0]) and grid[rightDirection[0]][rightDirection[1]] == 1:
                check1Count += 1
                grid[rightDirection[0]][rightDirection[1]] = 2
                rotSquareQueue.append(rightDirection)
            
            if downDirection[0] < len(grid) and grid[downDirection[0]][downDirection[1]] == 1:
                check1Count += 1
                grid[downDirection[0]][downDirection[1]] = 2
                rotSquareQueue.append(downDirection)
                
        minutesToRot += 1
            
    if check1Count == square1Count:
        return minutesToRot
        
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
    # beginWord = "hit"
    # endWord = "cog"
    
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    # print(ladderLength(beginWord, endWord, wordList))
    
    # node3 = TreeNode(3)
    # node9 = TreeNode(9)
    # node20 = TreeNode(20)
    # node15 = TreeNode(15)
    # node7 = TreeNode(7)
    
    # node3.left = node9
    # node3.right = node20
    # node20.left = node15
    # node20.right = node7
    
    # root = node3
    
    grid = [[0, 2]]
    
    print(orangesRotting(grid))
    