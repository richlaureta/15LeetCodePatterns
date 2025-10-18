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
    
if __name__ == "__main__":
    grid = [
        [0, 2]
    ]
    
    print(orangesRotting(grid))
    
    