from collections import deque 

def numIslands(grid: list[list[str]]) -> int:
    #Problem #200 Number of Islands - Medium
    if not grid or not grid[0]:
            return 0
        
    numberOfIslandsCount = 0
    
    for index in range(len(grid)):
        for index1 in range(len(grid[0])):
            if grid[index][index1] == "1":
                squareStack = [(index, index1)]
                numberOfIslandsCount += 1
                grid[index][index1] = '2'
                
                while squareStack:
                    row, column = squareStack.pop()
                    
                    leftDirection = [row, column - 1]
                    upDirection = [row - 1, column]
                    rightDirection = [row, column + 1]
                    downDirection = [row + 1, column]

                    if leftDirection[1] > -1 and grid[leftDirection[0]][leftDirection[1]] == "1":
                        grid[leftDirection[0]][leftDirection[1]] = '2'
                        squareStack.append([leftDirection[0], leftDirection[1]])
                    
                    if upDirection[0] > -1 and grid[upDirection[0]][upDirection[1]] == "1":
                        grid[upDirection[0]][upDirection[1]] = '2'
                        squareStack.append([upDirection[0], upDirection[1]])
                    
                    if rightDirection[1] < len(grid[0]) and grid[rightDirection[0]][rightDirection[1]] == "1":
                        grid[rightDirection[0]][rightDirection[1]] = '2'
                        squareStack.append([rightDirection[0], rightDirection[1]])
                    
                    if downDirection[0] < len(grid) and grid[downDirection[0]][downDirection[1]] == "1":
                        grid[downDirection[0]][downDirection[1]] = '2'
                        squareStack.append([downDirection[0], downDirection[1]])
                        
    return numberOfIslandsCount
                            
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    #Problem #733 Flood Fill - Easy 
    
    fillQueue = deque([[sr, sc]])
    fillColor = image[sr][sc]
    image[sr][sc] = color
    
    while fillQueue:
        for index in range(len(fillQueue)):
            row, column = fillQueue.popleft()
            
            leftDirection = [row, column - 1]
            upDirection = [row - 1, column]
            rightDirection = [row, column + 1]
            downDirection = [row + 1, column]
            
            if (leftDirection[1] > -1 and 
                image[leftDirection[0]][leftDirection[1]] == fillColor and 
                image[leftDirection[0]][leftDirection[1]] != color):
                fillQueue.append([leftDirection[0], leftDirection[1]])
                image[leftDirection[0]][leftDirection[1]] = color
                
            if (upDirection[0] > -1 and 
                image[upDirection[0]][upDirection[1]] == fillColor and
                image[upDirection[0]][upDirection[1]] != color):
                fillQueue.append([upDirection[0], upDirection[1]])
                image[upDirection[0]][upDirection[1]] = color
                
            if (rightDirection[1] < len(image[0]) and 
                image[rightDirection[0]][rightDirection[1]] == fillColor and
                image[rightDirection[0]][rightDirection[1]] != color):
                fillQueue.append([rightDirection[0], rightDirection[1]])
                image[rightDirection[0]][rightDirection[1]] = color
                
            if (downDirection[0] < len(image) and 
                image[downDirection[0]][downDirection[1]] == fillColor and
                image[downDirection[0]][downDirection[1]] != color):
                fillQueue.append([downDirection[0], downDirection[1]])
                image[downDirection[0]][downDirection[1]] = color
                
    return image

def solve(board: list[list[str]]) -> None:
    #Problem #130 Surrounded Regions - Medium
    
    visited = set()
    flipOArray = []
    locationQueue = deque()
    
    onBorderFlag = [False]
    
    def breadthFirstSearchRegion(index0: int, index1: int):
        locationQueue.append((index0, index1))
        flipOArray.append([index0, index1])
        visited.add((index0, index1))
        
        if index0 == 0 or index0 == len(board) - 1 or index1 == 0 or index1 == len(board[0]) - 1:
            onBorderFlag[0] = True
            
        while locationQueue:
            row, column = locationQueue.popleft()
            
            checkDirections = [[row - 1, column], [row, column + 1], [row + 1, column], [row, column - 1]]
            
            for direction in checkDirections:
                if direction[0] > -1 and direction[0] < len(board) and direction[1] > -1 and direction[1] < len(board[0]) and board[direction[0]][direction[1]] == "O" and (direction[0], direction[1]) not in visited:
                    visited.add((direction[0], direction[1]))
                    locationQueue.append((direction[0], direction[1]))
                    flipOArray.append([direction[0], direction[1]])
                    if direction[0] == 0 or direction[0] == len(board) - 1 or direction[1] == 0 or direction[1] == len(board[0]) - 1:
                        onBorderFlag[0] = True
                    
    for index0, row in enumerate(board):
        for index1, value in enumerate(row):
            if board[index0][index1] == "O" and (index0, index1) not in visited:
                breadthFirstSearchRegion(index0, index1)
                if onBorderFlag[0] == False:
                    for x, y in flipOArray:
                        board[x][y] = "X"
                    flipOArray = []
                    
                else:
                    onBorderFlag[0] = False
                    flipOArray = []
            
if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
    
    print(numIslands(grid))