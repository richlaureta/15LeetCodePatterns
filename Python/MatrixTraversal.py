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
    
    connectedSqauresQueue = deque()
    seenSqaureCells = set()
    
    for index in range(len(board)):
        for index1 in range(len(board[0])):
            if ((index, index1) not in seenSqaureCells and
                board[index][index1] == 'O' and 
                index > 0 and 
                index < len(board) - 1 and
                index1 > 0 and
                index1 < len(board[0]) - 1):
                
                connectedSquaresList = [[index, index1]]
                connectedSqauresQueue.append([index, index1])
                seenSqaureCells.add((index, index1))
                
                connectedToEdgeFlag = False
                
                while connectedSqauresQueue:
                    for index2 in range(len(connectedSqauresQueue)):
                        row, column = connectedSqauresQueue.popleft()
                        
                        leftDirection = [row, column - 1]
                        upDirection = [row - 1, column]
                        rightDirection = [row, column + 1]
                        downDirection = [row + 1, column]
                        
                        if (leftDirection[1] > -1 and
                            (leftDirection[0], leftDirection[1]) not in seenSqaureCells and
                            board[leftDirection[0]][leftDirection[1]] == 'O'):
                            if leftDirection[1] == 0:
                                connectedToEdgeFlag = True
                                
                            seenSqaureCells.add((leftDirection[0], leftDirection[1]))
                            connectedSqauresQueue.append([leftDirection[0], leftDirection[1]])
                            connectedSquaresList.append([leftDirection[0], leftDirection[1]])
                        
                        if (upDirection[0] > -1 and 
                            (upDirection[0], upDirection[1]) not in seenSqaureCells and
                            board[upDirection[0]][upDirection[1]] == 'O'):
                            if upDirection[0] == 0:
                                connectedToEdgeFlag = True
                                
                            seenSqaureCells.add((upDirection[0], upDirection[1]))
                            connectedSqauresQueue.append([upDirection[0], upDirection[1]])
                            connectedSquaresList.append([upDirection[0], upDirection[1]])
                            
                        if (rightDirection[1] < len(board[0]) and
                            (rightDirection[0], rightDirection[1]) not in seenSqaureCells and 
                            board[rightDirection[0]][rightDirection[1]] == 'O'):
                            if rightDirection[1] == len(board[0]) - 1:
                                connectedToEdgeFlag = True
                                
                            seenSqaureCells.add((rightDirection[0], rightDirection[1]))
                            connectedSqauresQueue.append([rightDirection[0], rightDirection[1]])
                            connectedSquaresList.append([rightDirection[0], rightDirection[1]])
                        
                        if (downDirection[0] < len(board) and
                            (downDirection[0], downDirection[1]) not in seenSqaureCells and
                            board[downDirection[0]][downDirection[1]] == 'O'):
                            if downDirection[0] == len(board) - 1:
                                connectedToEdgeFlag = True
                                
                            seenSqaureCells.add((downDirection[0], downDirection[1]))
                            connectedSqauresQueue.append([downDirection[0], downDirection[1]])
                            connectedSquaresList.append([downDirection[0], downDirection[1]])
                        
                if connectedToEdgeFlag == False:
                    for square in connectedSquaresList:
                        board[square[0]][square[1]] = 'X'

                                             
if __name__ == "__main__":
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    
    # board = [["X"]]
    print(solve(board))